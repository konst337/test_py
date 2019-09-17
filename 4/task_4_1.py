print("--"*100)
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
if NAT.find("Fast"):
    NAT = NAT.replace("Fast", "Gigabit")
    print(NAT)

print("-"*40)
mac = 'AAAA:BBBB:CCCC'
mac = mac.replace(':', ".")
print(mac)

print("-"*40)
config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
config = config.split()
VLAN = config[4].split(',')
print(VLAN)

print("-"*40)
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
vlans = set(vlans)
vlans = list(vlans)
vlans = sorted(vlans)
print(vlans)

print("-"*40)
command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
command1 = command1.split()
command2 = command2.split()
m1 = command1[4].split(',')
m2 = command2[4].split(',')
m1 = set(m1)
m2 = set(m2)
m3 = m1 & m2
m3 = list(m3)
m3 = sorted(m3)
print(m3)

print("-"*40)
ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.replace("O", "OSPF")
ospf_route = ospf_route.split()
ospf_route[2] = ospf_route[2].strip("[]")
ospf_route[4] = ospf_route[4].strip(",")
ospf_route[5] = ospf_route[5].strip(",")

print('Protocol:           {:15}'.format(ospf_route[0]))
print('Prefix:             {:15}'.format(ospf_route[1]))
print('AD/Metric:          {:15}'.format(ospf_route[2]))
print('Next-Hop:           {:15}'.format(ospf_route[3]))
print('Last update:        {:15}'.format(ospf_route[4]))
print('Outbound Interface: {:15}'.format(ospf_route[5]))

print("-"*40)
mac1 = 'AAAA:BBBB:CCCC'
mac1 = mac1.replace(":", '')
mac1 = int(mac1, 16)
mac1 = bin(mac1)
print(mac1)

print("-"*40)
ip = '192.168.3.1'
ip_temp = '''
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''
ip = ip.split('.')
print(ip_temp.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])))