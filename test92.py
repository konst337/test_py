trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}


def genConf(trunk_temp, trunk_cfg):
    for face, num in trunk_cfg.items():
        print(face)
        for command in trunk_temp:
            if "allowed" in command:
                print(command, *num)
            else: print(command)




genConf(trunk_mode_template, trunk_config)