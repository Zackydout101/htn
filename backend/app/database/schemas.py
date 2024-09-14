from supabase import create_client, Client
import json
import constants, query_constants

url: str = constants.SUPABASE_URL
key: str = constants.SUPABASE_KEY

supabase: Client = create_client(url, key)

def getSchemaByWebsiteAndUser(website_url:str, user_id:str) -> dict:
  response = supabase.table(query_constants.RESPONSE_SCHEMA_TABLE).select("*").eq(query_constants.WEBSITE_URL_COLUMN, website_url).eq(query_constants.USER_ID_COLUMN, user_id).execute()
  json = response.data[0][query_constants.RESPONSE_SCHEMA_COLUMN]
  print(json["cheese"])
  return json

def insertSchema(website_url:str, user_id:str, schema_string:str) -> bool:
  try:
    schema = json.loads(schema_string)
    response = supabase.table(query_constants.RESPONSE_SCHEMA_TABLE).insert({query_constants.WEBSITE_URL_COLUMN:website_url, query_constants.USER_ID_COLUMN:user_id, query_constants.RESPONSE_SCHEMA_COLUMN:schema}).execute()
    print(response) 
  
  except Exception as e: 
    print(e)
    return False
  
  
  return True

testschema = '{"name": "John", "age"": 30, "city": "New York"}'
print(insertSchema("nofrills.com2", "kevin223", testschema))
#getSchemaByWebsiteAndUser("nofrills.com", "kevin")




