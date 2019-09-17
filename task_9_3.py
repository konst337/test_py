def get_int_vlan_map(file_name):
    f = open(file_name, "r")
    cfg = []
    dict_acces = {}
    dict_trunck = {}
    tuple1 = tuple()

    
    cfg = f.readlines()
      
    for line in cfg:
        if line.find("FastEthernet") != -1:
            face = line[line.find("FastEthernet")::].strip()
        elif line.find("access vlan") != -1:
            buff = line[line.find("access vlan")::].replace("access vlan", "").strip()
            dict_acces[face] = buff
        elif line.find("vlan") != -1:
            buff = line[line.find("vlan")::].replace("vlan", "").strip()
            dict_trunck[face] = buff
    tuple1 = (dict_acces, dict_trunck)
    return tuple1
    


            

  

kek = get_int_vlan_map("C:\\repo_py\\test_py\\config_sw3.txt")
print(kek)