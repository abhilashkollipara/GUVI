n=input()
for i in K:
	A=n.count('(')
	B=n.count(')')
if A==B:
	print("yes")
else:
	print("no")