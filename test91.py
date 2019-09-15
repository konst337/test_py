access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}

port_security_template = [
    'switchport port-security maximum 2',
    'switchport port-security violation restrict',
    'switchport port-security'
]

template = []
def generate_access_config(intf_vlan_mapping, access_template, psecurity = None):
    temp = []
    for face, port in access_config.items():
        temp.append(face)
        print(face)
        for command in access_template:
            if "vlan" in command:
                print("{0} {1}".format(command, port))
                temp.append("{0} {1}".format(command, port))
            print(command)
            temp.append(command)
        if psecurity != None:
            for i in psecurity:
                print(i)
                temp.append(i)
    return temp

template = generate_access_config(access_config, access_mode_template, port_security_template)
