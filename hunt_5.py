n=int(input())
m=str(n)
c=0
for i in range(0,len(m)):
  if int(m[i:i+2])<26 and len(str(int(m[i:i+2])))==2:
    c=c+1
if c==2:
  print(c+c//2)
else:
  print(c+c//2+1)