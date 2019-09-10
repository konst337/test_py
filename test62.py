ip = input('Enter ip address: ')
ip = ip.split(".")

if ((ip[0] > 0) and (ip[0] < 224)):
    print("unicast")
elif (ip[0] > 223 and ip[0] < 240):
    print("multicast")
elif ((ip[0] and ip[1] and ip[2] and ip[3]) == 255):
    print("local broadcast")
