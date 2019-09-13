print("-"*30)
ip = input("Enter your ip and mask in this format \"10.1.1.0/24\": ")
ip = ip.split('/')

try:
    ip1 = ip[0]
    mask = ip[1]
    mask = int(mask)
    ip1 = ip1.split('.')

    net_byte = """{0:08b}{1:08b}{2:08b}{3:08b}"""
    nethex = net_byte.format(int(ip1[0]), int(ip1[1]), int(ip1[2]), int(ip1[3]))
    nethex_mask = "{0:<032}".format(nethex[:mask])
    net_bytes = "{0:<08}.{1:<08}.{2:<08}.{3:<08}".format(int(nethex_mask[0:8]), int(nethex_mask[8:16]), int(nethex_mask[16:24]), int(nethex_mask[24::]))
    net_bytes = net_bytes.split(".")
        
    net_temp = """
    Network:
    {0:<8} {1:<8} {2:<8} {3:<8}
    {0:08b} {1:08b} {2:08b} {3:08b}
    """
    print(net_temp.format(int(net_bytes[0], 2), int(net_bytes[1], 2), int(net_bytes[2], 2), int(net_bytes[3], 2)))

    mask1 = "1"*mask
    mask1 ="{:<032}".format(mask1)
    mask_bytes = "{0:<08}.{1:<08}.{2:<08}.{3:<08}".format(int(mask1[0:8]), int(mask1[8:16]), int(mask1[16:24]), int(mask1[24::]))
    mask_bytes = mask_bytes.split(".")
    
    mask_temp = '''
    Mask:
    /{0:<8}
    {1:<8} {2:<8} {3:<8} {4:<8}
    {1:08b} {2:08b} {3:08b} {4:08b}
    '''
    print(mask_temp.format(mask, int(mask_bytes[0], 2), int(mask_bytes[1], 2), int(mask_bytes[2], 2), int(mask_bytes[3],2)))
except:
     print("You must enter address in the correct form!")