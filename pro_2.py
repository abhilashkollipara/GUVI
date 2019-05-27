from itertools import combinations
n,k=map(int,input().split())
m=len(str(n))
l=list(combinations(str(n),m-k))
l.sort()
print("".join(l[0]))