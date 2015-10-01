# #Naive solution. This won't work you can't repeat numbers
# for a in range(1,6):
# 	for b in range(1,6):
# 		for c in range(1,6):
# 			for d in range(1,6):
# 				for e in range(1,6):
# 					for f in range(1,6):
# 						ans = (a + b - c) * d // e * f
# 							print (a, b, c, d, e, f)
# 							#Still have to check to see if your solutions have repitions
# 							#Too much work
						

from itertools import permutations

p = list(permutations([1, 2, 3, 4, 5, 6]))

for i in range(0 ,  720):
	ans = (p[i][0] + p[i][1] - p[i][2]) * p[i][3] // p[i][4] * p[i][5]
	if ans == 50:
		print(p[i])
