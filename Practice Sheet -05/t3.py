class Node:
    def __init__(self,val,next):
        self.elem = val 
        self.next = next 

class Stack:
    def __init__(self):
        self.top = None 

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
            popNode = self.top
            self.top = popNode.next 
            popNode.next = None
            return popNode.elem
    def peek(self):
        return self.top.elem 
    def isEmpty(self):
        if self.top == None:
            return True 
        return False 
    

stk = Stack()

def reverseString(string):
    
    reversed_str = ''
    for i in range(len(string)):
        stk.push(string[i])


    while not stk.isEmpty():
        reversed_str+=stk.pop()

    return reversed_str 


print(reverseString('CSE220'))