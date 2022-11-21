

for i in range(1,4):
    for space in range(1,3-i+1):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end="")
    print("")