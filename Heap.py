class Heap:
	def __init__(self,l):
		self.heap = l	 	
	
	def deleteMin(self):
		self.heap[0],self.heap[-1] = self.heap[-1],self.heap[0]
		minVal = self.heap.pop()
		i = 0
		while (i*2) < (len(self.heap)/2 -1 ):
			if self.heap[i] > self.heap[(2*i+1)] and self.heap[i] >self.heap[(2*i+2)]:	
				if self.heap[2*i+1] < self.heap[2*i+2]:
					self.heap[2*i+1],self.heap[i] = self.heap[i],self.heap[2*i+1]
				else: 
					self.heap[2*i+2],self.heap[i] = self.heap[i],self.heap[2*i+2]
			i +=1
		return minVal
		
	def insert(self,k):
		self.heap.append(k)
		i = len(self.heap)-1
		while i / 2 >= 0:
			if i == 0: break
			if i%2==1:
				if self.heap[i] < self.heap[i/2]:
					self.heap[i], self.heap[i/2] = self.heap[i/2], self.heap[i]
				i = i/2
			else:
				if self.heap[i] < self.heap[i/2-1]:
					self.heap[i], self.heap[i/2-1] = self.heap[i/2-1], self.heap[i]
				i = i/2-1
		return self.heap	
		
		
		
	def decreaseKey(self,i):
		while (i*2) <= (len(self.heap)/2):
			if self.heap[i] > self.heap[(2*i+1)] and self.heap[i] >self.heap[(2*i+2)]:	
				if self.heap[2*i+1] < self.heap[2*i+2]:
					self.heap[2*i+1],self.heap[i] = self.heap[i],self.heap[2*i+1]
				else: 
					self.heap[2*i+2],self.heap[i] = self.heap[i],self.heap[2*i+2]
			i +=1