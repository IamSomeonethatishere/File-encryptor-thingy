import shutil
import os

print("Python File Encryptor")
print("Loading...")

# Define paths
source_path = os.path.join("Source Files")
destination_path = os.path.join("Destination")

# Make sure folders exist
os.makedirs(source_path, exist_ok=True)
os.makedirs(destination_path, exist_ok=True)

# Keep track of uploaded (moved) files/folders
files = []

while True:
    try:
        menu = int(input("1. Upload files  2. Manage uploaded files  3. Manage passwords  4. Quit: "))
        print("Redirecting...")

        if menu == 1:
            confirm = int(input("Are you sure you want to encrypt (move) all files in 'Source Files'? (1 = Yes, 2 = No): "))
            if confirm == 1:
                print("Moving files...")
                for item in os.listdir(source_path):
                    src_item = os.path.join(source_path, item)
                    dest_item = os.path.join(destination_path, item)

                    if os.path.exists(dest_item):
                        print(f"Skipping '{item}' – it already exists in Destination.")
                        continue

                    shutil.move(src_item, dest_item)
                    files.append(item)

                print("Files successfully moved.")
            else:
                print("Upload cancelled.")

        elif menu == 2:
            print(f"These are all files and folders you have uploaded (moved): {files}")

        elif menu == 3:
            print("You are unable to manage passwords at this time. Please try again later.")

        elif menu == 4:
            print("Exiting...")
            break

        else:
            print("Please enter a valid option: (1), (2), (3), or (4)")

    except ValueError:
        print("An error occurred. Please enter a number.")
