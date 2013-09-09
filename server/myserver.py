from datetime import datetime as dt
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello %s' % dt.now()

if __name__ == '__main__':
    app.run()

