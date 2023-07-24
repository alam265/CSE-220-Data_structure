class Node:
    def __init__(self,elem,next):
        self.elem = elem 
        self.next = next 
class Stack:
    def __init__(self):
        self.top =None 

    def push(self,elem):
        if self.top == None:
            self.top = Node(elem,None)
        else:
            newNode = Node(elem,None)
            newNode.next = self.top 
            self.top = newNode

    def pop(self):
        if self.top == None:
            return 'Stack is Empty'
        else:
            x = self.top.elem
            self.top = self.top.next 
            return x 
    def isEmpty(self):
        if self.top == None:
            return True 
        return False 
    def display(self):
        p = self.top 
        while p!=None:
            print(p.elem,end=' ')
            p = p.next





stk1 = Stack()
stk2 = Stack()
class Queue:
    def __init__(self):
        pass 

    def enqueue(self,elem):
        stk1.push(elem)

    def dequeue(self):
        if stk2.isEmpty():
            if stk1.isEmpty():
                return 'Queue is Empty'
            else:
                while not stk1.isEmpty():
                    stk2.push(stk1.pop())

        
            return stk2.pop()
        
    def display(self):
        stk2.display()




Q = Queue()

Q.enqueue(12)
Q.enqueue(15)
Q.enqueue(1)
Q.enqueue(129)
Q.enqueue(23)

print(Q.dequeue())


Q.display()
        
        





