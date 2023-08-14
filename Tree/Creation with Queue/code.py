class TreeNode:
    def __init__(self,val,lc,rc):
        self.value = val 
        self.lchild = lc
        self.rchild = rc 

class Node:
    def __init__(self,elem,next):
        self.elem = elem 
        self.next = next 

class Queue:
    def __init__(self):
        self.front = None 
        self.back = None 

    def enqueue(self,elem):
        if self.front == None:
            self.front = Node(elem,None)
            self.back = self.front 
        else:
            newNode = Node(elem,None)
            self.back.next = newNode
            self.back = newNode

    def dequeue(self):
        if self.front == None:
            return 'Empty Queue'
        else:
            x = self.front 
            self.front = self.front.next 
            return x 
        
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
    root = TreeNode(v,0,0)
    q.enqueue(root)

    while not q.isEmpty():
        p = q.dequeue()
        x = int(input("Enter Left child: "))
        if x!=-1:
            temp = TreeNode(x,0,0)
            p.lchild = temp 
            q.enqueue(temp)

        x = int(input("Enter Right child: "))
        if x!=-1:
            temp = TreeNode(x,0,0)
            p.rchild = temp 
            q.enqueue(temp)


Tree_creation()




