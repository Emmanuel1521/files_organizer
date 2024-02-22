import os
import shutil
import pyautogui

def organize_files(source_folder, destination_folder):
    # Create destination folders if they don't exist
    for folder_name in ["Documents", "Images", "Videos", "Others"]:
        folder_path = os.path.join(destination_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    # Get a list of all files in the source folder
    files = os.listdir(source_folder)

    # Loop through each file and move it to the appropriate folder based on its extension
    for file in files:
        if os.path.isfile(os.path.join(source_folder, file)):
            file_extension = os.path.splitext(file)[1][1:].lower()  # Get the file extension
            if file_extension in ["doc", "docx", "txt", "pdf"]:
                shutil.move(os.path.join(source_folder, file), os.path.join(destination_folder, "Documents", file))
            elif file_extension in ["jpg", "jpeg", "png", "gif"]:
                shutil.move(os.path.join(source_folder, file), os.path.join(destination_folder, "Images", file))
            elif file_extension in ["mp4", "avi", "mov", "wmv"]:
                shutil.move(os.path.join(source_folder, file), os.path.join(destination_folder, "Videos", file))
            else:
                shutil.move(os.path.join(source_folder, file), os.path.join(destination_folder, "Others", file))

def main():
    source_folder = r"C:\Users\gepre\Downloads\source"  # Please replace the placeholder with the directory where the documents are located, as this directory will be used to organize the files.
    destination_folder = r"C:\Users\gepre\Downloads\destination"  # Please replace the placeholder with the directory where files will be organized

    # Organize files
    organize_files(source_folder, destination_folder)

    # Notify the user that the task is completed
    pyautogui.alert("File organization completed!")

if __name__ == "__main__":
    main()
