from supabase import create_client, Client
from flask import Flask, request, jsonify, Response
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
    print(supabase.auth.get_user().user.id)

    return Response(
        "success",
        status=200,
    )
  except Exception as e:
    print(e)
    return Response(
        "invalid credentials",
        status=400,
    )

@app.route('/auth/signin', methods=['POST'])
def signIn():
  data = request.json  # Get the JSON data sent in the request

  try:
    data = supabase.auth.sign_in_with_password({
      'email': data['email'],
      'password': data['password'],
    })
    print(supabase.auth.get_user())
    return Response(
        "success",
        status=200,
    )
  except Exception as e:
    print(e)
    return Response(
        "invalid credentials",
        status=400,
    )

@app.route('/auth/signout', methods=['POST'])
def signOut():
  try:
    supabase.auth.sign_out()
    return Response(
        "success",
        status=200,
    )
  except Exception as e:
    print(e)
    return Response(
        "invalid credentials",
        status=400,
    )
