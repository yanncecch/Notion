from datetime import datetime, timedelta, date
import os
from dotenv import load_dotenv

# Charger les variables du fichier .env
load_dotenv()

# Récupérer les valeurs des clés API
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
DATABASE_ID = os.getenv("DATABASE_ID")
DEVTO_API_KEY = os.getenv("DEVTO_API_KEY")

# Autres constantes
DEVTO_URL = "https://dev.to/api/articles?tag=devops&per_page=12"

# Headers Notion
NOTION_HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

DEVTO_HEADERS = {
    "api-key": DEVTO_API_KEY
}