from flask import Flask, render_template, redirect, request, session
from config import AUTH_URL, SCOPES
from DiscordAPI import exchange_code, get_user, revoke_token
from utils import check_api_access

app = Flask(__name__)


@app.route('/')
def home():
    if check_api_access():
        user = get_user(session.get('access_token'))
        return render_template('index.html', user=user)
    return render_template('index.html', auth_url=AUTH_URL)


@app.route('/profile')
def profile():
    if check_api_access():
        user = get_user(session.get('access_token'))
        return render_template('profile.html', user=user)
    return redirect('/')


@app.route('/api/auth')
def auth():
    code = request.args.get('code')
    oauth2 = exchange_code(code)
    if code is not None and oauth2 is not None and oauth2.compareScopes(SCOPES):
        session['access_token'] = oauth2.access_token
    return redirect('/')


@app.route('/api/logout')
def logout():
    if check_api_access():
        revoke_token(session.get('access_token'))
    session.pop('access_token')
    return redirect('/')
