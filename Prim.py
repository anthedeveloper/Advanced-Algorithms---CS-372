from Graph import *
from Heap import *
import random

def prim(g,s):
	cost = {}
	prev = {}
	h = Heap([])

	for v in g.V:
		cost[v] = float("inf")
		prev[v] = None
		h.insert(v)
# 	x = list(g.V)
# 	s = random.choice(x)
	cost[s] = 0
	while len(h.heap) != 0:
		u = h.deleteMin()
		#print dist,prev
		if u in g.E:
			for e in g.E[u]:
				#print u,e,g.E[u][e]
				if cost[e] > g.E[u][e]:
					cost[e] = g.E[u][e]
					prev[e] = u
					h.decreaseKey(e)
					print cost,prev
	print cost, prev
	
	
	
gr = UndirectedGraphLength()
a = "A"
b = "B"
c = "C"
d = "D"
e = "E"
f = "F"

gr.addNode(a)
gr.addNode(b)
gr.addNode(c)
gr.addNode(d)
gr.addNode(e)
gr.addNode(f)

gr.addEdge(a,b,5)
gr.addEdge(a,c,6)
gr.addEdge(a,d,4)
gr.addEdge(b,c,1)
gr.addEdge(b,d,2)
gr.addEdge(c,d,2)
gr.addEdge(c,e,5)
gr.addEdge(c,f,3)
gr.addEdge(d,f,4)
gr.addEdge(e,f,4)

prim(gr,a)
