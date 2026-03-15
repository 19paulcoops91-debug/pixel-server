from flask import Flask, send_file, request
import datetime
import os

app = Flask(__name__)

LOG_FILE = "log.txt"

@app.route("/pixel")
def pixel():
    # Log request details
    with open(LOG_FILE, "a") as f:
        f.write(
            f"{datetime.datetime.now()} | "
            f"IP: {request.remote_addr} | "
            f"UA: {request.headers.get('User-Agent')}\n"
        )

    # Serve the transparent PNG
    return send_file("transparent.png", mimetype="image/png")

@app.route("/")
def home():
    return "Pixel server is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
