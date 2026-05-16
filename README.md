# 🚀 Neo-DDOS - Multi-Vector Network Stress Testing Tool

**[!] ADVANCED NETWORK STRESS TESTING TOOL FOR AUTHORIZED SECURITY RESEARCH**

![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)
![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)
![Platform: Windows/Linux/MacOS/Termux](https://img.shields.io/badge/platform-All-lightgrey.svg)

---

## ⚠️ **LEGAL DISCLAIMER**
**THIS TOOL IS FOR AUTHORIZED SECURITY TESTING AND EDUCATIONAL PURPOSES ONLY.**
Unauthorized use against systems you do not own is **ILLEGAL** and punishable by law.
**The author is not responsible for any misuse of this tool.**

---

## 🌟 Features
✅ **13 Attack Vectors** (UDP, TCP SYN, HTTP GET/POST, Slowloris, ICMP, DNS, NTP, Memcached, SSL Renegotiation, HTTP Slow Body, Ping of Death, ARP Spoof)
✅ **Multi-threaded Architecture** (Supports up to 10,000 threads)
✅ **Real-time Statistics** (Packets/second, errors, connections)
✅ **One-Click Execution** (Simple CLI interface)
✅ **Cross-Platform** (Windows, Linux, MacOS, Termux)
✅ **Configurable Settings** (via `config/settings.json`)

---

## 📥 Installation

### **1. Clone the Repository**
```bash
git clone https://github.com/cameleonnbss/Neo-DDOS-
cd Neo-DDOS-
```

### **2. Install Dependencies**
#### **For Windows/Linux/MacOS:**
```bash
pip install -r config/requirements.txt
```
*(For Windows users: Run as **Administrator** if you encounter permission errors.)*

#### **For Termux (Android):**
```bash
pkg update && pkg upgrade
pkg install python
pkg install git
git clone https://github.com/cameleonnbss/Neo-DDOS-
cd Neo-DDOS-
pip install -r config/requirements.txt
```
*(Note: Some features like **Scapy** or **ARP Spoof** may not work on Termux due to limitations.)*

---

## 🎯 Usage
1. **Run the script**:
   ```bash
   python main.py
   ```
   *(Or `python3 main.py` if Python 2 is your default.)*

2. **Follow the prompts**:
   - Enter the **target IP or URL** (e.g., `127.0.0.1` or `http://example.com`).
   - Specify the **port** (default: `80`).
   - Set the **duration** (in seconds, default: `10`).
   - Set the **thread count** (default: `100`).
   - Choose an **attack method** (or select `14` for **Apocalypse Mode**).

---

## 🔥 Attack Vectors
| **ID** | **Vector**               | **Protocol** | **Amplification** | **Description**                          |
|--------|--------------------------|--------------|-------------------|------------------------------------------|
| 1      | UDP Flood                | UDP          | ❌ No             | Floods target with UDP packets.          |
| 2      | TCP SYN Flood            | TCP          | ❌ No             | Sends SYN packets without ACK.          |
| 3      | HTTP GET Flood           | HTTP         | ❌ No             | Massive GET requests.                   |
| 4      | HTTP POST Flood          | HTTP         | ❌ No             | POST requests with large payloads.      |
| 5      | Slowloris                | TCP          | ❌ No             | Keeps connections open with partial headers. |
| 6      | ICMP Flood               | ICMP         | ❌ No             | Ping flood with large packets.          |
| 7      | DNS Amplification        | UDP          | ✅ **28-54x**     | Uses DNS servers to amplify traffic.    |
| 8      | NTP Amplification        | UDP          | ✅ **556x**       | Abuses NTP servers for amplification.    |
| 9      | Memcached Amplification | UDP          | ✅ **10,000x**    | Exploits Memcached servers.             |
| 10     | SSL Renegotiation        | SSL/TLS      | ❌ No             | Exhausts CPU with SSL handshakes.        |
| 11     | HTTP Slow Body           | HTTP         | ❌ No             | Sends HTTP body byte-by-byte.           |
| 12     | Ping of Death            | ICMP         | ❌ No             | Sends oversized ICMP packets.            |
| 13     | ARP Spoof                | ARP          | ❌ No             | Spoofs ARP requests (local network).     |
| **14** | **ALL ATTACKS**          | **ALL**      | **✅ MAX**         | **Apocalypse Mode (All vectors at once)** |

---

## 📊 Performance
- **100 threads** ≈ **50,000 packets/second** (varies by system).
- **Max threads**: 10,000 (adjust in `config/settings.json`).
- **Memory usage**: ~200MB at peak.

---

## 🛠️ Troubleshooting

### **ModuleNotFoundError: No module named 'dns'**
```bash
pip install dnspython
```

### **ModuleNotFoundError: No module named 'scapy'**
```bash
pip install scapy
```
*(Note: On **Windows**, install **Npcap** from [npcap.com](https://npcap.com/). On **Linux/Mac**, Scapy works natively.)*

### **Permission Denied (Linux/Mac)**
```bash
sudo python main.py
```

### **Windows Defender Blocks Execution**
1. Add an exclusion for the `Neo-DDOS` folder in **Windows Security**.
2. Or run in a **virtual machine** (recommended).

### **Scapy: Npcap not found (Windows)**
Download and install **Npcap** from [npcap.com](https://npcap.com/).
During installation, check:
- **"Support raw 802.11 traffic"**
- **"WinPcap API-compatible mode"**

### **Termux: ModuleNotFoundError**
Some modules (like `scapy`) may not work on Termux due to Android limitations.
Use **Linux/Windows/MacOS** for full functionality.

---

## 📂 Project Structure
```
Neo-DDOS/
├── main.py                 # Main script (all-in-one)
├── config/
│   ├── requirements.txt    # Dependencies
│   └── settings.json       # Configuration
├── README.md               # Documentation
├── LICENSE                 # MIT License
└── .gitignore              # Ignored files
```

---

## 🤝 Contributing
Pull requests are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

---

## 📜 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---
**[!] FOR AUTHORIZED TESTING ONLY**
**DO NOT USE THIS TOOL FOR ILLEGAL ACTIVITIES.**
```


---

