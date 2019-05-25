n,k=map(int,input().split())
l=[[abs(i-k),i]for i in list(map(int,input().split()))]
l.sort()
l=l[1:]
z=[i[1] for i in l[:3]]
print(*z,sep=' ')