from supabase import create_client, Client
from . import constants, query_constants
from typing import List
from ..run import app
from flask import request, Response

url: str = constants.SUPABASE_URL
key: str = constants.SUPABASE_KEY

supabase: Client = create_client(url, key)

@app.route('/data/website', methods=['POST'])
def getPageDataByWebsite() -> str:
  data = request.json  # Get the JSON data sent in the request
  website_url = data["website_url"]
  user_id = supabase.auth.get_user().user.id
  response = supabase.table(query_constants.PAGE_DATA_TABLE).select("*").eq(query_constants.WEBSITE_URL_COLUMN, website_url).eq(query_constants.USER_ID_COLUMN, user_id).execute()
  if response.data:
      return response.data[0][query_constants.PAGE_DATA_COLUMN]
  return None

@app.route('/data/user', methods=['GET'])
def getPageDataForUser() -> List[str]:
  try:

    user_id = supabase.auth.get_user().user.id
    response = supabase.table(query_constants.PAGE_DATA_TABLE).select("*").eq(query_constants.USER_ID_COLUMN, user_id).execute()
    pageData = dict()

    for data in response.data:
      pageData[data[query_constants.WEBSITE_URL_COLUMN]] = data[query_constants.PAGE_DATA_COLUMN]
    print(pageData)
    return pageData
  except Exception as e:
    print(e)
    return Response(
        "database error",
        status=400,
    )

@app.route('/data/insert', methods=['POST'])
def insertPageData() -> bool:
  data = request.json  # Get the JSON data sent in the request
  website_url = data["website_url"]
  user_id = supabase.auth.get_user().user.id
  page_data = data["page_data"]
  try:
    response = supabase.table(query_constants.PAGE_DATA_TABLE).insert({query_constants.WEBSITE_URL_COLUMN:website_url, query_constants.PAGE_DATA_COLUMN: page_data, query_constants.USER_ID_COLUMN:user_id}).execute()
    return Response("Success", status=200)
  except Exception as e:
    print(e)
    return Response("Database error", status=400)

# insertPageData("walmart.com", "kevin", "new data")
# insertPageData("bestbuy.com", "kevin", "new data")
# getPageDataForUser("kevin")