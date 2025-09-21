import numpy as np 
class Queue:
    def __init__(self,size):
        self.size = size
        self.arr = np.zeros(size,dtype=int)
        self.front = -1
        self.back = -1 


    def enqueue(self,elem):
        self.back+=1
        if self.size == self.back:
            print('Queue Overflow')
        else:
            self.arr[self.back] = elem

    def dequeue(self):
        self.front +=1
        if self.front == self.size:
            print('Underflow')
        else:
            x = self.arr[self.front]

            return x 
    def peek(self):
        return self.arr[0] 
        
    def display(self):
        for i in range(self.front+1,self.size):
            print(self.arr[i],end=' ')






Q = Queue(4)

Q.enqueue(2)
Q.enqueue(5)
Q.enqueue(9)
#Q.enqueue(10)
#Q.enqueue(15)
print(Q.peek())


Q.display()

        
