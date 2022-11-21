age=10
if(age>=10 and age<=18):
    print("Age is between 10 and 18")       # Indentation is important in conditionals in Python
    print("kid")
elif(age>18 and age<=30):
    print("Age is between 19 and 30")
elif(age>31 and age<=50):
    print("Age is between 31 and 50")
else:
    print("Age is above 50")


age=20
if(age>=10 and age<=18):
    print("Age is between 10 and 18")       # These two statements are in the if condtion but the "Done" is not int the if conditon
    print("kid")
print("Done")