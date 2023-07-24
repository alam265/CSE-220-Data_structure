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
            x = self.front.elem 
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




Q = Queue()

Q.enqueue(12)
Q.enqueue(1)
Q.enqueue(23)
Q.enqueue(2)

Q.dequeue()

Q.display()