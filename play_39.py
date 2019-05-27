n=int(input())
k=2
if n==1:
        print("yes")     
else: 
    while k<=n:
        if k==n:
            print("yes")
            break
        else:
            k=k*2
    if n!=k:
        print("no")