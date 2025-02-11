import requests
import notion
from datetime import datetime, date, timedelta
from notion.config import NOTION_HEADERS, DATABASE_ID, DEVTO_HEADERS, DEVTO_URL


response = requests.get(DEVTO_URL, headers=DEVTO_HEADERS)
if response.status_code == 200:
    articles = response.json()

    notion.delete_old_articles()
    # ✅ Récupération des articles existants
    existing_articles = notion.get_existing_articles()

    for article in articles:
        title = article["title"]
        url = article["url"]
        dates = article["published_at"].split("T")[0]
        author = article["user"]["name"]
        tags = ", ".join(article["tag_list"])
        cover_image = article.get("cover_image")  # Récupère l'image
        if not cover_image :  # Si l'image est None ou vide
            cover_image = "https://t4.ftcdn.net/jpg/03/08/69/75/360_F_308697506_9dsBYHXm9FwuW0qcEqimAEXUvzTwfzwe.jpg"
        # Image par défaut

        # ✅ Vérifier si l'article existe déjà dans Notion
        if url in existing_articles:
            page_id = existing_articles[url]
            notion.update_article_in_notion(page_id, title, url, dates, author, tags, cover_image)
        else:
            notion.add_article_to_notion(title, url, dates, author, tags, cover_image)
else:
    print("❌ Erreur lors de la récupération des articles Dev.to")

