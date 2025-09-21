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


lst = [70,50,40,90,20,60,55]
root = TreeNode(lst[0],None,None)
for i in range(1,len(lst)):
    insert(root,lst[i])


InOrder(root)

def InOrder_Successor(root):
    p = root 
    while p.left:
        p = p.left
    return p 

def deletNode(root,key):
    if root is None:
        return 
    if key < root.elem:
        root.left = deletNode(root.left,key)
    elif key > root.elem:
        root.right = deletNode(root.right,key)
    else:
        if root.left is None:
            temp = root.right 
            root = None
            return temp 
        elif root.right is None:
            temp = root.left 
            root = None 
            return temp 
        temp = InOrder_Successor(root.right)
        root.elem = temp.elem 

        root.right = deletNode(root.right,temp.elem)

    return root 

deletNode(root,20)
deletNode(root,70)

print()
InOrder(root)