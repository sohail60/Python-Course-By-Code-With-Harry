f=0
max=0
a=str(15)
b=str(9)
c=str(50)

max(a,b,c)

def max(a,b,c):
    if(a>=b):
        f=a
    else:
        f=b

    if(c>=f):
        max=c
    else:
        max=f
    print(max)
