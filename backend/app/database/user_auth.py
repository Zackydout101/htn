from supabase import create_client, Client
import constants
url: str = constants.SUPABASE_URL
key: str = constants.SUPABASE_KEY

supabase: Client = create_client(url, key)

def signUp(email:str, password:str):
  try:
    data = supabase.auth.sign_up({  
      'email': email,
      'password': password,
      'options': {
        'email_redirect_to': "http://localhost:3000",
      },
    })
    print(data)
    return True
  except Exception as e:
    print(e)
  return False

def signIn(email:str, password:str):
  try:
    data = supabase.auth.sign_in_with_password({
      'email': email,
      'password': password,
    })
  except Exception as e:
    print(e)

def signOut():
  try:
    supabase.auth.sign_out()
  except Exception as e:
    print(e)
