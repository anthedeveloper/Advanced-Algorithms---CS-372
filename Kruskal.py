from operator import itemgetter, attrgetter 
from Graph import *
def makeSet(x):
	p[x] = x
	r[x] = 0

def find(x):
	while x!= p[x]:
		x = p[x]	
	return x

def union(x,y):
	px = find(x)
	py = find(y)
	if px == py: return None
	if r[px] > r[py]: p[py] = px
	else:
		p[px] = py
		if r[px] == r[py]: r[py] += 1

def trans(g):
	q = {}
	for e in g.E:
		for v in g.E[e]:
			q[(e,v)] = g.E[e][v]
	a = q.items()
	b = sorted(a,key=itemgetter(1))
	return b

def kruskal(g):
	global p 
	p = {}
	global r
	r = {}
	for v in g.V:
		makeSet(v)
	fi = []
	w = trans(g)
	for i in w:
		if find(i[0][0]) != find(i[0][1]):
			fi.append((i[0][0],i[0][1]))
	 		union(i[0][0],i[0][1])
	 
	return fi




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

gr.addEdge(a,a,0)
gr.addEdge(b,b,0)
gr.addEdge(c,c,0)
gr.addEdge(d,d,0)
gr.addEdge(e,e,0)
gr.addEdge(f,f,0)
gr.addEdge(a,c,6)
gr.addEdge(a,d,4)
gr.addEdge(a,b,5)
gr.addEdge(b,c,1)
gr.addEdge(b,d,2)
gr.addEdge(c,d,2)
gr.addEdge(c,e,5)
gr.addEdge(c,f,3)
gr.addEdge(d,f,4)
gr.addEdge(e,f,4)

print kruskal(gr)