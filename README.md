# 🚀 Notion Article Bot - Automatisation de veille Tech
Ce projet permet d'automatiser la récupération d'articles DevOps depuis Dev.to et de les ajouter dans Notion, avec une suppression automatique après un certain temps. Il s'exécute automatiquement via GitLab CI/CD.

## 📌 Fonctionnalités
✅ Récupération automatique des articles DevOps depuis Dev.to via API
✅ Ajout des articles dans une base de données Notion via l’API Notion
✅ Suppression automatique des articles après X jours pour éviter l’encombrement
✅ Automatisation avec GitLab CI/CD

## 📂 Structure du projet

```bash
notion_project/
├── notion/                # 📂 Contient les scripts liés à Notion
│   ├── __init__.py        # 📌 Initialise le module Notion
│   ├── config.py          # 📌 Gère les clés API et les headers
│   ├── add_article_to_notion.py  # 📌 Ajoute les articles dans Notion
│   ├── delete_old_articles.py    # 📌 Supprime les articles trop anciens
│   ├── get_existing_articles.py  # 📌 Vérifie les articles existants
│   ├── update_article_in_notion.py  # 📌 Met à jour un article dans Notion
├── .gitignore             # 📌 Liste des fichiers à ignorer dans Git
├── .env.example           # 📌 Exemple de fichier .env à remplir
├── requirements.txt       # 📌 Liste des dépendances Python
├── README.md              # 📌 Documentation du projet
├── main.py                # 📌 Script principal
```

## 🔧 Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/yanncecch/notion-article-bot.git
cd notion-article-bot
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Configurer les clés API
```bash
touch .env
```

Ajoute les clés API et l’ID de la base Notion :

```ini
NOTION_API_KEY=ta_cle_notion
DATABASE_ID=ton_database_id
DEVTO_API_KEY=ta_cle_devto
```

## 🚀 Utilisation

### 1. Lancer le script manuellement

Pour récupérer et ajouter les articles dans Notion :

```bash
python main.py
```

### 2. Automatiser avec GitLab CI/CD
Ajoute ce fichier .gitlab-ci.yml pour exécuter le script tous les jours :

```yaml
schedule:
  - cron: "0 6 * * *"
    script:
      - python main.py
```

Cela exécutera main.py tous les jours à 6h du matin.

## 📦 Technologies utilisées
🔹 Python
🔹 API Notion
🔹 API Dev.to
🔹 GitLab CI/CD

## 🛠 Améliorations possibles
🔹 Ajouter d’autres sources d’articles (Medium, Hashnode...).
🔹 Intégrer des notifications Slack/Telegram.
🔹 Améliorer l’affichage dans Notion avec des catégories et filtres.

## 📩 Contribuer
Tu veux améliorer ce projet ? Clone-le, fais tes modifications et propose une pull request !

## 📄 Licence
Ce projet est sous licence MIT – libre à utiliser et modifier.