import ipaddress
#rang = input("enter ip range: ")
rang = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
list1 = []
for i in range(len(rang)):
    if "-" in rang[i]:
        rang[i] = rang[i].split('-')
        ip1 = ipaddress.ip_address(rang[i][0])
        if len(rang[i][1]) <= 3:
            ip2 = int(rang[i][1])
            for i in range(ip2):
                list1.append(ip1)
                ip1 += 1

        elif ipaddress.ip_address(rang[i][1]):
            ip2 = ipaddress.ip_address(rang[i][1])
            list1.append(ip1)
            while ip1 != ip2:
                ip1 += 1
                list1.append(ip1)
            list1.append(ip2)

    else:
        ip1 = ipaddress.ip_address(rang[i])
        list1.append(ip1)


for ip in list1:
    print(ip)