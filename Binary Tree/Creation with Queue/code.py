class TreeNode:
    def __init__(self,val,lc,rc):
        self.value = val 
        self.lchild = lc
        self.rchild = rc 

class Node:
    def __init__(self,ref,next):
        self.ref = ref 
         
        self.next = next 

class Queue:
    def __init__(self):
        self.front = None 
        self.back = None 

    def enqueue(self,ref):
        if self.front == None:
            self.front = Node(ref,None)
            self.back = self.front 
        else:
            newNode = Node(ref,None)
            self.back.next = newNode
            self.back = newNode

    def dequeue(self):
        if self.front == None:
            return 'Empty Queue'
        else:
            x = self.front 
            self.front = self.front.next 
            return x.ref 
        
    def peek(self):
        if self.front == None:
            return 'Queue is Empty'
        return self.front.elem 
    
    def display(self):
        p = self.front
        while p!=None:
            print(p.elem,end=' ')
            p = p.next 
    def isEmpty(self):
        if self.front == None:
            return True
        return False


def Tree_creation():
    q = Queue()
    v = int(input('Enter Root value:'))
    root = TreeNode(v,None,None)
    r =root
    q.enqueue(root)

    while not q.isEmpty():
        p = q.dequeue()
        x = int(input(f"Enter Left child of {p.value}: "))
        if x!=-1:
            temp = TreeNode(x,None,None)
            p.lchild = temp 
            q.enqueue(temp)

        x = int(input(f"Enter Right child of {p.value}: "))
        if x!=-1:
            temp = TreeNode(x,None,None)
            p.rchild = temp 
            q.enqueue(temp)
    return r


def preOrder(root):
    r=root
    if r!=None:
        print(r.value,end=' ')
        preOrder(r.lchild)
        preOrder(r.rchild)

def inorder(root):
    if root!=None:
        inorder(root.lchild)
        print(root.value,end=' ')
        inorder(root.rchild)
        

def postorder(root):
    if root!=None:
        postorder(root.lchild)
        postorder(root.rchild)
        print(root.value,end=' ')


def CountNodes(r):
    if r == None:
        return 0
    x = CountNodes(r.lchild)
    y = CountNodes(r.rchild)
    return x+y+1 

def Height(r):
    if r == None:
        return -1
    x = Height(r.lchild)
    y = Height(r.rchild)
    if x > y :
        return x+1
    else:
        return y+1 
    
def CountNode_of_Degree_two(r):
    if r == None:
        return 0 
    
    x = CountNode_of_Degree_two(r.lchild)
    y = CountNode_of_Degree_two(r.rchild)
    if r.lchild and r.rchild:
        return x + y + 1
    else:
        return x+y
    
def Count_leafs(r):
    if r == None:
        return 0
    
    x = Count_leafs(r.lchild)
    y = Count_leafs(r.rchild)
    
    if r.lchild == None and r.rchild == None:
        return x + y + 1 
    else:
        return x + y 



def depth(node,node_level,target_elem):
    if node == None:
        return 0 
    if node.value == target_elem:
        return node_level
    left = depth(node.lchild,node_level+1,target_elem)
    if left!=0:
        return left 
    right = depth(node.rchild,node_level+1, target_elem)
    return right 
 
#We can do it this way also
def get_level(root,target,level=0):
    if root is None:
        return 0 
    if root.value == target:
        return level 
    return get_level(root.lchild,target,level+1) + get_level(root.rchild,target,level+1)







tree = Tree_creation()


print("Printing in Preorder:")
preOrder(tree)

print("\nPrinting in Inorder:")
inorder(tree)

print("\nprinting postorder:")
postorder(tree)

print("\nNumber of Nodes:",CountNodes(tree))
print("Height of the tree:",Height(tree))
print("Nodes with degree two:",CountNode_of_Degree_two(tree))

print("Number of leafs:",Count_leafs(tree))

print("\nDepth of Node 4 is:",depth(tree,0,4))




