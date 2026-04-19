import psutil
import platform
from datetime import datetime
import os

def get_size(bytes, suffix="B"):
    """Scales bytes to readable format (e.g., GB)"""
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def run_health_check():
    print("="*20, "💻 SYSTEM HEALTH CHECK", "="*20)
    
    # 1. CPU Health
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count(logical=True)
    print(f"🧠 CPU Usage: {cpu_usage}% ({cpu_count} Cores)")
    if cpu_usage > 80:
        print("   ⚠️ WARNING: CPU usage is high!")

    # 2. RAM (Memory) Health
    svmem = psutil.virtual_memory()
    print(f"💾 RAM: {get_size(svmem.used)} used of {get_size(svmem.total)} ({svmem.percent}%)")
    if svmem.percent > 85:
        print("   ⚠️ WARNING: Low memory available!")

    # 3. Disk Health (Storage)
    disk = psutil.disk_usage('/')
    print(f"💽 Disk: {get_size(disk.used)} used of {get_size(disk.total)} ({disk.percent}%)")
    if disk.percent > 90:
        print("   ⚠️ WARNING: Disk is nearly full!")

    # 4. Battery Health
    battery = psutil.sensors_battery()
    if battery:
        plugged = "Plugged In" if battery.power_plugged else "Running on Battery"
        print(f"🔋 Battery: {battery.percent}% ({plugged})")
    
    # 5. Network Check
    net_io = psutil.net_io_counters()
    print(f"🌐 Network: Sent {get_size(net_io.bytes_sent)}, Received {get_size(net_io.bytes_recv)}")

    print("="*62)

if __name__ == "__main__":
    run_health_check()