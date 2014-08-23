from Graph import *

def bfs(g,s):
	dist = {}
	for v in g.V: ### O(V) 
		dist[v] = float("inf")
					## +
	dist[s] = 0  ### O(V) queue operation
	q = []
	q.append(s)
	while len(q)!=0:	## +
		u = q.pop()
		for v in g.E[u]:  #### o(2E) = O(E)
			if dist[v] == float("inf"):
				q.append(v)			#### = O(|V|+|E|)
				dist[v] = dist[u] + 1
	return dist