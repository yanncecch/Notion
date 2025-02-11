import requests
from datetime import datetime, date, timedelta
from notion.config import NOTION_HEADERS, DATABASE_ID

def delete_old_articles():
    notion_url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(notion_url, headers=NOTION_HEADERS)

    if response.status_code == 200:
        data = response.json()
        for page in data["results"]:
            page_id = page["id"]
            date_str = page["properties"]['Date de publication']['date']['start']
            
            # Convertir la date en objet datetime
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
            
            # Vérifier si la date est plus ancienne que 3 mois
            if date_obj < (date.today() - timedelta(days=14)):
                delete_url = f"https://api.notion.com/v1/pages/{page_id}"
                requests.patch(delete_url, headers=NOTION_HEADERS, json={"archived": True})
                print(f"🗑️ Page {page_id} archivée (publiée le {date_obj})")
    else:
        print("❌ Erreur lors de la récupération des articles :", response.text)
