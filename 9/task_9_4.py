ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
    return any(word in command for word in ignore)

def get_int_vlan_map(file_name):
    f = open(file_name, "r")
    cfg = []
    commands = []
    dict1 = {}
    for line in f:
        if (ignore_command(line, ignore) == False) and (line.find('!') == -1):
            cfg.append(line.rstrip())
    
    mainComand = ""
    for line in cfg:
        if not(line.startswith(" ")):
            if mainComand == "":
                mainComand = line
            else:
                dict1[mainComand] = commands
                commands = []
                mainComand = line
                dict1[mainComand] = commands
                         
        else:
            commands.append(line)    

    for key, itm in dict1.items():
        print(key, itm)
    return dict1        
    
if __name__ == '__main__':
    kek = get_int_vlan_map("C:\\Users\\konst\\Desktop\\gitt\\test_py\\9\\config_sw1.txt")
    print(kek)