from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will allow all origins by default

# Import routes after creating the app
from app.routes import scraper_routes
from app.database import page_data, schemas, user_auth, api_endpoints

# This ensures that the routes are registered
scraper_routes
page_data
schemas
user_auth
api_endpoints
