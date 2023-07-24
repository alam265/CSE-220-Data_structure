class Node:
    def __init__(self,value,next,prev):
        self.elem = value
        self.next = next 
        self.prev = prev 

class Circular_Doubly_Linked_List:
    def __init__(self):
        self.dh = None 
        self.tail = None 

    def Creation(self,arr):
        self.dh = Node(None,None,None)
        self.dh.next = self.dh 
        self.dh.prev = self.dh 
        self.tail = self.dh 

        for i in range(len(arr)):
            temp = Node(arr[i],None,None)
            temp.next = self.dh 
            self.dh.prev = temp
            temp.prev = self.tail
            self.tail.next = temp 
            self.tail = self.tail.next
    def Forward_iteration(self):
        p = self.dh.next

        while p!=self.dh:
            print(p.elem,end=' ')
            p = p.next 

        
    def Backward_iteration(self):
        p = self.tail

        while p!=self.dh:
            print(p.elem,end=' ')
            p = p.prev
    def Insert(self,value,idx):
        if idx == 0:
            temp  = Node(value,None,None)
            temp.next = self.dh.next
            self.dh.next.prev = temp 
            self.dh.next = temp 
            temp.prev = self.dh 
        else:
            temp = Node(value,None,None)
            p = self.dh 
            for i in range(idx):
                p = p.next 
            q = p.next 
            temp.next = q
            q.prev = temp
            p.next = temp 
            temp.prev = p 


    def Delete(self,idx):
            p = self.dh
            for i in range(idx):
                p = p.next 
            q = p.next.next
            p.next = q 
            q.prev = p 










    


CDLL = Circular_Doubly_Linked_List()

CDLL.Creation([1,3,5,7,9,11])
#CDLL.Forward_iteration()
#CDLL.Backward_iteration()

#CDLL.Insert(100,2)
CDLL.Delete(3)
CDLL.Forward_iteration()

