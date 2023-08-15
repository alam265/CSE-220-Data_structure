class Node:
    def __init__(self,elem):
        self.elem = elem 
        self.left =None
        self.right = None 

def create_Tree(arr,i,n):
    temp=None
    if i < n:
        if arr[i] != None:
            temp = Node(arr[i])
            temp.left = create_Tree(arr,2*i,n)
            temp.right = create_Tree(arr, 2*i+1,n)

    return temp

def preOrderPrint(root):
    if root!=None:
        print(root.elem,end=' ')
        preOrderPrint(root.left)
        preOrderPrint(root.right)





arr = [None,'A','B','C','D','E','F','G','H',None,None,None,'I','J',None,'K']
tree = create_Tree(arr,1,len(arr))

preOrderPrint(tree)


array = [None]*16
def array_from_tree(p,i):
    if p == None:
        return 
    array[i] = p.elem
    array_from_tree(p.left,2*i)
    array_from_tree(p.right,2*i+1)


array_from_tree(tree,1)
print("\nArray From tree:")
print(array)


