m=input()
sum1=0
for i in range(len(m)):
   sum=0
   for j in range(i+1):
      sum=sum+int(m[j])
   sum1=sum1+sum
print(sum1)