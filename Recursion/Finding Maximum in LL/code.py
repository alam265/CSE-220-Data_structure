class Node:
    def __init__(self,elem,next):
        self.elem = elem 
        self.next = next 

class Singly_Linked_List:
    def __init__(self):
        self.head = None 
        
    def creation(self,arr):
        self.head = Node(arr[0],None)
        tail = self.head

        for i in range(1,len(arr)):
            newNode = Node(arr[i],None)
            tail.next = newNode
            tail = newNode 
        return self.head


def maximum(a,b):
    return a if a>=b else b 


def FindMax(head):
    if head.next == None:
        return head.elem 
    else:
        Rest = FindMax(head.next)
        return maximum(head.elem,Rest)
    



LL = Singly_Linked_List()

LL= LL.creation([1,30,5,7,9])


print(FindMax(LL))


