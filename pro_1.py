str1=input()
str2=input()
n1 = len(str1) 
n2 = len(str2) 
result = ""
i=0
j=0
while(i <= n1 - 1 and j <= n2 - 1):
    if (str1[i] != str2[j]): 
        break
    result += (str1[i]) 
    i += 1
    j += 1
print(result)