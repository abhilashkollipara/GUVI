n=int(input())
if (n <= 1): 
    print("no")
if (n <= 3): 
    print("no")
if (n % 2 == 0 or n % 3 == 0): 
    print("yes")
i = 5
while(i * i <= n): 
    if (n % i == 0 or n % (i + 2) == 0): 
        print("yes")
    i = i + 6    
if(n==5):
    print("no")