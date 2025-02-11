import requests
from notion.config import NOTION_HEADERS, DATABASE_ID

def update_article_in_notion(page_id, title, url, date, author, tags, cover_image):
    notion_url = f"https://api.notion.com/v1/pages/{page_id}"

    payload = {
        "cover": {"external": {"url": cover_image}},  # ✅ Ajout de l'image de couverture
        "properties": {
            "Titre": {"title": [{"text": {"content": title}}]},
            "URL": {"url": url},
            "Date de publication": {"date": {"start": date}},
            "Auteur": {"rich_text": [{"text": {"content": author}}]},
            "Tags": {"rich_text": [{"text": {"content": tags}}]}
        }
    }

    response = requests.patch(notion_url, headers=NOTION_HEADERS, json=payload)

    if response.status_code == 200:
        print(f"✅ Article mis à jour avec image : {title}")
    else:
        print(f"❌ Erreur lors de la mise à jour : {title}, {response.text}")
