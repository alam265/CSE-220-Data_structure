import numpy as np 
class Queue:
    def __init__(self,size):
        self.size = size
        self.arr = np.zeros(size,dtype=int)
        self.front = 0 
        self.back = 0 

    def enqueue(self,elem):
        if (self.back+1)%self.size == self.front: 
            print('Queue is full')
        else:
            self.back = (self.back+1) % self.size 
            self.arr[self.back] = elem 

    def dequeue(self):
        if self.front  == self.back:
            return 'Queue is Empty'
        else:
            self.front = (self.front+1) % self.size 
            x = self.arr[self.front]
            return x 
        

    def isEmpty(self):
        if self.front==self.back:
            return True 
        return False 
    
    def display(self):
        for i in range(self.front+1,self.back+1):
            print(self.arr[i],end=' ')



cq = Queue(5)

cq.enqueue(1)  
cq.enqueue(12)  
cq.enqueue(15)  
cq.enqueue(19)  
cq.dequeue()



cq.display()