class Node:
    def __init__(self,val=None,next=None):
        self.elem = val 
        self.next = next 


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
            x = self.top 
            self.top = self.top.next 
            return x 
        
    def isEmpty(self):
        if self.top == None:
            return True 
        else:
            return False 
    def peek(self):
        return self.top.elem 

stk = Stack()

def isBalance(st):
    for i in range(len(st)):
        if st[i] == '(' or st[i]=='[' or st[i] == '{':
            stk.Push(st[i])
        elif st[i] == ')' :
            if stk.isEmpty():
                return False
            elif stk.peek()=='(':
                stk.Pop()
        elif st[i] == '}' :
            if stk.isEmpty():
                return False
            elif stk.peek() == '{':
                stk.Pop()
        elif st[i] == ']' :
            if stk.isEmpty():
                return False
            elif stk.peek()=='[':
                stk.Pop()
    if stk.isEmpty():
        return True 
    return False     


print(isBalance('([A+B]-C)/{D*E}+[2*[(2A+5){5B}]-{7C-9AB}]'))