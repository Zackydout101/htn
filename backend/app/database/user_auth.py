from supabase import create_client, Client
from flask import Flask, request, jsonify
from run import app

import constants

url: str = constants.SUPABASE_URL
key: str = constants.SUPABASE_KEY

supabase: Client = create_client(url, key)

@app.route('/auth/signup', methods=['POST'])
def signUp():
  data = request.json  # Get the JSON data sent in the request

  try:
    data = supabase.auth.sign_up({  
      'email': data['email'],
      'password': data['password'],
      'options': {
        'email_redirect_to': "http://localhost:3000",
      },
    })
    print(data)
    return jsonify({'result': data})
  except Exception as e:
    print(e)
  return jsonify({'result': "data"})

@app.route('/auth/signin', methods=['POST'])
def signIn():
  data = request.json  # Get the JSON data sent in the request

  try:
    data = supabase.auth.sign_in_with_password({
      'email': data['email'],
      'password': data['password'],
    })
    return ""
  except Exception as e:
    print(e)
    return e

def signOut():
  try:
    supabase.auth.sign_out()
  except Exception as e:
    print(e)
