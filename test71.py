file = open('D:\\repo_py\\test_py\\ospf.txt', 'r')
cfg = []
for i in file:
    cfg += file.readlines()
print(cfg)
templ = ['Protocol:', 'Prefix:', 'AD/Metric:', 'Next-Hop:', 'Last update:', 'Outbound Interface']
lest = []
for i in cfg:
    lest[i] = i.split()
print(lest)

''' for line in cfg:
    for word in line:
        print(word + '\n') '''


file.close()
