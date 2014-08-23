import math
def binarySearch(l,k):
	"""
	inputs: sorted list and a value
	output: if value is in list; True    
			if values is not in list; False """
	mid = int(math.floor(len(l)/2))
	if len(l) == 0:
		return False
	else:
		if l[mid] == k: return True
		elif l[mid] < k: return binarySearch(l[mid + 1:],k)
		else: return binarySearch(l[:mid],k)
			
def binaryIndexSearch(l,i,j,k):
	"""
	inputs: list, first index, last index, value
	output: if value is in list; its index
			if value is not in list; -1
	"""
	if len(l[i:j]) == 0: return -1
	else:
		m = (i+j)/2 #middle index
		if l[m] == k: return m
		elif l[m] < k: return binaryIndexSearch(l,m+1,j,k)
		else: return binaryIndexSearch(l,i,m,k)
		
		
# l = [0,1,2,3,4,5,6,7,9,10]
# print binarySearch(l,3)
# print binarySearch(l,8)
# print binaryIndexSearch(l,0,len(l)-1,3)
# print binaryIndexSearch(l,0,len(l)-1,8)