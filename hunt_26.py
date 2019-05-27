n=int(input())
arr=list(input().split())
arr=arr[::-1]
for i in range(0,n-1):
    print(arr[i]+''.join("->"),end="")
print(arr[n-1])    