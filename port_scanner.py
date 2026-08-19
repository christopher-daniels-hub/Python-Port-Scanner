import socket

target = "10.11.16.21"

print("Scanning Windows Server:", target)

for port in range(1, 1025):
    scanner = socket. socket(socket.AF_INET, socket. SOCK_STREAM)
    scanner.settimeout(0.2)

    result = scanner.connect_ex((target, port))

    if result = 0:
        print("Open port:", port)

    scanner.close()

print("Scan complete.")