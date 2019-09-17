file = open("C:\\repo_py\\test_py\\sh_cdp_n_sw1.txt", "r")
buff = file.read()
def parse_cdp_neighbors(command_output):
    dict1 = {}
    sw = command_output[:command_output.find(">")].rstrip().split()
    sw = ''.join(sw)
    
    command_output = command_output[command_output.find("Device")::].rstrip().split("\n")
    command_output = command_output[1::]
    for i in range(len(command_output)):
        command_output[i] = command_output[i].split()
        
    for i in range(len(command_output)):
        dev, inter, num, *other, inter1, num1 = command_output[i]
        inter = inter + num
        inter1 = inter1 + num1
        dict1[sw, inter] = dev, inter1

    return dict1
        

        
if __name__ == "__main__":
    lol =parse_cdp_neighbors(buff)
    for line in lol.items():
        print(line)
