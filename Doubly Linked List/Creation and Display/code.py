class Node:
    def __init__(self,value,next,prev):
        self.elem = value 
        self.next = next 
        self.prev = prev 


def creation(arr):
    head = Node(arr[0],None,None)
    tail = head 
    for i in range(1,len(arr)):
        n = Node(arr[i],None,None)
        tail.next = n
        n.prev = tail  
        tail = n
    return head 


def iteration(head):
    p = head 
    while p:
        print(p.elem,end=' ')
        p = p.next















DLL = creation([1,2,3,4,56])

iteration(DLL)