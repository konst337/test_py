file = open('D:\\repo_py\\test_py\\ospf.txt', 'r')
cfg = []
for i in file:
    cfg += file.readlines()
print(cfg)
templ = ['Protocol:', 'Prefix:', 'AD/Metric:', 'Next-Hop:', 'Last update:', 'Outbound Interface', ' ']

for i in range(len(cfg)):
    cfg[i] = cfg[i].replace("O", "OSPF")
    cfg[i] = cfg[i].replace("via", "")
    cfg[i] = cfg[i].split()
    cfg[i][2] = cfg[i][2].strip("[]")
    cfg[i][4] = cfg[i][4].strip(",")
    cfg[i][3] = cfg[i][3].strip(",")
    
for i in range(len(cfg)):
    print("-"*40)
    for j in range(len(cfg[i])):
        print(("{0:<20} {1} \n".format(templ[j], cfg[i][j]).rstrip()))
        
file.close()
