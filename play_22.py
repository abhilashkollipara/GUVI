x,y = map(int,input().split())
while (y!= 0):
    temp = y
    y = x % y
    x = temp

gcd = x   
print(gcd)