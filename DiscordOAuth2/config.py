from urllib import parse

# https://discord.com/developers/applications
CLIENT_ID = ''
CLIENT_SECRET = ''
TOKEN = ''

SCOPES = ['identify', 'email']
PORT = 5000
REDIRECT_URI = f'http://localhost:{PORT}/api/auth'
API_ENDPOINT = 'https://discord.com/api/v10'
DISCORD_CDN = 'https://cdn.discordapp.com'

AUTH_URL = f'https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri={parse.quote(REDIRECT_URI)}' \
           f'&response_type=code&scope=' + " ".join([str(i) for i in SCOPES])
