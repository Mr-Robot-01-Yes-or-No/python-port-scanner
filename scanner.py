import socket

# Common ports with service names
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    8080: "HTTP-Alt"
}

target = input("Enter target IP or domain: ")

print(f"\nScanning target: {target}\n")

try:
    for port, service in common_ports.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port} → {service}")

        s.close()

except socket.gaierror:
    print("❌ Invalid target. Please enter a valid IP or domain.")

except KeyboardInterrupt:
    print("\nScan stopped by user.")

print("\nScan completed.")