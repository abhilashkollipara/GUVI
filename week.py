day= input().split()
lis1={"Monday","Tuesday","Wednesday","Thursday","Friday"}
lis2={"Saturday","Sunday"}
i=0
n=len(day)
for i in range(n):

    if day[i] in lis1:
        print("no")
    
    elif day[i] in lis2:
         print("yes")
