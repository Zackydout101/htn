from supabase import create_client, Client
import constants, query_constants
from typing import List
from run import app
from flask import Flask, request, jsonify

url: str = constants.SUPABASE_URL
key: str = constants.SUPABASE_KEY

supabase: Client = create_client(url, key)

@app.route('/data/website', methods=['GET'])
def getPageDataByWebsite() -> str:
  data = request.json  # Get the JSON data sent in the request
  website_url = data["website_url"]
  user_id = data["user_id"]
  response = supabase.table(query_constants.PAGE_DATA_TABLE).select("*").eq(query_constants.WEBSITE_URL_COLUMN, website_url).eq(query_constants.USER_ID_COLUMN, user_id).execute()
  print(response)
  pageData = response[0][query_constants.PAGE_DATA_COLUMN]
  return pageData

@app.route('/data/user', methods=['GET'])
def getPageDataForUser() -> List[str]:
  data = request.json  # Get the JSON data sent in the request
  user_id = data["user_id"]
  response = supabase.table(query_constants.PAGE_DATA_TABLE).select("*").eq("user_id", user_id).execute()
  pageData = []

  for data in response.data:
    pageData.append([data[query_constants.WEBSITE_URL_COLUMN], data[query_constants.PAGE_DATA_COLUMN]])
  print(pageData)

  return pageData

@app.route('/data/insert', methods=['POST'])
def insertPageData() -> bool:
  data = request.json  # Get the JSON data sent in the request
  website_url = data["website_url"]
  user_id = data["user_id"]
  page_data = data["page_data"]
  try:
    response = supabase.table(query_constants.PAGE_DATA_TABLE).insert({query_constants.WEBSITE_URL_COLUMN:website_url, query_constants.PAGE_DATA_COLUMN: page_data, query_constants.USER_ID_COLUMN:user_id}).execute()
    print(response)
  except Exception as e:
    print(e)
    return False
  return True

# insertPageData("walmart.com", "kevin", "new data")
# insertPageData("bestbuy.com", "kevin", "new data")
# getPageDataForUser("kevin")