def config_filename():#file_name
    with open("D:\\repo_py\\test_py\\config_sw3.txt") as f:
        for line in f:
            str_all_interface, str_access_vlan, str_trunk_vlan = '', '', ''
            if line.find('FastEthernet') != -1:
                str_all_interface = line
                str_all_interface = str_all_interface[str_all_interface.find('FastEthernet')::]
                print(str_all_interface)

            elif line.find('access vlan') != -1:
                str_access_vlan = line
                str_access_vlan = str_access_vlan[str_access_vlan.find('vlan')::].replace('vlan ', '')
                print(str_access_vlan)

            elif line.find('allowed vlan') != -1:
                str_trunk_vlan = line
                str_trunk_vlan = str_trunk_vlan[str_trunk_vlan.find('vlan')::].replace('vlan ', '')
                print(str_trunk_vlan)

config_filename()