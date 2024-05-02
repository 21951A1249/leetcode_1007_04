class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.hd=0
def level_order(root,order='TB'):
    level_map={}
    q=[(root,0)]
    while q:
        Node,lvl=q.pop(0)
        if lvl not in level_map:
            level_map[lvl]=[]
        level_map[lvl].append(Node.data)
        if Node.left:
            q.append((Node.left,lvl+1))
        if Node.right:
            q.append((Node.right,lvl+1))
    if order=="TB":
        print("level order traversal")
        for lvl in level_map:
            print(level_map[lvl],end=",")
    elif order=="BT":
        print("\nreverse level order traversal")
        for lvl in sorted(level_map,reverse=True):
            print(level_map[lvl],end=",")
            
root=Node('A')
root.left=Node('B')
root.right=Node('C')
root.left.left=Node('D')
root.left.right=Node('E')
root.right.left=Node('F')
root.right.right=Node('G')
level_order(root,"BT")

