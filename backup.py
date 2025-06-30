# backup_once.py
import os, shutil
from datetime import datetime

source = r"C:\Users\Richie\Documents"
dest = r"D:\adope\backup"

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
target = os.path.join(dest, f"backup_{timestamp}")
os.makedirs(target, exist_ok=True)

for file in os.listdir(source):
    src_file = os.path.join(source, file)
    if os.path.isfile(src_file):
        shutil.copy2(src_file, target)

print("✅ One-time backup complete.")
