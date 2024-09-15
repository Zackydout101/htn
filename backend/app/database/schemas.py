from supabase import create_client, Client
import json
from app.database import constants, query_constants
from app import app
from flask import request, Response, jsonify

url: str = constants.SUPABASE_URL
key: str = constants.SUPABASE_KEY

supabaseCli: Client = create_client(url, key)

def get_schema_by_website_and_user(website_url: str, user_id: str) -> dict:
    response = supabaseCli.table(query_constants.RESPONSE_SCHEMA_TABLE).select("*").eq(query_constants.WEBSITE_URL_COLUMN, website_url).eq(query_constants.USER_ID_COLUMN, user_id).execute()
    if response.data:
        return response.data[0]['json_schema']
    return None

def get_schema_by_user(user_id: str) -> dict:
    response = supabaseCli.table(query_constants.RESPONSE_SCHEMA_TABLE).select("*").eq(query_constants.USER_ID_COLUMN, user_id).execute()
    schema_data = {}
    for data in response.data:
        schema_data.append([data[query_constants.RESPONSE_SCHEMA_COLUMN], data[query_constants.WEBSITE_URL_COLUMN]])
    return schema_data

def insert_schema(website_url: str, user_id: str, schema_string: str) -> bool:
    try:
        schema = json.loads(schema_string)
        response = supabaseCli.table(query_constants.RESPONSE_SCHEMA_TABLE).insert({
            query_constants.WEBSITE_URL_COLUMN: website_url,
            query_constants.USER_ID_COLUMN: user_id,
            query_constants.RESPONSE_SCHEMA_COLUMN: schema
        }).execute()
        return True
    except Exception as e:
        print(e)
        return False

@app.route('/schema/website', methods=['POST'])
def get_schema_by_website_and_user_route():
    data = request.json
    website_url = data["website_url"]
    user_id = supabaseCli.auth.get_user().user.id
    schema = get_schema_by_website_and_user(website_url, user_id)
    if schema:
        return jsonify(schema)
    return jsonify({"error": "No schema found"}), 404

@app.route('/schema/user', methods=['GET'])
def get_schema_by_user_route():
    user_id = supabaseCli.auth.get_user().user.id
    schema = get_schema_by_user(user_id)
    res = dict()
    res["schemas"] = schema
    if schema:
        return res
    return jsonify({"error": "No schema found"}), 404

@app.route('/schema/insert', methods=['POST'])
def insert_schema_route():
    data = request.json
    website_url = data["website_url"]
    user_id = "supabase.auth.get_user().user.id"
    schema_string = data["schema_string"]
    print(website_url, schema_string)
    if insert_schema(website_url, user_id, schema_string):
        return Response("Success", status=200)
    return Response("Database error", status=400)

# testschema = '{"name": "John", "age"": 30, "city": "New York"}'
# print(insertSchema("nofrills.com2", "kevin223", testschema))
#getSchemaByWebsiteAndUser("nofrills.com", "kevin")
# {"name": "John", "age": 30, "city": "New York"}



