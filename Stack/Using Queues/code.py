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



Q1 = Queue()
Q2 = Queue()

class Stack:
    def __init__(self):
        pass 
    def push(self,elem):
        Q1.enqueue(elem)

    def pop(self):
        for i in range(Q1.length()-1):
            Q2.enqueue(Q1.dequeue())

        last_elem = Q1.dequeue()
        while not Q2.isEmpty():
            Q1.enqueue(Q2.dequeue())
        return last_elem 

 

    def display(self):
        Q1.display()


stk = Stack()

stk.push(1)
stk.push(3)
stk.push(5)
stk.push(7)
stk.push(9)

print(stk.pop())


stk.display()

