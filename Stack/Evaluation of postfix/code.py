class Node:
    def __init__(self,val,next):
        self.elem = val 
        self.next = next 

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
            return 'Stack Empty'
        else:
            topNode = self.top 
            self.top = self.top.next 
            topNode.next = None 
            return topNode.elem 
            
        
    def peek(self):
        if self.top == None:
            return 'Stack empty'
        return self.top 
    


stk = Stack()

def isOperand(ch):
    if ch == '+' or ch=='-' or ch == '*' or ch == '/':
        return False 
    return True

def Evaluation(postfix):
    for i in range(len(postfix)):
        if isOperand(postfix[i]):
            stk.push(int(postfix[i]))
        else:
            x2 = stk.pop()
            x1 = stk.pop()
            if postfix[i] == '+':
                r = x1 + x2 
                stk.push(r)
            elif postfix[i] == '-':
                r = x1 - x2 
                stk.push(r)
            elif postfix[i] == '*':
                r = x1 * x2 
                stk.push(r)
            elif postfix[i] == '/':
                r = x1 // x2 
                stk.push(r)
    return r 


print(Evaluation("35*62/+4-"))
            