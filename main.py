import os
import shutil
import pandas as pd
import time

# Define your path to your downloads folder
downloads_path = os. path.expanduser("~/Downloads") 

#File Organization
file_types = {
  'Images':['.jpg', '.jpeg', '.png', '.gif'],
   'Documents': ['.pdf', '.docx', '.txt'],
    'Spreadsheets': ['.xls', '.xlsx', '.csv'],
    'Archives': ['.zip', '.tar', '.gz'],
    'Executables': ['.exe', '.msi','.dmg']
}
# Create subfolders if they don't exist
for folder in file_types.keys():
  folder_path = os. path .join(downloads_path,folder)
  if not os. path.exists(folder_path):
        os.makedirs(folder_path)

  # Move files into subfolders based on their extension
for filename in os. listdir(downloads_path):
    file_path = os. path.join(downloads_path, filename)
    if os. path.isfile(file_path):
        file_ext = os.path.splitext(filename)[1].lower()
        for folder, extensions in file_types.items():
            if file_ext in extensions:
                shutil.move(file_path, os.path.join(downloads_path, folder, filename))
                break

   # Clean all CSV files in the Downloads folder
for filename in os. listdir(downloads_path):
    if filename.endswith('.csv'):
        clean_csv(os.path.join(downloads_path, filename))

  # System Maintenance
days_old = 30
current_time = time.time()

# Delete files older than the specified number of days
for filename in os. listdir(downloads_path):
    file_path = os. path.join(downloads_path, filename)
    if os. path.isfile(file_path):
        file_age = current_time - os. path.getmtime(file_path)
        if file_age > days_old * 86400:
            os.remove(file_path)

  # Clear temporary files
temp_path = os.path.expanduser("~/AppData/Local/Temp")
for root, dirs, files in os.walk(temp_path):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
       