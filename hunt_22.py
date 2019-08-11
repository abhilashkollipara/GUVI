n=int(input())
arr=[int(i) for i in input().split()]
val=1
arr2=[]
for i in range(n):
    val=int(val*arr[i])
for j in range(n):    
    arr2.append(int(val/arr[j]))
for i in range(n):
    print(arr2[i],end=" ")    