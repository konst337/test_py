from sys import argv 

ignore = ['duplex', 'alias', 'Current configuration']
name = argv[1]
print(name)
file = open(name, "r")
filer = open("config_sw1_cleared.txt", "w")
for i in file:
    if (not (i.startswith("!"))):
        if (i.find(ignore[0]) == -1) and (i.find(ignore[1]) == -1) and (i.find(ignore[2]) == -1): 
            print(i.rstrip().strip())
            filer.writelines(i)
        
        
               
    
        