string1,string2 = input().split()
temp = 0
n = int(len(string1))
for i in range(0,n) :
    if string1[i] != string2[i] :
        temp += 1        
if temp==1:
    print("yes")  
else :
   print("no")