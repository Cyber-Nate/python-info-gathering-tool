# 🛡️ Cyber Nate — Python Information Gathering Tool

> Cross-platform ping-based reconnaissance script for ethical hacking
> Built for MetBrains 7-Day Cyber Camp | Guided by Prof. Dimple Chauhan

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Mac-green)
![License](https://img.shields.io/badge/License-Educational-orange)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 📌 Description

This tool performs active network reconnaissance using the system `ping`
command. It auto-detects the operating system and presents the appropriate
ping arguments, validates user input, and executes the command with
colour-coded output.

---

## ⚙️ Features

| Feature | Description |
|---|---|
| 🖥️ Cross-Platform | Auto-detects Windows, Linux & Mac |
| 🎨 Colour Output | ANSI colour-coded terminal interface |
| ✔ Input Validation | Validates domain before executing |
| ⚙️ Multi-Argument | Supports all ping flags combined |
| 🔄 Repeat Mode | Run multiple pings without restarting |
| 📋 Help Menu | Shows OS-specific args with descriptions |

---

## 🚀 How to Run
```bash
# Clone the repo
git clone https://github.com/Cyber-Nate/python-info-gathering-tool

# Navigate to folder
cd python-info-gathering-tool

# Run the script
python cyber_nate_ping_tool.py
```

---

## 📸 Screenshots

### Demo 1 — Basic Ping (`-n 4`)
![Demo1](screenshots/screenshot1.png)

### Demo 2 — Large Packet (`-n 4 -l 512`)
![Demo2](screenshots/screenshot2.png)

---

## 📖 Supported Ping Arguments

### Windows
| Argument | Purpose |
|---|---|
| `-n <count>` | Number of packets to send |
| `-l <size>` | Packet buffer size in bytes |
| `-t` | Ping continuously (Ctrl+C to stop) |
| `-i <TTL>` | Set Time To Live value |
| `-w <ms>` | Timeout in milliseconds |

### Linux / Mac
| Argument | Purpose |
|---|---|
| `-c <count>` | Number of packets to send |
| `-s <size>` | Packet size in bytes |
| `-i <interval>` | Interval between packets |
| `-W <sec>` | Timeout in seconds |
| `-q` | Quiet mode — summary only |

---

## ⚠️ Disclaimer

This tool is built strictly for **educational purposes** and
**authorized ethical hacking** only. Do not use on systems you
do not own or have explicit written permission to test.

---

## 👤 Author

**Nathaniel Temitope Ogunjobi**
AMICDFA | CCEP | CBTP | CTIGA | SOC Analyst

🌐 [cybernatesec.netlify.app](https://cybernatesec.netlify.app)
💼 [LinkedIn](https://linkedin.com/in/nathaniel-cybersecurity)
📺 [YouTube: @CyberNation01](https://youtube.com/@CyberNation01)

---

*MetBrains 7-Day Cyber Camp 2026 | Guided by Prof. Dimple Chauhan*
