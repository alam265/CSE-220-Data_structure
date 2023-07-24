class Node:
    def __init__(self,value,next,prev):
        self.elem = value 
        self.next = next 
        self.prev = prev 


class Doubly_Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def creation(self,arr):
        self.head = Node(arr[0],None,None)
        tail = self.head 

        for i in range(1,len(arr)):
            temp = Node(arr[i],None,None)
            tail.next = temp
            temp.prev = tail
            tail = temp 
        self.tail = tail

    def Forward_iteration(self):
        p = self.head
        while p:
            print(p.elem,end=' ')
            p = p.next

    def Backward_iteration(self):
        p = self.tail 

        while p :
            print(p.elem,end=' ')
            p = p.prev 


    def reverse(self):
        r = None 
        q = None 
        p = self.head

        while p!=None:
            r = q
            q = p
            p = p.next 
            q.next = r 
            q.prev = p 
        self.head = q

        




DLL = Doubly_Linked_list()
DLL.creation([1,2,3,4,5,6])
DLL.reverse()
DLL.Forward_iteration()






