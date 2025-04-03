# using function, loop, conditional, error handling, modularities
import os

def list_files_in_folder(folder):
  try:
    files = os.listdir(folder)
    if files:
      return files, None
    else:
      return None, "No files found in this folder."
  except FileNotFoundError:
    return None, "Folder not found"
  except PermissionError:
    return None, "Permission denied"

def main():
  folders = input("Enter a list of folder or if u have multiple folder please use spaces in between folders: ").split()

  for folder in folders:
    files, error_message = list_files_in_folder(folder)
    if files:
      print(f"Files in {folder}:")
      for file in files:
        print(f"- {file}")
    
    else:
      print(f"Error in {folder}: {error_message}")

if __name__ == "__main__":
  main()