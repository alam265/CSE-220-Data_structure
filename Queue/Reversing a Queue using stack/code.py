class Node:
    def __init__(self,val,next):
        self.elem = val 
        self.next =next 

class Stack:
    def __init__(self):
        self.top = None 

    def push(self,val):
        if self.top == None:
            self.top = Node(val,None)

        else:
            newNode = Node(val,None)
            newNode.next = self.top 
            self.top = newNode
    
    def pop(self):
        if self.top == None:
            return "Stack is Empty"
        else:
            x = self.top 
            self.top = self.top.next 
            return x 
        
    def peek(self):
        if self.top == None:
            return "Empty Stack"
        else:
            return self.top.elem 
    def isEmpty(self):
        if self.top == None:
            return True 
        return False
        

    def display(self):
        while self.top != None:
            print(self.top.elem,end=' ')
            self.top = self.top.next 
    def stk_ref(self):
        return self.top 


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
    def isEmpty(self):
        if self.front == None:
            return True 
        False 

    def Q_ref(self):
        return self.front 


def Display(ref):
    p = ref 
    while p!=None:
        print(p.elem,end=' ')
        p = p.next 




def reverse(Qu):
    stk = Stack()
    while not  Qu.isEmpty():
        stk.push(Qu.dequeue())

    while not stk.isEmpty():
        Qu.enqueue(stk.pop())
    return Qu.front 
    
    

Q = Queue()    
Q.enqueue(1)
Q.enqueue(3)
Q.enqueue(5)
Q.enqueue(7)
Q.enqueue(9)


 
Q.display()

reverse(Q)

Q.display()

        



    
        

    



