from supabase import create_client, Client
import constants, query_constants
from run import app
from flask import request, Response, jsonify
import uuid

url: str = constants.SUPABASE_URL
key: str = constants.SUPABASE_KEY

supabase: Client = create_client(url, key)

def generate_api_endpoint():
    return str(uuid.uuid4())

@app.route('/api_endpoint/create', methods=['POST'])
def create_api_endpoint():
    data = request.json
    website_url = data["website_url"]
    user_id = supabase.auth.get_user().user.id
    page_data = data["page_data"]
    
    api_endpoint = generate_api_endpoint()
    
    try:
        response = supabase.table(query_constants.API_ENDPOINTS_TABLE).insert({
            query_constants.WEBSITE_URL_COLUMN: website_url,
            query_constants.USER_ID_COLUMN: user_id,
            query_constants.API_ENDPOINT_COLUMN: api_endpoint,
            query_constants.PAGE_DATA_COLUMN: page_data
        }).execute()
        return api_endpoint
    except Exception as e:
        print(e)
        return None

@app.route('/api/<api_endpoint>', methods=['GET'])
def get_data_from_api_endpoint(api_endpoint):
    response = supabase.table(query_constants.API_ENDPOINTS_TABLE).select("*").eq(query_constants.API_ENDPOINT_COLUMN, api_endpoint).execute()
    if response.data:
        return jsonify(response.data[0][query_constants.PAGE_DATA_COLUMN])
    return jsonify({"error": "API endpoint not found"}), 404