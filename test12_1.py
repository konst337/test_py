import ipaddress
import subprocess

def ping_ip(ip_address):
    """
    Ping IP address and return tuple:
    On success:
        * True
        * command output (stdout)
    On failure:
        * False
        * error output (stderr)
    """
    reply = subprocess.run(['ping', ip_address])
    if reply.returncode == 0:
        return True
    else:
        return False

print(ping_ip('8.8.8.8'))
print(ping_ip('a'))
print(ping_ip("192.168.1.1"))