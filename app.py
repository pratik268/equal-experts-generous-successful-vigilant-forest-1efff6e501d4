from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/<username>")
def gists(username):
    url = f"https://api.github.com/users/{username}/gists"
    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        return jsonify({"error": "GitHub user not found"}), response.status_code

    data = response.json()
    result = []

    for gist in data:
        result.append({
            "id": gist["id"],
            "description": gist["description"],
            "url": gist["html_url"]
        })

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
