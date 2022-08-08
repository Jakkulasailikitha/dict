#  Write a program in python to remove the duplicate values from the dictionary. For example:
# Original dictionary = {1 : “Aman”, 2: “Suman”, 3: “Aman”}
n= {1 : "Aman", 2: "Suman",3:"Aman"}
d={}
for a,b in n.items():
    if b not in d.values():
        d[b]=a
print(d)
