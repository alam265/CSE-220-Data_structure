class Node:
    def __init__(self,value,next,prev):
        self.elem = value 
        self.next = next 
        self.prev = prev 

class Doubly_Linked_list:
    def __init__(self):
        self.head = None
        self.tail=None

    def creation(self,arr):
        self.head = Node(arr[0],None,None)
        self.tail = self.head 
        for i in range(1,len(arr)):
            n = Node(arr[i],None,None)
            self.tail.next = n
            n.prev = self.tail  
            self.tail = n
        return self.head 


    def Forward_iteration(self):
        p = self.head 
        while p:
            print(p.elem,end=' ')
            p = p.next

    def  Backword_iteration(self):
        p = self.tail 
        while p:
            print(p.elem,end=' ')
            p = p.prev 


    def Insertion(self,value,idx):
        p = self.head
        if idx==0:
            temp = Node(value,None,None)
            temp.next = self.head 
            self.head.prev = temp
            self.head = temp 
        else:
            temp = Node(value,None,None)
            for i in range(idx-1):
                p = p.next 
            q = p.next 
            temp.next = q
            q.prev = temp
            p.next = temp 
            temp.prev = p 

    def Deletation(self,idx):
        p = self.head
        if idx==0:
            self.head = self.head.next 
        else:
            for i in range(idx-1):
                p = p.next 
            q = p.next.next 
            p.next = q
            q.prev = p 
















DLL = Doubly_Linked_list()
DLL.creation([1,2,3,4,5,6])
DLL.Insertion(100,2)
DLL.Deletation(3)
DLL.Forward_iteration()






