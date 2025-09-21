class Node:
    def __init__(self,val,next,prev):
        self.elem = val 
        self.next = next 
        self.prev = prev 

class Circular_Doubly_Linked_list:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def creation(self,arr):
        self.head = Node(arr[0],self.head,self.head)
        tail = self.head 

        for i in range(1,len(arr)):
            temp = Node(arr[i], self.head, tail)
            self.head.prev = temp
            tail.next = temp 
            tail = temp 
        self.tail = tail
    def Forward_iteration(self):
        p = self.head.next

        print(self.head.elem, end=' ')
        while p!=self.head:
            print(p.elem,end=' ')
            p = p.next 

        
    def Backward_iteration(self):
        p = self.tail
        print(p.elem,end=' ')
        while p!=self.head:
            print(p.elem,end=' ')
            p = p.prev


    def reverse(self):
        last = self.head 
        last1 = self.head.next 

        p = self.head.next 
        r = None 
        q = None 

        while p!=self.head:
            r = q
            q = p
            p = p.next 
            q.next = r
            q.prev = p 
        last1.next = last
        last.prev = last1
        last.next = q
        self.head = q


CDLL = Circular_Doubly_Linked_list()
CDLL.creation([1,2,3,4,5,6,7])
CDLL.reverse()
CDLL.Forward_iteration()