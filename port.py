import socket 

def port_scanner(ip, port): 
    try: 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
            s.settimeout(1)  # Timeout for connection 
            s.connect((ip, port)) 
            print(f"[+] Port {port} is OPEN on {ip}") 
    except: 
        print(f"[-] Port {port} is CLOSED on {ip}") 

# Example Usage 
ip = "8.8.8.8"  # Localhost 

for port in range(45,55): 
    port_scanner(ip, port)
