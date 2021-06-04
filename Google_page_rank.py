import networkx as nx
g= nx.DiGraph()
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_node(6)

g.add_edge(2,1)
g.add_edge(1,3)
g.add_edge(3,2)
g.add_edge(3,4)
g.add_edge(3,5)
g.add_edge(4,6)¬
g.add_edge(6,5)

nx.draw_networkx(g)

pr=nx.pagerank(g,alpha=0.85)
print(pr)


