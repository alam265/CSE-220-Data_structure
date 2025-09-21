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

def minimumNode(a,b):
    return a if a.elem < b.elem else b 

def findMinNode(head):
    if head.next == None:
        return head 
    minRest = findMinNode(head.next)
    return minimumNode(head,minRest)

def swap(a , b):
    a.elem,b.elem = b.elem,a.elem 


def SelectionSort(head):
    if head == None or head.next ==  None:
        return 
    else:
        minNode = findMinNode(head)
        swap(head, minNode)
        SelectionSort(head.next)
    return head 

def display(head):
    p = head 
    while p:
        print(p.elem,end=' ')
        p = p.next 

LL = Singly_Linked_List()
LL = LL.creation([1,6,3,9,2,0,12,67,43,2])

SorteLL = SelectionSort(LL)

display(SorteLL)