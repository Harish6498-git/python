# List the files in the folder
import os

folders = input("Enter a list of folder paths seperated by spaces: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
        if files:
            print(f"Files in {folder}: ")
            for file in files:
                print(f"- {file}")
        
        else:
            print(f"Please enter the proper file paths")
    
    except FileNotFoundError:
        print(f"\n[ERROR] Folder '{folder}' not found. Please enter a valid path.")