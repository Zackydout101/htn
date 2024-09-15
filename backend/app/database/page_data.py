from supabase import create_client, Client
from app.database import constants, query_constants
from typing import List
from app import app
from flask import request, Response, jsonify
from app.database.user_auth import supabase


def get_page_data_by_website(website_url: str, user_id: str) -> str:
    response = supabase.table(query_constants.PAGE_DATA_TABLE).select("*").eq(query_constants.WEBSITE_URL_COLUMN, website_url).eq(query_constants.USER_ID_COLUMN, user_id).execute()
    if response.data:
        return response.data[0][query_constants.PAGE_DATA_COLUMN]
    return None

def insert_page_data(website_url: str, user_id: str, page_data: str) -> bool:
    try:
        response = supabase.table(query_constants.PAGE_DATA_TABLE).insert({
            query_constants.WEBSITE_URL_COLUMN: website_url,
            query_constants.PAGE_DATA_COLUMN: page_data,
            query_constants.USER_ID_COLUMN: user_id
        }).execute()
        return True
    except Exception as e:
        print(e)
        return False

def get_page_data_for_user(user_id: str) -> dict:
    response = supabase.table(query_constants.PAGE_DATA_TABLE).select("*").eq(query_constants.USER_ID_COLUMN, user_id).execute()
    page_data = {}
    for data in response.data:
        page_data[data[query_constants.WEBSITE_URL_COLUMN]] = data[query_constants.PAGE_DATA_COLUMN]
    return page_data

@app.route('/data/website', methods=['POST'])
def get_page_data_by_website_route():
    data = request.json
    website_url = data["website_url"]
    user_id = supabase.auth.get_user().user.id
    result = get_page_data_by_website(website_url, user_id)
    if result:
        return jsonify(result)
    return jsonify({"error": "No data found"}), 404

@app.route('/data/insert', methods=['POST'])
def insert_page_data_route():
    data = request.json
    website_url = data["website_url"]
    user_id = supabase.auth.get_user().user.id
    page_data = data["page_data"]
    if insert_page_data(website_url, user_id, page_data):
        return Response("Success", status=200)
    return Response("Database error", status=400)

@app.route('/data/user', methods=['GET'])
def get_page_data_for_user_route():
    try:
        user_id = supabase.auth.get_user().user.id
        page_data = get_page_data_for_user(user_id)
        return jsonify(page_data)
    except Exception as e:
        print(e)
        return Response("Database error", status=400)

# insertPageData("walmart.com", "kevin", "new data")
# insertPageData("bestbuy.com", "kevin", "new data")
# getPageDataForUser("kevin")