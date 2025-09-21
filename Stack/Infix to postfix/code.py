class Node:
    def __init__(self,val,next):
        self.elem = val 
        self.next =next 

class Stack:
    def __init__(self):
        self.top = None 

    def Push(self,val):
        if self.top == None:
            self.top = Node(val,None)

        else:
            newNode = Node(val,None)
            newNode.next = self.top 
            self.top = newNode
    
    def Pop(self):
        if self.top == None:
            return "Stack is Empty"
        else:
            x = self.top.elem 
            self.top = self.top.next 
            return x 
        
    def Peek(self):
        if self.top == None:
            return "Empty Stack"
        else:
            return self.top.elem 
        

    def isEmpty(self):
        if self.top == None:
            return True 
        else:
            return False 


stk = Stack()

def isOperand(ch):
    if ch == '+' or ch == '-' or ch == '*' or ch == '/':
        return False  
    else:
        return True 

def precedence(ch):
    if ch == '+' or ch == '-':
        return 1 
    elif ch == '*' or ch == '/':
        return 2 
    return 0

def convert(infix):
    postfix = ''
    i = 0
    

    while i < len(infix):
        if isOperand(infix[i]):
            postfix += infix[i]
            i+=1
        else:
            if precedence(infix[i]) > precedence(stk.Peek()) :
                stk.Push(infix[i])
                i+=1
            else:
                postfix += stk.Pop()
    
    while stk.isEmpty()!=True :
        postfix += stk.Pop()

    return postfix


print(convert("a+b*c-d/c"))









