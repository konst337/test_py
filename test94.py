ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)


def get_int_vlan_map(file_name):
    f = open(file_name, "r")
    cfg = []
    commands = []
    dict1 = {}
    ''' dict_acces = {}
    dict_trunck = {}
    tuple1 = tuple() '''

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
    
   
get_int_vlan_map("D:\\repo_py\\test_py\\config_sw3.txt")
