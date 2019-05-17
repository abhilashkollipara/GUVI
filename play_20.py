a=str(input())
b=[]
l=len(a)
for i in range(0,l):
    c=ord(a[i])
    c=c+3
    if(a[i].isupper()==True):
        if(c==91):
            c=65
        elif(c==92):
            c=66
        elif(c==93):
            c=67
    b.append(chr(c))
print(*b,sep='')