from supabase import create_client, Client, auth
import constants
url: str = constants.SUPABASE_URL
key: str = constants.SUPABASE_KEY

supabase: Client = create_client(url, key)

async def signUp(email:str, password:str):
  data = await auth.sign_up({
    'email': email,
    'password': password,
    'options': {
      'email_redirect_to': "http://localhost:3000",
    },
  })
  print(data)

async def signIn(email:str, password:str):
  data = Client.auth.sign_in_with_password({
    'email': email,
    'password': password,
  })
  print(data)

async def signOut():
  await supabase.auth.signOut()

