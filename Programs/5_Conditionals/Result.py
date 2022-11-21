n1=int(input("Enter the marks: "))
n2=int(input("Enter the marks: "))
n3=int(input("Enter the marks: "))

avg=(n1+n2+n3)/3

if(avg>=40 and n1>=33 and n2>=33 and n3>=33):
    print("Pass")
else:
    print("Fail")