class Node:
    def __init__(self,value,next):
        self.elem = value
        self.next = next 

class Circular_Linked_list:
    def __init__(self):
        self.dh = None 
        self.tail = None 
    
    def creation(self,arr):
        self.dh = Node(None,None)
        self.dh.next = self.dh
        tail = self.dh

        for i in range(len(arr)):
            n = Node(arr[i],None)
            n.next = self.dh
            tail.next = n
            tail = n 
    def iteration(self):
        p = self.dh
        while p:
            print(p.elem,end=' ')
            p = p.next 
        
    def reverse(self):
        last = self.dh.next 

        r =None
        q=None 
        p = self.dh.next 

        while p!=self.dh:
            r = q 
            q = p
            p = p.next 
            q.next = r 
        self.dh.next = q 
        last.next = self.dh



CLL = Circular_Linked_list()
CLL.creation([1,2,3,4,5,6])
CLL.reverse()
CLL.iteration()
    