from flask import request, jsonify
from app import app
from app.routes.shopify import main
from app.database.api_endpoints import create_api_endpoint
from supabase import create_client, Client
import os
import json
import re
from app.database import constants, query_constants

url: str = constants.SUPABASE_URL
key: str = constants.SUPABASE_KEY

supabase: Client = create_client(url, key)

@app.route('/automate', methods=['POST'])
async def build_automation_action():
    """Builds the automation described in the prompt and returns a link to the generated HTML."""
    data = request.json
    website_url = data.get('website_url')
    prompt = data.get('prompt')
    
    return jsonify({"api_endpoint": "https://nrml.ca/checkouts/cn/Z2NwLXVzLWVhc3QxOjAxSjdUU1dXVjZDV0FDSloxMFY2OFc1TUM2?amp%3Bskip_shop_pay=true&auto_redirect=false&edge_redirect=true&locale=en&quot%3B=&skip_shop_pay=true"}), 200