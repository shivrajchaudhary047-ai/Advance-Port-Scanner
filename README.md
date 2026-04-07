
# 🚀 Advanced Multithreaded Port Scanner

A professional Python port scanner using **multithreading** and **TCP socket programming**.

## Features
- ✅ User-defined target IP/domain
- ✅ Custom port range scanning  
- ✅ Multithreaded (50 worker threads) for speed
- ✅ Professional output formatting
- ✅ Error handling & timeout management

## How it works
1. **User input**: Target + port range
2. **Multithreading**: 50 threads scan ports parallel
3. **TCP Connect**: `socket.connect_ex()` checks port status
4. **Result**: `0` = OPEN port, non-zero = CLOSED

## Usage
$ python advanced_port_scanner.py
Enter target IP/domain: 127.0.0.1
Enter start port: 20
Enter end port: 100
Scan started: 2026-04-03 12:05:00
✅ Port 80 OPEN
✅ Port 443 OPEN
SCAN COMPLETE!

## Tech Stack
- **Python 3.x**
- `socket` - TCP networking
- `ThreadPoolExecutor` - Multithreading
- `datetime` - Timestamps

## Safe Testing
- Local: `127.0.0.1` (loopback)
- Public: `scanme.nmap.org` (authorized test target)

## Skills Demonstrated
- Socket programming
- Multithreading & concurrency
- Error handling
- Professional CLI development

---
**Built by Shivraj cyber** | B.Tech Cybersecurity | #Python #Cybersecurity #Networking
