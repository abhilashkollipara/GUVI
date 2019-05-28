n=input()
arr=list(input().split())
k=arr.copy()
arr.sort()
if(k==arr):
    print("yes")
else:
    print("no")