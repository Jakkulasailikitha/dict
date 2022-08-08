# to find the employeee name and salary in dictionary
num=int(input("enter the number of employees:"))
employee=dict()
for count in range(num):
    name=input("enter the name of the employees:")
    salary=int(input("enter the salary of the employees:"))
    employee[name]=salary
print("\n enploye_name\t salary")
for k in employee:
    print(k,'\t\t',employee[k])