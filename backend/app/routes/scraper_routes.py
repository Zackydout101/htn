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

    # Check if we have cached data for this website
    cached_data = page_data.getPageDataByWebsite(website_url)
    if cached_data:
        # Generate API endpoint for cached data
        api_endpoint = api_endpoints.create_api_endpoint(website_url=website_url, page_data=cached_data)
        if api_endpoint:
            return jsonify({"api_endpoint": f"/api/{api_endpoint}"})
        else:
            return jsonify({"error": "Failed to create API endpoint"}), 500

    # If no cached data, perform scraping
    result = scraper.scrape(website_url, schema)

    # Store the result in the database
    page_data.insertPageData(website_url, result)

    # Store the schema if it's new
    existing_schema = schemas.getSchemaByWebsiteAndUser(website_url)
    if not existing_schema:
        schemas.insertSchema(website_url, schema)

    # Generate API endpoint for the scraped data
    api_endpoint = api_endpoints.create_api_endpoint(website_url=website_url, page_data=result)
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

    schema = schemas.getSchemaByWebsiteAndUser(website_url)
    return jsonify(schema)