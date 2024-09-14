from supabase import create_client, Client
import constants, query_constants
from typing import List

url: str = constants.SUPABASE_URL
key: str = constants.SUPABASE_KEY

supabase: Client = create_client(url, key)

def getPageDataByWebsite(website_url:str, user_id:str) -> str:
  response = supabase.table(query_constants.PAGE_DATA_TABLE).select("*").eq(query_constants.WEBSITE_URL_COLUMN, website_url).eq(query_constants.USER_ID_COLUMN, user_id).execute()
  print(response)
  pageData = response[0][query_constants.PAGE_DATA_COLUMN]
  return pageData

def getPageDataForUser(user_id:str) -> List[str]:
  response = supabase.table(query_constants.PAGE_DATA_TABLE).select("*").eq("user_id", user_id).execute()
  pageData = []

  for data in response.data:
    pageData.append([data[query_constants.WEBSITE_URL_COLUMN], data[query_constants.PAGE_DATA_COLUMN]])
  print(pageData)

  return pageData

def insertPageData(website_url:str, user_id:str, page_data:str):
  response = supabase.table(query_constants.PAGE_DATA_TABLE).insert({query_constants.WEBSITE_URL_COLUMN:website_url, query_constants.PAGE_DATA_COLUMN: page_data, query_constants.USER_ID_COLUMN:user_id}).execute()
  print(response)

# insertPageData("walmart.com", "kevin", "new data")
# insertPageData("bestbuy.com", "kevin", "new data")
getPageDataForUser("kevin")