import requests
from notion.config import NOTION_HEADERS, DATABASE_ID

def add_article_to_notion(title, url, date, author, tags, cover_image):
    notion_url = "https://api.notion.com/v1/pages"

    payload = {
        "parent": {"database_id": DATABASE_ID},
        "cover": {"external": {"url": cover_image}},
        "properties": {
            "Titre": {"title": [{"text": {"content": title}}]},
            "URL": {"url": url},
            "Date de publication": {"date": {"start": date}},
            "Auteur": {"rich_text": [{"text": {"content": author}}]},
            "Tags": {"rich_text": [{"text": {"content": tags}}]}
        }
    }

    response = requests.post(notion_url, headers=NOTION_HEADERS, json=payload)

    if response.status_code == 200:
        print(f" Article modifié : {title}")
    else:
        print(f" Erreur lors de la modification : {title}, {response.text}")


        