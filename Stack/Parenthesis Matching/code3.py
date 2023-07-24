class Node:
    def __init__(self,val,next):
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
        
    def isBalance(self,st):
        for i in st:
            if i == "(":
                stk.Push('(')
            elif i == ')':
                if stk.isEmpty():
                    return False
                else:
                    stk.Pop()
        if stk.isEmpty():
            return True 
        else:
            return False

        
    

        

stk = Stack()

print(stk.isBalance("(a(a+b)*(c+d))"))
   
