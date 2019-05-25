from itertools import permutations 
n=input()
perm = permutations(n)
for i in list(perm): 
	print (''.join(i))
