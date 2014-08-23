from Graph import *
import random	

def dfs(G, v):
	visited = set()
	def explore(G, v):	
		visited.add(v)
		edges = set()
		if v in G.E.keys():
			edges = G.E[v]
		for e in edges:
			if e not in visited: explore(G, e)
	explore(G,v)
	print visited	
	

	
def noIncome(g,v):
 	for e in g.E:
 		if e!=v:
 			if v in g.E[e]:
 				return False
 	return True			

			
def linearization(g):
	if len(g.E.keys()) == 1:
		print g.E.keys()[0]
		for i in g.E.values()[0]:
			print i
		return "Done"
	else:
		x = random.choice(g.E.keys())
		if noIncome(g,x) == True:
			print x
			del g.E[x]
			return linearization(g)
		else: return linearization(g)
		
		
		
		
gr = UndirectedGraph()
a = "A"
b = "B"
c = "C"
d = "D"
e = "E"
f = "F"
g = "G"
h = "H"
i = "I"
j = "J"
k = "K"
l = "L"

gr.addNode(a)
gr.addNode(b)
gr.addNode(c)
gr.addNode(d)
gr.addNode(e)
gr.addNode(f)
gr.addNode(g)
gr.addNode(h)
gr.addNode(i)
gr.addNode(j)
gr.addNode(k)
gr.addNode(l)

gr.addEdge(a,b)
gr.addEdge(a,e)
gr.addEdge(e,a)
gr.addEdge(e,i)
gr.addEdge(e,j)
gr.addEdge(j,i)
gr.addEdge(c,d)
gr.addEdge(c,h)
gr.addEdge(c,g)
gr.addEdge(d,h)
gr.addEdge(g,h)
gr.addEdge(g,k)
gr.addEdge(k,h)
gr.addEdge(h,l)
#print gr.E

#linearization(g) ####   B D A C E F
#print g.V #set(['A', 'C', 'B', 'E', 'D', 'F'])