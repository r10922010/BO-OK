# Bo OK!
A web site about ordering book

## How do use
### settings
1. Copy .env.example to .env and set gmail account and password
2. Open goolge lesssecureapps
3. Run `sqlite3 book.db < DBschema/schema.sql` to import sql

### run web server
```
1. pip install -r requirements.txt
2. python app.py
```

### background crawler
- You can set update time in `bgCrawling.py`
```
python bgCrawling.py
```

## Environment
1. python3