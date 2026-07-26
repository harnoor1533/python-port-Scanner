import socket
import time

# Get target IP
target = input("Enter IP Address: ")

# Validate IP address
try:
    socket.inet_aton(target)
except socket.error:
    print("Invalid IP Address!")
    exit()

# Get port range
start_port = int(input("Enter Start Port: "))
end_port = int(input("Enter End Port: "))

print(f"\nScanning {target}...\n")

start_time = time.time()

open_ports = []

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"

        print(f"Port {port} is OPEN ({service})")
        open_ports.append(port)

    s.close()

end_time = time.time()

print("\n---------- Scan Complete ----------")
print(f"Total Open Ports: {len(open_ports)}")
print(f"Time Taken: {end_time - start_time:.2f} seconds")
