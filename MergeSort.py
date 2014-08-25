def merge(l1,l2): #linear time alg
	"""
	input: two lists
	output: one sorted list
	"""
	if len(l1) == 0: return l2
	if len(l2 )== 0: return l1
	if l1[0] <= l2[0]: return l1[:1] + merge(l1[1:],l2)
	else: return l2[:1] + merge(l1,l2[1:])
		
def mergeSort(l):#nlog(n)
	n = len(l)
	if n>1:
		return merge(mergeSort(l[:n/2]),mergeSort(l[n/2:]))
	else:
		return l

#l = [9,4,7,2,5,6,1,8,34,456,234,45,2,54,646,43,346,647,678]
l = [2,36,5,21,8,13,11,20,5,4,1]

print mergeSort(l)		
		
def iterativeMerge(l):#nlog(n)
	q = []
	for i in l:
		q.append([i])
	while len(q)>1:
		q.append(merge(q.pop(0),q.pop(0)))
	return q.pop(0)