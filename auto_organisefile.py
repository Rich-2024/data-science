import os
import shutil

source_dir = r"C:\Users\Richie\Downloads"
destination_dir = r"D:\adope"

file_types = {
    "Images": ['.jpg', '.png', '.jpeg', '.gif', '.bmp'],
    "Documents": ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx'],
    "Videos": ['.mp4', '.mkv', '.mov'],
    "Music": ['.mp3', '.wav'],
    "Archives": ['.zip', '.rar', '.7z'],
    "Programs": ['.exe', '.msi'],
    "Others": []
}

def organize():
    for file_name in os.listdir(source_dir):
        full_path = os.path.join(source_dir, file_name)
        if os.path.isfile(full_path):
            ext = os.path.splitext(file_name)[1].lower()
            moved = False
            for category, extensions in file_types.items():
                if ext in extensions:
                    target_folder = os.path.join(destination_dir, category)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(full_path, os.path.join(target_folder, file_name))
                    moved = True
                    break
            if not moved:
                other_folder = os.path.join(destination_dir, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(full_path, os.path.join(other_folder, file_name))
    print("Files organized successfully.")

organize()
