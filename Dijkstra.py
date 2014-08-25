from Graph import *
from Heap import *


def dijkstra(g,s):
	dist = {}
	prev = {}
	h = Heap([])

	for v in g.V:
		dist[v] = float("inf")
		prev[v] = None
		h.insert(v)
	dist[s] = 0
	while len(h.heap) != 0:
		u = h.deleteMin()
		#print dist,prev
		if u in g.E:
			for e in g.E[u]:
				#print u,e,g.E[u][e]
				if dist[e] > dist[u] + g.E[u][e]:
					dist[e] = dist[u] + g.E[u][e]
					prev[e] = u
					h.decreaseKey(v)
					print dist,prev
	print dist, prev
	
gr = GraphLength()
a = "A"
b = "B"
c = "C"
d = "D"
e = "E"
gr.addNode(a)
gr.addNode(b)
gr.addNode(c)
gr.addNode(d)
gr.addNode(e)

gr.addEdge(a,a,0)
gr.addEdge(a,b,4)
gr.addEdge(a,c,2)
gr.addEdge(b,c,3)
gr.addEdge(c,b,1)
gr.addEdge(b,d,2)
gr.addEdge(b,e,3)
gr.addEdge(c,e,5)
gr.addEdge(c,d,4)
gr.addEdge(e,d,1)
#print gr.E

dijkstra(gr,a)
