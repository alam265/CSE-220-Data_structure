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
            return 'Queue Empty'
        else:
            x = self.front 
            self.front = self.front.next 
            return x.elem 
    def isEmpty(self):
        if self.front == None:
            return True 
        return False 
    
    def display(self):
        p = self.front 
        while p!=None:
            print(p.elem,end=' ')
            p = p.next 

    def length(self):
        c = 0
        p = self.front 
        while p!=None:
            c+=1
            p = p.next 
        return c 
    

Q =Queue()

class Stack:
    def __init__(self):
        pass 
    def push(self,elem):
        Q.enqueue(elem)

    def pop(self):
        for i in range(Q.length()-1):
            Q.enqueue(Q.dequeue())
        x = Q.dequeue()
        return x 
    
    def display(self):
        Q.display()


stk = Stack()

stk.push(12)
stk.push(1)
stk.push(3)
stk.push(56)

print(stk.pop())

stk.push(100)

stk.display()
