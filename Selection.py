import random
def swap(l,i,j):
	"""
	input: list, two indexes
	output: None
	Just swap the elements in given indexes
	"""
	x = l[j]
	l[j] = l[i]
	l[i] = x
	

def splt(l,v):
	sl,sv,sr = [],[],[]
	for i in l:
		if i < v: sl.append(i)
		elif i > v:	sr.append(i)
		else:	sv.append(i)
	return sl, sv, sr
	
	

def splt2(l,k):
 	"""
 	does not take extra memory
 	"""
	j = len(l)-1
	i = 0
	while i !=j:
		if l[i]>k and l[j]<=k:
			swap(l,i,j)
			i +=1
			j -= 1
		else:
			if l[i]<=k:
				i +=1
				if l[j]>k:	j -=1
				elif l[j]==k and l[j-1]>k: 
					swap(l,j,j-1)
					j -= 1		
				else: 
					if l[i]>k:
						swap(l,i,j)
						i +=1
						j -= 1
			else: j -= 1
		print i,j
	return l
	
	
def selection(l,k):	
	v = random.choice(l)
	sl,sv,sr = splt(l,v)
	if k <= len(sl):
		return selection(sl,k)
	elif len(sl)< k <= (len(sl)+len(sv)):
		return sv[0]
	else:
		return selection(sr,k-len(sl)-len(sv))
		
#l = [2,36,5,21,8,13,11,20,5,4,1]   #sorted [1, 2, 4, 5, 5, 8, 11, 13, 20, 21, 36]

#print selection(l,7)