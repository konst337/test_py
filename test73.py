file = open('D:\\repo_py\\test_py\\CAM_table.txt', 'r')
table = []
for i in file:
    table += file.readlines()
table = table[5:]

for i in range(len(table)):
    table[i] = table[i].replace("DYNAMIC", "").split()

temp = "{0:<5} {1:<16} {2}"

k = []
for j in range(len(table)):
    for i in range(len(table) - 2):
        if table[i][0] > table[i+1][0]:
            k = table[i]
            table[i] = table[i+1]
            table[i+1] = k 
    

for i in range(len(table)):
    print(temp.format(table[i][0], table[i][1], table[i][2]))