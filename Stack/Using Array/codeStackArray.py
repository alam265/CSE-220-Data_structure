import numpy as np 

class Stack:
    def __init__(self):
        self.top = -1 

    def creation(self,size):
        self.arr = np.zeros(size,dtype=int)
        self.size = size 


    def Display(self):
        for i in range(self.top+1):
            print(self.arr[i],end=' ')

    def push(self,value):
        if self.top == self.size-1:
            print('Stack Overflow')
        else:
            self.top += 1
            self.arr[self.top] = value 
    def pop(self):
        if self.top == -1:
            return "Stack Underflow"
        else:
            x = self.arr[self.top]
            self.top -= 1
        return x 
    
    def peak(self):

        return self.arr[self.top]
        
        
    

st =Stack()
st.creation(5)
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st.pop()
st.push(0)

print(st.peak())

st.Display()

            








