from supabase import create_client, Client
import json
import constants, query_constants
from flask import Flask, request, Response
from run import app

url: str = constants.SUPABASE_URL
key: str = constants.SUPABASE_KEY

supabase: Client = create_client(url, key)

@app.route('/schema/website', methods=['POST'])
def getSchemaByWebsiteAndUser() -> dict:
  data = request.json  # Get the JSON data sent in the request
  website_url = data["website_url"]
  user_id = supabase.auth.get_user().user.id
  response = supabase.table(query_constants.RESPONSE_SCHEMA_TABLE).select("*").eq(query_constants.WEBSITE_URL_COLUMN, website_url).eq(query_constants.USER_ID_COLUMN, user_id).execute()
  if response.data:
    return response.data[0]['json_schema']
  return None

@app.route('/schema/insert', methods=['POST'])
def insertSchema() -> bool:
  data = request.json  # Get the JSON data sent in the request
  website_url = data["website_url"]
  user_id = supabase.auth.get_user().user.id
  schema_string = data["schema_string"]
  try:
    schema = json.loads(schema_string)
    response = supabase.table(query_constants.RESPONSE_SCHEMA_TABLE).insert({
      query_constants.WEBSITE_URL_COLUMN: website_url,
      query_constants.USER_ID_COLUMN: user_id,
      query_constants.RESPONSE_SCHEMA_COLUMN: schema
    }).execute()
    return Response("Success", status=200)
  except Exception as e:
    print(e)
    return Response("Database error", status=400)

# testschema = '{"name": "John", "age"": 30, "city": "New York"}'
# print(insertSchema("nofrills.com2", "kevin223", testschema))
#getSchemaByWebsiteAndUser("nofrills.com", "kevin")




