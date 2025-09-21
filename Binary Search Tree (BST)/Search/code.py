class TreeNode:
    def __init__(self,elem,l=None,r=None):
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
        temp = TreeNode(val)
        return temp
    if val < root.elem:
        root.left = insert(root.left,val)
    elif val > root.elem:
        root.right = insert(root.right,val)
    return root

def search(root,key):
    if root is None:
        return False
    if root.elem == key:
        return True  
    elif key > root.elem:
        return search(root.right,key)
    else:
        return search(root.left,key)
    






#Driver Code
root = TreeNode(10)


insert(root,5)
insert(root,11)
insert(root,8)
insert(root,40)

key = int(input("Enter key: "))
if search(root, key):
    print("Found")
else:
    print("Not found")



InOrder(root)