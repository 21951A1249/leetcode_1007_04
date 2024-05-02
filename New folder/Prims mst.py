import heapq
def prims(graph):
    mst=[]
    adj_list={v:[] for v in graph['vertices']}
    for edge in graph['edge']:
        adj_list[edge[0]].append((edge[1],edge[2]))
        adj_list[edge[1]].append((edge[0],edge[2]))
    start='A'
    visited_set=set()
    visited_set.add(start)
    q=[(weight,start,dest) for dest,weight in adj_list[start]]
    while q:
        w,s,d=heapq.heappop(q)
        if d not in visited_set:
            visited_set.add(d)
            mst.append((w,s,d))
            for neighbour,w in adj_list[d]:
                if neighbour not in visited_set:
                    heapq.heappush(q,(w,d,neighbour))
    print(mst)
    tot=0
    for edge in mst:
        tot+=edge[0]
    print("Total distance =",tot)
    
graph={ 'vertices':['A','B','C','D','E'],
'edge':[('A','B',2),('B','D',4),('D','E',5),('C','E',1),('C','D',6),('A','C',3)]
   }
prims(graph)
