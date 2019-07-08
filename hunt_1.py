n=int(input())
arr=input().split()
arr2=[]
for i in range(n):
    for j in range(i+1,n):
        if arr[i]==arr[j] and arr[i] not in arr2:
            arr2.append(arr[i])
arr2.sort()
if len(arr2)==0:
    print('unique')
else:    
    print (' '.join(arr2))