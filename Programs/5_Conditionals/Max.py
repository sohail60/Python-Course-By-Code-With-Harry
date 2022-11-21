n1=int(input("Enter a Number: "))
n2=int(input("Enter a Number: "))
n3=int(input("Enter a Number: "))
n4=int(input("Enter a Number: "))

if(n1>=n2):
    f1=n1
else:
    f1=n2

if(n3>n4):
    f2=n3
else:
    f2=n4

if(f1>f2):
    print("Greatest Number is "+str(f1))
else:
    print("Greatest Number is "+str(f2))