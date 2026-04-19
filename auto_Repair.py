import os
import subprocess
import shutil
import ctypes

def is_admin():
    """Checks if the script is running with Administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def find_large_files(threshold_mb=500):
    """Scans the user directory for massive files."""
    print(f"\n🔎 Step 5: Scanning for files larger than {threshold_mb}MB...")
    threshold_bytes = threshold_mb * 1024 * 1024
    home_dir = os.path.expanduser("~")
    large_files_found = 0

    for root, dirs, files in os.walk(home_dir):
        for name in files:
            filepath = os.path.join(root, name)
            try:
                file_size = os.path.getsize(filepath)
                if file_size > threshold_bytes:
                    size_gb = round(file_size / (1024**3), 2)
                    print(f"📦 {size_gb}GB -> {filepath}")
                    
                    # Optional: Ask to delete
                    # choice = input("   Delete this file? (y/n): ")
                    # if choice.lower() == 'y':
                    #     os.remove(filepath)
                    #     print("   🗑️ Deleted.")
                    
                    large_files_found += 1
            except (OSError, PermissionError):
                continue
    
    if large_files_found == 0:
        print("✅ No massive files found.")
    else:
        print(f"\nTotal large files found: {large_files_found}")

def run_fix_routine():
    if not is_admin():
        print("❌ ERROR: Access Denied.")
        print("👉 Right-click VS Code or Terminal and select 'Run as Administrator'.")
        return

    print("="*60)
    print("🚀 STARTING FULL SYSTEM OPTIMIZATION & REPAIR")
    print("="*60)

    # 1. NETWORK FIX
    print("\n🌐 Step 1: Flushing DNS...")
    subprocess.run(["ipconfig", "/flushdns"], capture_output=True)
    print("✅ Network cache cleared.")

    # 2. TEMP CLEANING
    print("\n🧹 Step 2: Cleaning System Temp Files...")
    temp_paths = [os.environ.get('TEMP'), r'C:\Windows\Temp']
    for path in temp_paths:
        try:
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                try:
                    if os.path.isfile(item_path): os.unlink(item_path)
                    elif os.path.isdir(item_path): shutil.rmtree(item_path)
                except: continue
            print(f"✅ Cleaned: {path}")
        except: print(f"⚠️ Skip: {path}")

    # 3. WINDOWS REPAIR
    print("\n🔍 Step 3: Running System File Checker (SFC)...")
    print("   (This repairs Windows OS corruption)")
    try:
        subprocess.run(["sfc", "/scannow"], check=True)
        print("✅ Windows integrity check complete.")
    except Exception as e:
        print(f"⚠️ SFC could not run: {e}")

    # 4. DRIVE OPTIMIZATION
    print("\n💽 Step 4: Optimizing C: Drive...")
    subprocess.run(["defrag", "C:", "/O"], capture_output=True)
    print("✅ Disk optimization complete.")

    # 5. LARGE FILE SCAN (The new addition)
    confirm = input("\n❓ Do you want to scan for large files (>500MB)? (y/n): ")
    if confirm.lower() == 'y':
        find_large_files(threshold_mb=500)

    print("\n" + "="*60)
    print("✨ MAINTENANCE COMPLETE! Your PC is now in top shape.")
    print("="*60)

if __name__ == "__main__":
    run_fix_routine()