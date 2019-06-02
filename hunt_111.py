n=int(input())
a = []
ar=0
for i in range(n):
    a.append([int(j) for j in input().split()])
for i in range(0,n):
    ar=ar+a[i][i]
print(ar)