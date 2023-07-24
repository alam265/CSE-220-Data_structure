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
            x = self.top.elem 
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
        else:
            return False 
    


stk = Stack()

def isOperand(ch):
    if ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch=='^' or ch== '(' or ch == ')':
        return False
    return True 

def outStackPrecedance(ch):
    if ch == '+' or ch=='-':
        return 1 
    elif ch == '*' or ch == '/':
        return 3 
    elif ch == '^' :
        return 6 
    elif ch == '(':
        return 7 
    elif ch == ')':
        return 0
    return -1 
def InStackPrecedance(ch):
    if ch == '+' or ch=='-':
        return 2 
    elif ch == '*' or ch == '/':
        return 4 
    elif ch == '^' :
        return 5
    elif ch == '(':
        return 0
    return -1 

def Infix_To_Postfix(infix):
    postfix = ' '
    i = 0

    while i < len(infix):
        if isOperand(infix[i]):
            postfix += infix[i]
            i+=1
        else:
            if   outStackPrecedance(infix[i]) > InStackPrecedance(stk.peek()):
                stk.push(infix[i])
                i+=1
            elif outStackPrecedance(infix[i]) == InStackPrecedance(stk.peek()):
                stk.pop()              
            else:
                postfix += stk.pop()
                

    while not  stk.isEmpty() and stk.peek() != ')':
        postfix += stk.pop()

    return postfix




print(Infix_To_Postfix("((a+b)*c)-d^e^f"))


            




    
    

