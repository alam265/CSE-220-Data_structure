class Node:
    def __init__(self,value,next,prev):
        self.elem = value 
        self.next = next 
        self.prev = prev

class Circular_Doubly_Linked_list:
    def __init__(self):
        self.dh = None 
        self.tail = None 

    def creation(self,arr):
        self.dh = Node(None,None,None)
        self.dh.next = self.dh 
        self.dh.prev = self.dh 
        tail = self.dh 

        for i in range(len(arr)):
            temp = Node(arr[i],self.dh,tail)
            tail.next = temp
            self.dh.prev = temp
            tail = temp 

    def Forward_iteration(self):
        p = self.dh.next 

        while p!=self.dh:
            print(p.elem,end=' ')
            p = p.next 

    def Reverse(self):
        p = self.dh.next 
        last = self.dh.next 

        r = None 
        q = None 
        
        while p!=self.dh:
            r = q
            q = p
            p = p.next 
            q.next = r
            q.prev = p
        self.dh.next = q 
        q.prev = self.dh 
        self.dh.prev = last 
        last.next = self.dh 





CDLL = Circular_Doubly_Linked_list()
CDLL.creation([1,2,3,4,5,6,7])
CDLL.Reverse()
CDLL.Forward_iteration()
