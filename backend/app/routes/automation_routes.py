from flask import request, jsonify
from app import app
from supabase import create_client, Client
from app.database.user_auth import supabase
from app.scraper.scraper import Scraper
from app.database import page_data, schemas, api_endpoints

scraper = Scraper()

@app.route('/automate', methods=['POST'])
def build_automation_action():
    """Builds the automation described in the prompt."""
    data = request.json
    website_url = data.get('website_url')
    prompt = data.get('prompt')
    return jsonify({"api_endpoint": "/test"}), 200