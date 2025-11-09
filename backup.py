import os
import shutil
import datetime

print(" Creating backup...")

backup_folder = 'backups'
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)
    print(" Created backup folder")

timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
backup_file = f"{backup_folder}/backup_{timestamp}.db"

if os.path.exists('app.db'):
    shutil.copy('app.db', backup_file)
    print(f" Backup created successfully → {backup_file}")
else:
    print(" No app.db found. Run sampledb.py first.")
