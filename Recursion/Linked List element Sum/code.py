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

def Sum_elem(head):
    if head.next == None:
        return head.elem
    return head.elem + Sum_elem(head.next)




LL = Singly_Linked_List()

LL= LL.creation([1,3,5,7,9])

print(Sum_elem(LL))
