from task_11_1F import parse_cdp_neighbors
import os
from draw_network_graph import draw_topology

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

path = "C:\\Users\\konst\\Desktop\\gitt\\test_py\\11\\"
files = [path + "sh_cdp_n_sw1.txt", path + "sh_cdp_n_r1.txt" , path + "sh_cdp_n_r2.txt", path + "sh_cdp_n_r3.txt"]

def create_network_map(filenames):
    all_conn = {}
    for name in filenames:
        with open(name, "r") as f:
            data = f.read()
            struct = parse_cdp_neighbors(data)
            all_conn.update(struct)
    
    all_test = {}
    for key, item in all_conn.items():
        if "SW" in key[0]:
            key , item = item, key
            all_test[key] = item
        else:
            all_test[key] = item

    for key, item in all_test.items():
        print(key, item)

    return all_test

topy = create_network_map(files)

draw_topology(topy)
