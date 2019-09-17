from tabulate import tabulate
#pip install tabulate

wrong_num = ["a",  "14.88.69.96", "aa.bb.cc.dd"]
true_num = ["192.168.1.1", "8.8.8.8", "87.250.250.242", "173.194.73.100"]
head = ["Reachable", "Unreachable"]

tpl = {"Unreachable" : wrong_num, "Reachable": true_num}
print(tabulate(tpl, headers='keys'))
