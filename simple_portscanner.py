# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Algorithms:
1. Start
2. Input Target IP Address (target_ip) and Port Range (start_port, end_port)
3. Initialize an empty list `open_ports` to store open ports
4. Loop through each port in the specified range (from start_port to end_port):
 a. Create a socket using `socket.socket()
   - b. Set a timeout for the socket using `socket.settimeout()
   - c. Try to connect to the target IP on the current port using `socket.connect_ex()
     - i. If the connection is successful (returns 0):
       - - Append the current port to `open_ports`
     - ii.   If the connection fails:
       - - Ignore and continue to the next port
   - d. Close the socket using `socket.close()
5. Print the list of open ports
6. End
"""
import vincent_chimaobi
import socket

def port_scanner(target_ip, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        """
        socket.AF_INET: The socket will use IPv4 addresses.
        socket.SOCK_STREAM: The socket will use the TCP protocol, which provides reliable, ordered, 
        and error-checked delivery of a stream of data between applications.
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set timeout for the socket (in miliseconds)
        sock.settimeout(1)
        try:
            result = sock.connect_ex((target_ip, port))
            # Check if the port is open
            if result == 0:
                open_ports.append(port)
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed (result code: {result})")
        except Exception as e:
            print(f"Error on port {port}: {e}")
        finally:
            sock.close()
    # Out puting all the open ports within the ports range
    return open_ports

target_ip = input("Enter the target IP address: ")
start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))
# print("Scanning.......")
# imported code for auto loading with dots ("Scanning......")
import auto_scanning_thread
# Scan the ports
open_ports = port_scanner(target_ip, start_port, end_port)
print(f"Open ports: {open_ports}")