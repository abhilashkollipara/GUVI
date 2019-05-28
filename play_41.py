n,m=map(int,input().split())
k=m
if n==1:
        print("yes")     
else: 
    while k<=n:
        if k==n:
            print("yes")
            break
        else:
            k=k*m
    if n!=k:
        print("no")