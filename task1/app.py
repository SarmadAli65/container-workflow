import os
from flask import Flask
import redis

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port)


@app.route('/')
def hello_world():
    return f'Hello and welcome'

@app.route('/count')
def index():
    counter = r.incr('counter')
    return f'Page visited {counter} times'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)