class Node:
    def __init__(self,value,next):
        self.elem = value
        self.next = next 

class Circular_LL:
    def __init__(self):
        self.head = None 

    def creation(self,arr):
        self.head = Node(arr[0],None)
        self.head.next = self.head 
        tail = self.head
        for i in range(1,len(arr)):
            temp = Node(arr[i],None)
            temp.next = self.head
            tail.next = temp
            tail = temp 


    def iteration(self):
        p = self.head.next 
        print(self.head.elem,end=' ')
        while p!=self.head:
            print(p.elem,end=' ')
            p = p.next 
        
    def reverse(self):
        p = self.head.next 
        q=None 
        r=None
        
        last = self.head
        last1 = self.head.next

        while p!=self.head:
            r= q
            q = p
            p = p.next 
            q.next = r 

        last.next = q
        last1.next = last
        self.head = q
        




CLL = Circular_LL()
CLL.creation([1,2,3,4,5,6])
CLL.reverse()
CLL.iteration()