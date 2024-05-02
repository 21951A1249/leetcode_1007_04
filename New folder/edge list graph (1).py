edgelist=[('A','B',2),('B','D',4),('D','E',5),('C','E',1),('C','D',6),('A','C',3)]
tot=0
for edge in edgelist:
    tot+=edge[2]
print("total distance =",tot)
# to find number of nodes
v_set=set()
for edge in edgelist:
    v_set.add(edge[0])
    v_set.add(edge[1])
print("nodes =",v_set)
print("number of nodes",len(v_set))
# adjacency list
adj_list={v:[] for v in v_set}
for edge in edgelist:
    adj_list[edge[0]].append((edge[1],edge[2]))
    adj_list[edge[1]].append((edge[0],edge[2]))
print(" adjacency list =", adj_list)


