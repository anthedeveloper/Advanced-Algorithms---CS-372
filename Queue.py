class Queue:
	def __init__(self):
		self.l = list()
		
	def enqueue(self,k):
		self.l.append(k)
		return self.l
		
	def dequeue(self):
		k = self.l.pop(0)
		return k
		
	def empty(self):
		if len(self.l) == 0: return True
		return False
		

q = Queue()
print q.enqueue(1)
print q.enqueue(2)
print q.enqueue(3)
print q.dequeue()