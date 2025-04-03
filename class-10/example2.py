# conditional statements
# loops

import os

folders = input("Enter a list of folder paths seperated by spaces: ").split()

for folder in folders:
    if os.path.exists(folder):
      files = os.listdir(folder)
      if files:
        print(f"Files in {folder}:")
        for file in files:
          print(f"- {file}")

      else:
        print(f"No files found in {folder}")      

    else:
      print(f"Folder is not valid")        
