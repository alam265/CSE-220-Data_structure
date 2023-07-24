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
            x = self.top 
            self.top = self.top.next 
            return x 
        
    def Peek(self):
        if self.top == None:
            return "Empty Stack"
        else:
            return self.top.elem 
        

    def display(self):
        while self.top != None:
            print(self.top.elem,end=' ')
            self.top = self.top.next 


    
st = Stack() 

arr=[1,3,5,7,9]
for i in range(len(arr)):
    st.Push(arr[i])

st.Push(100)
st.Pop()
print(st.Peek())

st.display()











