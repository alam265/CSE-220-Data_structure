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

def contains(head,key):
    if head == None:
        return False
    elif head.elem == key:
        return True 
    return contains(head.next,key)


LL = Singly_Linked_List()
LL = LL.creation([1,2,3,4,5,6])

print(contains(LL,6))
