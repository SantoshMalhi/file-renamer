import os

def rename_files(directory, prefix):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    # Get all files in the specified directory
    files = os.listdir(directory)

    # Check if there are files in the directory
    if not files:
        print(f"No files found in the directory '{directory}'.")
        return

    # Initialize a counter for numbering the files
    counter = 1

    # Loop through each file and rename it
    for filename in files:
        # Skip directories
        if os.path.isdir(os.path.join(directory, filename)):
            continue

        # Create the new file name with a number and the same file extension
        file_extension = os.path.splitext(filename)[1]
        new_name = f"{prefix}_{counter}{file_extension}"

        # Create the full paths for the old and new file names
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)

        # Rename the file
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")
        except Exception as e:
            print(f"Error renaming {filename}: {e}")

        # Increment the counter for the next file
        counter += 1

# Example usageimport os

def rename_folder(directory, old_name, new_name):
    # Construct the full path for the old and new folder names
    old_folder_path = os.path.join(directory, old_name)
    new_folder_path = os.path.join(directory, new_name)

    # Check if the old folder exists
    if not os.path.exists(old_folder_path):
        print(f"Error: The folder '{old_name}' does not exist in '{directory}'.")
        return

    # Check if the new folder already exists
    if os.path.exists(new_folder_path):
        print(f"Error: The folder '{new_name}' already exists in '{directory}'.")
        return

    # Rename the folder
    try:
        os.rename(old_folder_path, new_folder_path)
        print(f"Renamed folder: {old_name} -> {new_name}")
    except Exception as e:
        print(f"Error renaming folder: {e}")

# Example usage
directory = r"C:\Users\malhi\OneDrive\Desktop\file-renamer\Folders"  # Directory containing the folder
old_name = "New santosh"  # Current name of the folder
new_name = "Changed New santosh"  # New name for the folder

rename_folder(directory, old_name, new_name)

directory = r"C:\Users\malhi\OneDrive\Desktop\file-renamer\Folders\New santosh"  # Use raw string notation
prefix = "New_folder"  # Prefix for the new file names

rename_files(directory, prefix)
