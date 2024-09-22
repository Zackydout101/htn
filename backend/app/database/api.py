from supabase import create_client, Client
from app.database import constants, query_constants
from typing import List
from app import app
from flask import Flask, request, Response
from app.database.user_auth import supabase


@app.route('/apis/api', methods=['POST'])
def getAPI() -> str:
  data = request.json  # Get the JSON data sent in the request
  api_name = data["api_name"]
  user_id = supabase.auth.get_user().user.id
  response = supabase.table(query_constants.API_ENDPOINTS_TABLE).select("*").eq(query_constants.API_NAME_COLUMN, api_name).eq(query_constants.USER_ID_COLUMN, user_id).execute()
  if response.data:
      return response.data[0][query_constants.API_JSON_COLUMN]
  return None

@app.route('/apis/user', methods=['GET'])
def getAPIsForUser() -> List[str]:
  try:
    user_id = supabase.auth.get_user().user.id
    response = supabase.table(query_constants.API_ENDPOINTS_TABLE).select("*").eq(query_constants.USER_ID_COLUMN, user_id).execute()
    pageData = []
    print(response.data[0].keys(), flush=True)
    print(response.data[0]["website_url"], flush=True)
    for data in response.data:
      pageData.append([data["website_url"], str(data["json_schema"]), data["api_endpoint"]])
    res = dict()
    res["data"] = pageData

    return res
  except Exception as e:
    print(e)
    return Response(
        "database error",
        status=400,
    )

@app.route('/apis/insert', methods=['POST'])
def insertGeneratedAPI() -> bool:
  data = request.json  # Get the JSON data sent in the request
  user_id = supabase.auth.get_user().user.id
  api_name = data["api_name"]
  json_data = data["json_data"]
  try:
    response = supabase.table(query_constants.API_ENDPOINTS_TABLE).insert({query_constants.API_NAME_COLUMN:api_name, query_constants.API_JSON_COLUMN: json_data, query_constants.USER_ID_COLUMN:user_id}).execute()
    return Response("Success", status=200)
  except Exception as e:
    print(e)
    return Response("Database error", status=400)

# insertPageData("walmart.com", "kevin", "new data")
# insertPageData("bestbuy.com", "kevin", "new data")
# getPageDataForUser("kevin")