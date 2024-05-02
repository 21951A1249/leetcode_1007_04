class disjointset:
    def __init__(self,vertices):
        self.parent={v:v for v in vertices}
    def find_root(self,v):
        if v!=self.parent[v]:
            self.parent[v]=self.find_root(self.parent[v])
        return self.parent[v]
    def union(self,v1,v2):
        p1=self.find_root(v1)
        p2=self.find_root(v2)
        self.parent[p1]=p2
def distance(e):
    return e[2]
def kruskal(graph):
    obj=disjointset(graph['vertices'])
    edgelist=graph['edge']
    edgelist.sort(key=distance)
    mst=[]
    for edge in edgelist:
        u,v,w=edge
        r1=obj.find_root(u)
        r2=obj.find_root(v)
        if r1!=r2:
            obj.union(u,v)
            mst.append(edge)
    return mst
graph={ 'vertices':['A','B','C','D','E'],
'edge':[('A','B',3),('B','D',2),('D','E',7),('C','E',1),('C','D',5),('A','C',4)]
   }
mst=kruskal(graph)
print(mst)
tot=0
for edge in mst:
        tot+=edge[2]
print("Total distance =",tot)
    
