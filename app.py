from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, db=0)

@app.get("/")
def hello():
    r.incr("visits")
    visits = r.get("visits").decode("utf-8")

    return {
        "message": "Hello, world!",
        "visits": visits
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
