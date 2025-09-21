class Node:
    def __init__(self,value,next):
        self.value = value 
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def creation(self,arr):
        self.head  = Node(arr[0],None)
        self.tail = self.head 

        for i in range(1,len(arr)):
            n = Node(arr[i],None)
            self.tail.next = n
            self.tail = self.tail.next 
    def Update(self,idx,value):
        p = self.head 
        c = 0
        f = False
        while p!=None:
            if c == idx:
                p.value = value
                f = True
            c +=1 
            p = p.next 
        if f==True:
            print('Value Updated Successfully')
        else:
            print('Invalid Syntax')

    def iteration(self):
        p = self.head 
        while p!= None:
            print(p.value,end=' ')
            p = p.next 


SLL = LinkedList()

SLL.creation([1,3,5,7,9,11])
SLL.Update(2,4)
SLL.iteration()