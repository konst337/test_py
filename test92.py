trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

dct = {}
def genConf(trunk_temp, trunk_cfg):
    dick = {}
    for face, num in trunk_cfg.items():
        print(face)
        temp = []
        for command in trunk_temp:
            if "allowed" in command:
                port = ""
                for i in num:
                    port += "{}, ".format(str(i))
                print("{} {}".format(command, port.strip(", ")))
                temp.append("{} {}".format(command, port.strip(", ")))
            else: 
                print(command)
                temp.append(command)
        dick[face] = temp

    return dick




dct = genConf(trunk_mode_template, trunk_config)
print(dct)