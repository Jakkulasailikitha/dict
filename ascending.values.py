# for ascending order
# Dictionary in ascending order by value :[(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# the out put should be like this in list
a1={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
a2 = sorted(a1,key=a1.get)
d=[]
for r in a2:
    e=(r, a1[r])    
    d.append(e)
print(d)


# # two methods for doing this
l={1 : 25, 2 : 21, 3 : 23}
# c=(sorted(l.values()))
# print(c)
x=l.values()
b=sorted(x)
print(b) 
