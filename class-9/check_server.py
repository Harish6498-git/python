import os
import time

server_ip = "18.222.122.141"  # Google's Public DNS (Use your own server IP)

while True:  # Infinite loop
    response = os.system(f"ping -c 1 {server_ip} > /dev/null 2>&1")
    if response == 0:
        print(f"Server {server_ip} is UP ✅")
        break  # Stop the loop when the server is up
    else:
        print(f"Server {server_ip} is DOWN ❌, checking again in 5 seconds...")
    time.sleep(5)  # Wait for 5 seconds before checking again
