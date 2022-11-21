n=int(input("Enter the Number: "))
flag=0

if(n<=0):
    print("Invalid input")
elif(n==1):
    print("Neither Prime nor Composite")
else:
    for i in range(2,n):
        if(n%i==0):
            flag=1
    if(flag==1):
        print("Not Prime")
    else:
        print("Prime")
