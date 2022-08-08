# here  we are changing dictionary to list with values and keys

a={'a':1,"b":2,"c":3}
b = [] 
for key, val in a.items(): 
    b.append([key, val]) 
print(b)


	
# the another method to change the things
d = {"name":"python", "version":3.9}
new_list = []
for i in d:
  k = [i, d[i]]
  new_list.append(k)
print(new_list)