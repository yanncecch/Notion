import requests
from notion.config import NOTION_HEADERS, DATABASE_ID

def get_existing_articles():
    notion_url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(notion_url, headers=NOTION_HEADERS)
    

    if response.status_code == 200:
        data = response.json()
        articles = {}

        for page in data["results"]:
            page_id = page["id"]
            properties = page["properties"]
            
            title = properties["Titre"]["title"][0]["text"]["content"] if properties["Titre"]["title"] else "Sans titre"
            url = properties['URL']['url'] if properties['URL']['url'] else None  # Corrige l'affectation incorrecte
            if url:
                articles[url] = page_id  # Stocke l'ID de la page associée à l'URL
        
        return articles
    else:
        print("❌ Erreur lors de la récupération des articles Notion :", response.text)
        return {}