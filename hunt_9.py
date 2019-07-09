from itertools import combinations
n=int(input())
arr=[int(x) for x in input().split()]
m=max(arr)
comb=combinations(arr,3)
arr=list(sum(comb,())) 
x=0
y=0
for i in range(0,len(arr),2):
    if (abs(arr[i]+arr[i+1])<m):
        x,y=arr[i],arr[i+1]
        m=abs(x+y)
        
print(x,y)