from flask import request, jsonify
from app import app
from app.scraper.scraper import Scraper
from app.database import page_data, schemas, api_endpoints

scraper = Scraper()

@app.route('/scrape', methods=['POST'])
def scrape_website():
    data = request.json
    website_url = data.get('website_url')
    schema = data.get('schema')

    if not website_url or not schema:
        return jsonify({"error": "Missing website_url or schema"}), 400

    user_id = request.headers.get('Authorization')  # Assuming you're passing user ID in the Authorization header
    if not user_id:
        return jsonify({"error": "User not authenticated"}), 401

    # Check if we have cached data for this website
    cached_data = page_data.get_page_data_by_website(website_url, user_id)
    if cached_data:
        # Generate API endpoint for cached data
        api_endpoint = api_endpoints.create_api_endpoint(website_url, user_id, cached_data)
        if api_endpoint:
            return jsonify({"api_endpoint": f"/api/{api_endpoint}"})
        else:
            return jsonify({"error": "Failed to create API endpoint"}), 500

    # If no cached data, perform scraping
    result = scraper.scrape(website_url, schema)

    # Store the result in the database
    if not page_data.insert_page_data(website_url, user_id, result):
        return jsonify({"error": "Failed to store page data"}), 500

    # Store the schema if it's new
    existing_schema = schemas.get_schema_by_website_and_user(website_url, user_id)
    if not existing_schema:
        if not schemas.insert_schema(website_url, user_id, schema):
            return jsonify({"error": "Failed to store schema"}), 500

    # Generate API endpoint for the scraped data
    api_endpoint = api_endpoints.create_api_endpoint(website_url, user_id, result)
    if api_endpoint:
        return jsonify({"api_endpoint": f"/api/{api_endpoint}"})
    else:
        return jsonify({"error": "Failed to create API endpoint"}), 500

@app.route('/get_schema', methods=['POST'])
def get_schema():
    data = request.json
    website_url = data.get('website_url')

    if not website_url:
        return jsonify({"error": "Missing website_url"}), 400

    user_id = request.headers.get('Authorization')  # Assuming you're passing user ID in the Authorization header
    if not user_id:
        return jsonify({"error": "User not authenticated"}), 401

    schema = schemas.get_schema_by_website_and_user(website_url, user_id)
    return jsonify(schema)