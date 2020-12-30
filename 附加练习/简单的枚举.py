ls = []
ans = 0
for i in range(100, 900):
	ls = []
	lsx = []
	for m in str(i):
		if m not in ls and m != '0':
			ls.append(m)	
	if len(ls) == 3:
		lsx = ls[:]
		
		for t in range(100, 900):
			x = i + t
			if x > 999:
				ls = lsx
				break
			else:
				for n in str(t):
					if n not in ls and n != '0':
						ls.append(n)
						
				for p in str(x):
					if p not in ls and p != '0':
						ls.append(p)
						
				if len(ls) == 9:
					print(str(i)+'+'+str(t)+'='+str(x))	
					ans += 1
				ls = lsx[:]
					
	else:
		ls = []
		lsx = []
