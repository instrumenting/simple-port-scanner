import socket
import sys
import time

def scan_port(host, port):
    # Try to connect. If it works, the port is open.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # don't wait forever on closed ports
    result = s.connect_ex((host, port))  # 0 means success
    s.close()
    return result == 0

def main():
    if len(sys.argv) != 4:
        print("Usage: python scanner.py <host> <start_port> <end_port>")
        sys.exit(1)

    host = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])

    print(f"Scanning {host} from port {start} to {end}...")
    t0 = time.time()  # start the clock before the loop
    for port in range(start, end + 1):
        if scan_port(host, port):
            print(f"Port {port} is open")

    elapsed = time.time() - t0  # end time minus start time
    print(f"Done. Scanned {end - start + 1} ports in {elapsed:.2f} seconds.")

if __name__ == "__main__":
    main()
