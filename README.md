# 🗄️ Task 2 – Backup & Restore System

This project demonstrates a simple database backup and restore system using Python and SQLite.

## 📂 Files
- `sampledb.py` – Creates a sample database with data.
- `backup.py` – Creates timestamped backups of the database.
- `restore.py` – Restores the latest backup.

## ⚙️ Usage
1. Run `python sampledb.py` → creates `app.db`
2. Run `python backup.py` → creates backup in `/backups`
3. Run `python restore.py` → restores the most recent backup

📝 Note: The database and backup files are generated automatically when you run the scripts.
