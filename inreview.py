# start=int(input("enter the num1:"))
# end=int(input("enter the num1:"))
# for num in range(start,end+1):
#     if num>1:
#         for i in range(2,num):
#             if (num%i)==0:
#                 break
#         else:
#             print(num)
    
    
import json
d={
    "name":"amla",
    "age":45,
    "employee":"no"
}
f=open("abc.json","w")
json.dump(d,f)
with open("abc.json","r") as f:
    a=json.load(f)
print(a)


a=open("abc.json","r")
b=json.load(a)
print(b)



# def function(n,m):
#     for i in range(n,m):
#         if i>1:
#             for j in range(2,i):
#                 if i%j==0:
#                     break
#             else:
#                 print(i)
# n=int(input("enter the starting number:"))
# m=int(input("enter the end number here:"))
# function(n,m)
