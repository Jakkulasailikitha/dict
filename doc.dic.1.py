# Q1.Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# # Sample output:
# # Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for i  in d1:
#     if i in d2:
#         d2[i]=d1[i]+d2[i]
# d1.update(d2)
# print



# d={"name":"indhu"}
# d={'sajani','sai','kerthi'}
# a=d.fromkeys("name","indhu")
# print(a)


# d={"name":"sajani","sai":"kerthi"}
# f=d.fromkeys(d,"name")
# print(f)



a=["5001","5002","5003"]
b=["abc","def","ghf"]
c=["abc",2,3]
l=[]
for key in range(len(a)):
    d={b[key]:{a[key]:c[key]}}
    l.append(d)
print(l)