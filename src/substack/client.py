import requests
from src.config import settings


class SubstackClient:
    def __init__(self):
        self.base_url = f"https://{settings.substack_publication}.substack.com/api/v1"
        self.headers = {
            "Cookie": f"substack.sid={settings.substack_sid}",
            "Content-Type": "application/json",
        }

    def create_draft(self, title, subtitle, body_html):
        url = f"{self.base_url}/drafts"
        payload = {
            "draft_title": title,
            "draft_subtitle": subtitle,
            "draft_body": body_html,
            "type": "newsletter",
        }
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return {"draft_id": data.get("id"), "url": data.get("url"), "status": "success"}
