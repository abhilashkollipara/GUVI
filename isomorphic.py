def isIso(a,b):
        if(len(a) != len(b)):
                return false
        x=[a.count(char1) for char1 in a]
        y=[b.count(char1) for char1 in b]
        return x==y                   
string1,string2 = input().split()
if(isIso(string1,string2)==True):
        print("yes")
else:
        print("no")
