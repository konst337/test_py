from sys import argv 

ignore = ['duplex', 'alias', 'Current configuration']
name = argv[1]
name2 = argv[2]
print(name)
file = open(name, "r")
filer = open(name2, "w")
for i in file:
    if (not (i.startswith("!"))):
        if (i.find(ignore[0]) == -1) and (i.find(ignore[1]) == -1) and (i.find(ignore[2]) == -1): 
            print(i.strip())
            filer.writelines(i)
file.close()
filer.close()
        
               
    
        