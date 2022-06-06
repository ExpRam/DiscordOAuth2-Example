from routes import app
from config import PORT

app.secret_key = 'super_secret_key'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
