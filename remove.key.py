# Write a program to accept a key from the user and remove that key from the 
# dictionary if present.
c={1:3,"tree":"mango","flower":"rose",6:5}
a=input("enter the key here:")
if a in c:
    c.pop(a)
    print("the key is present in it",c)
else:
    print("the key is not present in it")
    
            