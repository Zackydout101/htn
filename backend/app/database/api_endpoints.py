from supabase import create_client, Client
from app.database import constants, query_constants
from app import app
from flask import request, Response, jsonify
import uuid
import json

url: str = constants.SUPABASE_URL
key: str = constants.SUPABASE_KEY

supabase: Client = create_client(url, key)

def generate_api_endpoint():
    return str(uuid.uuid4())

def create_api_endpoint(website_url: str, user_id: str, page_data: str, schema_string:str) -> str:
    api_endpoint = generate_api_endpoint()
    
    try:
        # Ensure page_data is a valid JSON string
        json.loads(page_data)  # This will raise an exception if page_data is not valid JSON
        schema = json.loads(schema_string)
        response = supabase.table(query_constants.API_ENDPOINTS_TABLE).insert({
            query_constants.WEBSITE_URL_COLUMN: website_url,
            query_constants.USER_ID_COLUMN: user_id,
            query_constants.API_ENDPOINT_COLUMN: api_endpoint,
            query_constants.PAGE_DATA_COLUMN: page_data,
            query_constants.RESPONSE_SCHEMA_COLUMN: schema
        }).execute()
        return api_endpoint
    except json.JSONDecodeError:
        print("Invalid JSON data")
        return None
    except Exception as e:
        print(e)
        return None

@app.route('/api/<api_endpoint>', methods=['GET'])
def get_data_from_api_endpoint(api_endpoint):
    response = supabase.table(query_constants.API_ENDPOINTS_TABLE).select("*").eq(query_constants.API_ENDPOINT_COLUMN, api_endpoint).execute()
    if response.data:
        page_data = response.data[0][query_constants.PAGE_DATA_COLUMN]
        try:
            # Parse the stored string as JSON
            json_data = json.loads(page_data)
            return jsonify(json_data)
        except json.JSONDecodeError:
            return jsonify({"error": "Stored data is not valid JSON"}), 500
    return jsonify({"error": "API endpoint not found"}), 404