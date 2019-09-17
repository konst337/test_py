print("-"*30)
access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

mode = input("Enter mode name (access/trunk): ")
inter = input("Enter type and number of interface: ")
vlan = input("Enter number of vlan: ")

access_template[1] = access_template[1].format(vlan)
trunk_template[2] = trunk_template[2].format(vlan)

dict = {
"trunk" : trunk_template,
"access" : access_template
}

print("-"*30)
print("Interface", inter)
for i in dict[mode]:
        print(i)
