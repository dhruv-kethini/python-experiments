age_str = input("Enter your age: ")
age = int(age_str) 
if age<13:
    print("child")
elif age>=18:
    print("adult")
else:
    print("teenager")