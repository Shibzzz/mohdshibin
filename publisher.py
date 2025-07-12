import requests
import os
from dotenv import load_dotenv

load_dotenv()

def post_to_medium(title, content):
    token = os.getenv("MEDIUM_INTEGRATION_TOKEN")
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    user_resp = requests.get("https://api.medium.com/v1/me", headers=headers)
    user_id = user_resp.json()["data"]["id"]

    post_url = f"https://api.medium.com/v1/users/{user_id}/posts"
    payload = {
        "title": title,
        "contentFormat": "html",
        "content": f"<p>{content}</p>",
        "publishStatus": "public"
    }

    response = requests.post(post_url, headers=headers, json=payload)
    return response.json()
