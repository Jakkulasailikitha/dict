# 1.Write a Python script to generate and print a dictionary that contains a number 
# (between 1 and n) in the form (x, x*x).
# Sample input ( n = 5) :
# Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.


#2.Accept the number of terms say n from the user and display the dictionary 
# in the form of {n: n*5} for example:
# If number of terms entered by user is 4 then the expected dictionary is
# {1:5, 2:10, 3: 15, 4: 20}
# a={}
# user=int(input("enter the number:"))
# for i in range(user):
#     a[i+1]=(i+1)*4
# print(a)

# 3. Write a program to add the values of given dictionary.
d1 = {1:2, 2: 90, 3: 50}
for i in d1:
    c=sum(d1.values())
print(c)