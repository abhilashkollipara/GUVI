n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
arr.sort(reverse = False)     
n1 = len(arr[0])
t1=arr[0]
n2 = len(arr[n-1])
t2=arr[n-1]
result = "" 
j = 0
i = 0
while(i <= n1 - 1 and j <= n2 - 1): 
        if (t1[i]!=t2[j]): 
            break
        result += (t1[i]) 
        i += 1
        j += 1
print(result)