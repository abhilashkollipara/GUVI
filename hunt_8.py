from itertools import combinations
n=int(input())
arr=[int(x) for x in input().split()]
comb=combinations(arr,3)
arr=list(sum(comb,())) 
a = []
for i in range(0,len(arr),+3):
    if ((arr[i]+arr[i+1]) == arr[i+2]):
        print(arr[i],arr[i+1],arr[i+2])