import os
import shutil

def organize_my_files():
    # 1. SET YOUR PATH
    # This points to your Downloads folder. 
    # Since you are on Windows, we use 'userprofile' to find it automatically.
    downloads_path = os.path.expanduser("~/Downloads")
    
    # 2. DEFINE THE RULES
    # We map file extensions to the folder they should go into
    file_types = {
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Software": [".exe", ".msi", ".zip", ".iso"],
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Media": [".mp3", ".mp4", ".wav", ".mov"]
    }

    print(f"📁 Scanning: {downloads_path}")

    # 3. THE LOGIC ENGINE
    for filename in os.listdir(downloads_path):
        filepath = os.path.join(downloads_path, filename)
        
        # Skip if it's a folder already
        if os.path.isdir(filepath):
            continue
            
        # Get the extension (e.g., .pdf)
        file_ext = os.path.splitext(filename)[1].lower()

        for folder_name, extensions in file_types.items():
            if file_ext in extensions:
                # Create the target folder if it doesn't exist
                target_folder = os.path.join(downloads_path, folder_name)
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                
                # Move the file
                print(f"🚚 Moving {filename} -> {folder_name}")
                shutil.move(filepath, os.path.join(target_folder, filename))

    print("✨ Cleanup complete!")

if __name__ == "__main__":
    organize_my_files()