class Graph():
	def __init__(self):
		self.V = set()
		self.E = dict()

	def addNode(self, v):
		self.V.add(v)

	def addEdge(self, u, v):
		self.E.setdefault(u, set())
		self.E[u].add(v)
		
	
class UndirectedGraph(Graph):
	def addEdge(self,u,v):
		self.E.setdefault(u, set())
		self.E.setdefault(v, set())
		self.E[u].add(v)
		self.E[v].add(u)
		
		
class GraphLength(Graph):
	def addEdge(self, u, v, l):
		self.E.setdefault(u, dict())
		self.E[u][v] = l
		
class UndirectedGraphLength(UndirectedGraph):
	def addEdge(self, u, v, l):
		self.E.setdefault(u, dict())
		self.E[u][v] = l
		self.E.setdefault(v, dict())
		self.E[v][u] = l
		
	
# gr = UndirectedGraphLength()
# a = "A"
# b = "B"
# c = "C"
# d = "D"
# gr.addNode(a)
# gr.addNode(b)
# gr.addNode(c)
# gr.addNode(d)
# 
# gr.addEdge(a,b,3)
# gr.addEdge(b,c,2)
# print gr.V
# print gr.E[a][b]
