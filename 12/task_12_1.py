import ipaddress
import subprocess

def ping_ip(ip_address):
    true_list = []
    false_list = []
    tupoy = tuple()
    for ip in ip_address:
        reply = subprocess.run(['ping', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if reply.returncode == 0:
            true_list.append(ip)
        else:
            false_list.append(ip)
    tupoy = (true_list, false_list)
    return tupoy
            
ips = ["192.168.1.1", "8.8.8.8", "a", "87.250.250.242", "173.194.73.100", "14.88.69.96"]
test = ping_ip(ips)
print(test)