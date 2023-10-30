from pprint import pprint

d={}
d["a"] = [x for x in range(1,11)]
d["b"] = [x for x in range(11,21)]
d["c"] = [x for x in range(21,31)]

list=d["b"]
print(list[2])

print(d["b"][2])