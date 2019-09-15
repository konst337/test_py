access_template = [
    'switchport mode access', 'switchport access vlan',
    'spanning-tree portfast', 'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan'
]

access = {
    '0/12': '10',
    '0/14': '11',
    '0/16': '17',
    '0/17': '150'
}
trunk = {
        '0/1': ['add', '10', '20'],
        '0/2': ['only', '11', '30'],
        '0/4': ['del', '17']
    }

for num, port in trunk.items():
    print('interface FastEthernet' + num)
    for command in trunk_template:
        if command.endswith('vlan'):
            if num == "0/1":
                print(' {} {}'.format(command, ",".join(port)).replace("add,", "add "))
            elif num == "0/2":
                print(' {} {}'.format(command, ",".join(port)).replace("only,", ""))
            else: 
                print(' {} {}'.format(command, ",".join(port)).replace("del,", "remove "))
        else:
            print(' {}'.format(command))

''' for intf, vlan in access.items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command)) '''