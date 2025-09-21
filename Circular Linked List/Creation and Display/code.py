class Node:
    def __init__(self,value,next):
        self.elem = value 
        self.next = next 


def creation(arr):
    head = Node(arr[0],None)
    tail = head

    for i in range(1,len(arr)):
        n = Node(arr[i],None)
        n.next = head
        tail.next = n
        tail = n 
    return head 



def iteration(head):
    p = head
    while p.next!=head: 
        print(p.elem,end=' ')
        p = p.next 
    print(p.elem)
        



CLL = creation([1,2,3,4,5])

iteration(CLL)