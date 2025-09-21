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


root = Tree_creation()


def DiffSum(root):
    def helper(root,level=0):
        global sumN
        
        
        if root is None:
            return 
        if level%2 == 0:
            sumN+=root.value
        elif level%2!=0:
            sumN-=root.value 
        helper(root.lchild,level+1)
        helper(root.rchild,level+1)
    global sumN 
    sumN = 0
    helper(root)
    return sumN 


print(DiffSum(root))