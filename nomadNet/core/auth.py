from functools import wraps
from aiohttp import web
import jwt
from jwt import PyJWKClient
from config.settings import AUTH0_DOMAIN, AUTH0_API_AUDIENCE, AUTH0_ALGORITHMS

jwks_client = PyJWKClient(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')

def get_signing_key(token):
    try:
        signing_key = jwks_client.get_signing_key_from_jwt(token)
        return signing_key.key
    except jwt.exceptions.PyJWKClientError as error:
        print(f"Error retrieving signing key: {error}")
        return None

async def validate_token(token):
    try:
        signing_key = get_signing_key(token)
        if not signing_key:
            return None

        payload = jwt.decode(
            token,
            signing_key,
            algorithms=AUTH0_ALGORITHMS,
            audience=AUTH0_API_AUDIENCE,
            issuer=f'https://{AUTH0_DOMAIN}/'
        )
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.JWTClaimsError:
        return None
    except jwt.InvalidTokenError:
        return None

@web.middleware
async def auth_middleware(request, handler):
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return web.json_response({'error': 'Missing Authorization header'}, status=401)

    parts = auth_header.split()
    if parts[0].lower() != 'bearer':
        return web.json_response({'error': 'Invalid authentication scheme'}, status=401)
    token = parts[1]

    payload = await validate_token(token)
    if not payload:
        return web.json_response({'error': 'Invalid or expired token'}, status=401)

    request['user'] = payload
    return await handler(request)

def authenticate(f):
    @wraps(f)
    async def decorated(request, *args, **kwargs):
        if 'user' not in request:
            return web.json_response({'error': 'Authentication required'}, status=401)
        return await f(request, *args, **kwargs)
    return decorated