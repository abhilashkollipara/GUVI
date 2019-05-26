n=input()
for i in n:
	A=n.count('(')
	B=n.count(')')
if A==B:
	print("yes")
else:
	print("no")
