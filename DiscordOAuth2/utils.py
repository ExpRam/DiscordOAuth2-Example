from flask import redirect, session
from DiscordAPI import get_user


def check_api_access() -> bool:
    if get_user(session.get('access_token')) is None:
        redirect('/api/logout')
        return False
    return True
