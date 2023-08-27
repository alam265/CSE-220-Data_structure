class TreeNode:
    def __init__(self,elem,l,r):
        self.elem = elem
        self.left = l 
        self.right = r
def InOrder(root):
    if root != None:
        InOrder(root.left)
        print(root.elem,end=' ')
        InOrder(root.right)

def insert(root,val):
    temp = None
    if root is None:
        temp = TreeNode(val ,None, None)
        return temp
    if val < root.elem:
        root.left = insert(root.left,val)
    elif val > root.elem:
        root.right = insert(root.right,val)
    return root


root = TreeNode(10,None,None)


insert(root,5)
insert(root,11)
insert(root,8)
insert(root,40)

InOrder(root)