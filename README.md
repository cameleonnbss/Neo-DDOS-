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

Here's the **complete, polished, and universal installation and usage guide** for your **Neo-DDOS** tool in English, optimized for clarity and compatibility across all platforms:

---

---

## **📥 Installation Guide**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/cameleonnbss/Neo-DDOS-
cd Neo-DDOS-
```

---

### **2️⃣ Install Dependencies**

#### **🪟 Windows**
1. Install **Python 3.10+** from [python.org](https://www.python.org/downloads/).
   - **Check "Add Python to PATH"** during installation.
2. Install **Npcap** (required for Scapy):
   - Download from [npcap.com](https://npcap.com/).
   - During installation, enable:
     - ✅ **"Support raw 802.11 traffic"**
     - ✅ **"WinPcap API-compatible mode"**
3. Install Python dependencies:
   ```powershell
   pip install -r config/requirements.txt
   ```
   *(Run PowerShell as **Administrator** if you encounter permission errors.)*

---

#### **🐧 Linux (Ubuntu/Debian)**
```bash
# Update system and install Python + dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv libpcap-dev -y

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r config/requirements.txt
```

---
#### **🍎 MacOS**
```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python and dependencies
brew install python libpcap

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r config/requirements.txt
```

---
#### **📱 Termux (Android)**
```bash
# Update Termux
pkg update && pkg upgrade -y

# Install Python and Git
pkg install python git -y

# Clone and install Neo-DDOS
git clone https://github.com/cameleonnbss/Neo-DDOS-
cd Neo-DDOS-
pip install -r config/requirements.txt
```
⚠️ **Note for Termux**:
Some features (e.g., **Scapy**, **ARP Spoof**) **may not work** due to Android limitations.
For full functionality, use **Linux/Windows**.

---
#### **🪟⚠️ WSL (Windows Subsystem for Linux)**
Follow the **Linux (Ubuntu/Debian)** instructions above.
⚠️ **Note for WSL**:
- **Scapy** and **ARP Spoof** **will not work** due to WSL's network limitations.
- Use **native Windows** for these features.

---

---

## **🎯 Usage Guide**

### **1️⃣ Run the Script**
```bash
python main.py
```
*(Use `python3 main.py` if `python` defaults to Python 2.)*

---

### **2️⃣ Follow the Prompts**
The script will guide you through the following steps:

1. **Enter the target IP or URL**
   Example: `127.0.0.1` (localhost) or `http://example.com`.

2. **Specify the port**
   Default: `80` (press **Enter** to accept).

3. **Set the duration (in seconds)**
   Default: `10` (press **Enter** to accept).

4. **Set the thread count**
   Default: `100` (press **Enter** to accept).

5. **Choose an attack method**
   Select from the menu (e.g., `1` for UDP Flood, `14` for **Apocalypse Mode**).

---

### **📊 Attack Methods Menu**
| **ID** | **Attack Method**          | **Protocol** | **Amplification** | **Description**                          |
|--------|----------------------------|--------------|-------------------|------------------------------------------|
| 1      | UDP Flood                  | UDP          | ❌ No             | Floods target with UDP packets.          |
| 2      | TCP SYN Flood              | TCP          | ❌ No             | Sends SYN packets without ACK.          |
| 3      | HTTP GET Flood             | HTTP         | ❌ No             | Massive GET requests.                   |
| 4      | HTTP POST Flood            | HTTP         | ❌ No             | POST requests with large payloads.      |
| 5      | Slowloris                  | TCP          | ❌ No             | Keeps connections open with partial headers. |
| 6      | ICMP Flood                 | ICMP         | ❌ No             | Ping flood with large packets.          |
| 7      | DNS Amplification          | UDP          | ✅ **28-54x**     | Uses DNS servers to amplify traffic.    |
| 8      | NTP Amplification          | UDP          | ✅ **556x**       | Abuses NTP servers for amplification.    |
| 9      | Memcached Amplification    | UDP          | ✅ **10,000x**    | Exploits Memcached servers.             |
| 10     | SSL Renegotiation          | SSL/TLS      | ❌ No             | Exhausts CPU with SSL handshakes.        |
| 11     | HTTP Slow Body             | HTTP         | ❌ No             | Sends HTTP body byte-by-byte.           |
| 12     | Ping of Death              | ICMP         | ❌ No             | Sends oversized ICMP packets.            |
| 13     | ARP Spoof                  | ARP          | ❌ No             | Spoofs ARP requests (local network).     |
| **14** | **ALL ATTACKS**            | **ALL**      | **✅ MAX**         | **Apocalypse Mode (All vectors at once)** |

---

---

## **⚠️ Troubleshooting**

| **Issue** | **Solution** |
|-----------|--------------|
| `ModuleNotFoundError: No module named 'X'` | Run `pip install X` in the virtual environment. |
| `pip: command not found` | Install `python3-pip` (`sudo apt install python3-pip` on Linux). |
| `python: command not found` | Use `python3` or install `python-is-python3`. |
| `Scapy: Npcap not found` (Windows) | Install [Npcap](https://npcap.com/). |
| `Permission denied` (Linux) | Use `sudo` or a virtual environment. |
| `externally-managed-environment` (Ubuntu/WSL) | Use `python3 -m venv venv` + `source venv/bin/activate`. |
| **Scapy/ARP Spoof not working** (Termux/WSL) | Use **native Linux/Windows** for full functionality. |

---

---
---
## **📌 Quick Start Commands**
| **OS**       | **Installation Command** | **Run Command** |
|--------------|--------------------------|-----------------|
| **Windows**  | `pip install -r config/requirements.txt` | `python main.py` |
| **Linux**    | `python3 -m venv venv && source venv/bin/activate && pip install -r config/requirements.txt` | `python3 main.py` |
| **MacOS**    | `python3 -m venv venv && source venv/bin/activate && pip install -r config/requirements.txt` | `python3 main.py` |
| **Termux**   | `pip install -r config/requirements.txt` | `python main.py` |

---
---
---
### **💡 Pro Tips**
1. **Always use a virtual environment** (`venv`) on Linux/MacOS/WSL to avoid conflicts.
2. **Test on `127.0.0.1` first** to ensure the tool works before targeting other IPs.
3. **Reduce threads** (`-th 50`) if you experience performance issues.
4. **For Scapy on Windows**, **Npcap is mandatory**.
5. **Termux/WSL users**: Some attacks (Scapy, ARP Spoof) **won’t work** due to OS limitations.

---
### **⚠️ Legal Disclaimer**
> **⚠️ FOR AUTHORIZED TESTING ONLY**
> This tool is for **educational and authorized security testing purposes only**.
> **Unauthorized use against systems you do not own is ILLEGAL** and punishable by law.
> **The author is not responsible for any misuse of this tool.**

---
**By CAMZZZ / Evil Merlin**
*A dark sorcerer who ensures his tools work across all realms (OSes).* 🧙‍♂️💻

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

