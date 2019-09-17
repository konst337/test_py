mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = []
for i in mac:
    mac_cisco.append(i.replace(":", "."))

for i in mac_cisco:
    print(i)