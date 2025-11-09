import os
import shutil

print("🔵 Checking for backups...")

backup_folder = 'backups'

if not os.path.exists(backup_folder) or len(os.listdir(backup_folder)) == 0:
    print("⚠️ No backups found to restore.")
else:
    backups = sorted(os.listdir(backup_folder))
    latest_backup = backups[-1]
    shutil.copy(f"{backup_folder}/{latest_backup}", 'app.db')
    print(f"✅ Restored {latest_backup} → app.db")
