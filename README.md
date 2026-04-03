# Advanced Multithreaded Port Scanner

This is a Python-based advanced port scanner built using socket programming and multithreading.

## Features
- Custom target IP/domain input
- Custom port range scanning
- Fast multithreaded execution
- Open port detection
- Clean command-line output

## Technologies Used
- Python
- socket
- ThreadPoolExecutor
- datetime

## How It Works
The script takes a target and a port range from the user.
It then checks each port using TCP socket connections.
If the connection is successful, the port is marked as open.

## Example Input
Target: 127.0.0.1
Start Port: 20
End Port: 100

## Author
Shivraj 
