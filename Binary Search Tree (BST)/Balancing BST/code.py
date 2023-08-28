class TreeNode:
    def __init__(self,elem,l,r):
        self.elem = elem
        self.left = l 
        self.right = r
def PreOrder(root):
    if root != None:
        print(root.elem,end=' -> ')
        PreOrder(root.left)
        PreOrder(root.right)
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


lst = [40,50,70,90,95,99]
root = TreeNode(lst[0],None,None)
for i in range(1,len(lst)):
    insert(root,lst[i])

#Balancing The tree 

def PushTreeNodes(root,lst):
    if root!=None:
        PushTreeNodes(root.left,lst)
        lst.append(root.elem)
        PushTreeNodes(root.right,lst)

def BalanceBST(lst,start,end):
    if start > end:
        return None
    mid = (start+end)//2 
    root = TreeNode(lst[mid],None,None)

    root.left = BalanceBST(lst, start, mid-1)
    root.right = BalanceBST(lst, mid+1, end)
    return root

print("Unbalanced tree:")
PreOrder(root)

lst=[]
PushTreeNodes(root,lst)

Balanced_tree_root = BalanceBST(lst, 0, len(lst)-1)
print('\nBalanced Tree:')
PreOrder(Balanced_tree_root)


