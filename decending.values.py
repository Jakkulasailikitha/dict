# Write a Python program to sort (ascending and descending) a dictionary 
# by value.
# Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value :[(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value :{3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
# for descending order
# a1={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# a2 = sorted(a1, key=a1.get,reverse=True)
# d=[]
# for r in a2:
#     e=(r, a1[r])
#     d.append(e)
# print(dict(d))


# 2.  Write a Python program to arrange the values in a dictionary in ascending order. For example
# Original Dictionary = {1 : 25, 2 : 21, 3 : 23}
# Expected Output = [21, 25, 32]

# # two methods for doing this
# l={1 : 25, 2 : 21, 3 : 23}
# # c=(sorted(l.values()))
# # print(c)
# x=l.values()
# b=sorted(x)
# print(b) 



