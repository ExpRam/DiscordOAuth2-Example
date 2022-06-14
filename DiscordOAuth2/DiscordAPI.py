from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, API_ENDPOINT, DISCORD_CDN
from requests import post, get, HTTPError
from typing import NoReturn, Union


class OAuth2:

    def __init__(self, json: dict) -> NoReturn:
        self.access_token = json.get('access_token')
        self.expires_in = json.get("expires_in")
        self.refresh_token = json.get('refresh_token')
        self.scope = str(json.get('scope')).split(" ")
        self.token_type = json.get('token_type')

    def compareScopes(self, scopes: list) -> bool:
        return set(self.scope) == set(scopes)


class User:

    def __init__(self, json: dict) -> NoReturn:
        self.id = json.get('id')
        self.username = json.get('username')
        self.avatar = json.get('avatar')
        self.avatar_decoration = json.get('avatar_decoration')
        self.discriminator = json.get('discriminator')
        self.public_flags = json.get('public_flags')
        self.flags = json.get('flags')
        self.banner = json.get('banner')
        self.banner_color = json.get('banner_color')
        self.accent_color = json.get('accent_color')
        self.locale = json.get('locale')
        self.mfa_enabled = json.get('mfa_enabled')
        self.email = json.get('email')
        self.verified = json.get('verified')

    def get_avatar_url(self) -> Union[str, None]:
        return f"{DISCORD_CDN}/avatars/{self.id}/{self.avatar}" if self.avatar is not None else None


def exchange_code(code: str) -> Union[OAuth2, None]:
    try:
        data = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        r = post(f'{API_ENDPOINT}/oauth2/token', data=data, headers=headers)
        r.raise_for_status()
        return OAuth2(r.json())
    except HTTPError:
        return None


def get_user(access_token: str, token_type: str = "Bearer") -> Union[User, None]:
    headers = {
        'Authorization': f'{token_type} {access_token}'
    }
    try:

        r = get(f"{API_ENDPOINT}/users/@me", headers=headers)
        r.raise_for_status()
        return User(r.json())
    except HTTPError:
        return None


def revoke_token(access_token: str) -> NoReturn:
    try:
        data = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'token': access_token
        }

        r = post("https://discord.com/api/oauth2/token/revoke", data=data)
        r.raise_for_status()
    except HTTPError:
        return None
