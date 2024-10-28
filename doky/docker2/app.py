import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

port = int(os.getenv('PORT'))

@app.route('/')
def index():
    return render_template('index.html', message='Benvenuto alla Web App!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)