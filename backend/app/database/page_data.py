from supabase import create_client, Client
import constants

url: str = constants.SUPABASE_URL
key: str = constants.SUPABASE_KEY

supabase: Client = create_client(url, key)

def getPageData(website_url:str):

  response = supabase.table("testPageData").select("*").eq("id", website_url).execute()
  print(response)

def insertPageData(website_url:str, page_data:str):

  response = supabase.table("testPageData").insert({"website_url":website_url, "page_data": page_data}).execute()
  print(response)

insertPageData("amazon.com", "random data")
