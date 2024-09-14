from flask import Flask, request, abort
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # This will allow all origins by default


# import declared routes
import page_data
import schemas
import user_auth
