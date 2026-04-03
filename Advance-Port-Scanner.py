import socket                                     #Python Built in Module for Networking(Make TCP connection)
from concurrent.futures import ThreadPoolExecutor #Use for Multithreading,multiple Ports scan and improve speed)
from datetime import datetime                     #Scan and finsh time
target = input("Target IP ya domain daalo: ")     #Taking Target IP
start_port = int(input("Start port daalo: "))     #Port Range
end_port = int(input("End port daalo: "))

print(f"Scanning start: {datetime.now()}")
print(f"Target: {target}")
print(f"Range: {start_port} to {end_port}")
open_ports = []                                    #Open Ports Store
def scan_port(port):                               #Single Port test
    try:
     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #IPv4 TCP Socket
     sock.settimeout(1)                            #1-sec timeout
     result = sock.connect_ex((target, port))      #Open port=0
     sock.close()
     if result == 0:
            open_ports.append(port)                 #Open Ports save in List
            print(f"✅ Port {port} OPEN")
    except:
        pass
with ThreadPoolExecutor(max_workers=50) as executor: #Multiple Ports scan
    executor.map(scan_port, range(start_port, end_port + 1))  # sacn_port() fuction parallel run
print("Scan complete!")
print("Open ports:", open_ports)
print(f"Finished at: {datetime.now()}")