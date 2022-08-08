
# Write a Python script to concatenate the following dictionaries to create a
# new one.
# d1={1:10, 2:20}
# d2={3:30, 4:40}
# d3={5:50,6:60}
# # Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# d={}
# for i in (d1,d2,d3):
#     d.update(i)
# print(d)



# Write a Python program to print all unique values in a dictionary. 
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
#                {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
# a=["5001","5002","5003"]
# b=["abc","def","ghf"]
# c=["abc",2,3]
# l=[]
# for key in range(len(a)):
#     d={b[key]:{a[key]:c[key]}}
#     l.append(d)
# print(l)



# # 3. Write a function check(key) which takes a key as an argument and check
# # # whether that key is present in dictionary or not
# d1 = {1 :"Amit",2 : "Suman"}
# def check(i):
#   for k in d1:
#     if k==i:
#       print("key is present")
#       break 
#     else: 
#       print("key is not present")
# check(1) #This function is only to verify code