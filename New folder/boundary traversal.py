"""boundary traversal of a binary tree involves traversing
the boundary nodes of the tree in an anti clockwise direction
starting from the root node.
it includes the left boundary(excluding the leaf nodes),
the leaf nodes from left to right,
and the right boundary (excluding the leaf nodes) in that order """
class treenode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def print_left_boundary(root):
    if root:
        if root.left:
            print(root.value,end=" ")
            print_left_boundary(root.left)
        elif root.right:
            print(root.value,end=" ")
            print_left_boundary(root.right)
def print_leaves(root):
    if root:
        print_leaves(root.left)
        if root.left is None and root.right is None:
            print(root.value,end=" ")
        print_leaves(root.right)
def print_right_boundary(root):
    if root:
        if root.right:
            print_root_boundary(root.right)
            print(root.value,end=" ")
        elif root.left:
            print_right_boundary(root.left)
            print(root.value,end=" ")
            


            
