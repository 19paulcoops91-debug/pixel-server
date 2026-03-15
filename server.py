from flask import Flask, send_file, request
import datetime
import os

app = Flask(__name__)

LOG_FILE = "log.txt"

@app.route("/pixel")
def pixel():
    # Get real client IP (Render passes it in X-Forwarded-For)
    ip = (
    request.headers.get("True-Client-Ip")
    or request.headers.get("Cf-Connecting-Ip")
    or request.headers.get("X-Forwarded-For", "").split(",")[0].strip()
    or request.remote_addr
)
    ua = request.headers.get("User-Agent")

    # Log request details
    with open(LOG_FILE, "a") as f:
        f.write(
            f"{datetime.datetime.now()} | "
            f"IP: {ip} | "
            f"UA: {ua}\n"
        )

    # Serve the transparent PNG
    return send_file("transparent.png", mimetype="image/png")

# 👉 ADD THIS NEW ROUTE HERE
@app.route("/debug")
def debug():
    return dict(request.headers)

@app.route("/")
def home():
    return "Pixel server is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
