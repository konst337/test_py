while(True):
    try:
        ip = input('Enter ip address: ')
        ip = ip.split(".")
        print("{0}.{1}.{2}.{3}".format((int(ip[0])), (int(ip[1])), (int(ip[2])), (int(ip[3]))))
        if ((int(ip[0]) < 256) and (int(ip[0]) >= 0)) and ((int(ip[1]) < 256) and (int(ip[1]) >= 0)) and ((int(ip[2]) < 256) and (int(ip[2]) >= 0)) and ((int(ip[3]) < 256) and (int(ip[3]) >= 0)):
            if (int(ip[0]) < 224) and (int(ip[0]) > 0):
                print("unicast")
            elif (int(ip[0]) > 223) and (int(ip[0]) < 240):
                print("multicast")
            elif ("255" in ip[0]) and ("255" in ip[1]) and ("255" in ip[2]) and ("255" in ip[3]):
                print("local broadcast")
            elif ("0" in ip[0]) and ("0" in ip[1]) and ("0" in ip[2]) and ("0" in ip[3]):
                print("unassigned")
            else:
                print("unused")
            break
        else:
            print("Адрес введен в неверном формате!")

    except ValueError:
        print("Пожалуйста, вводите только числа")
   
