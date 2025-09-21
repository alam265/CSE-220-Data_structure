class Node:
    def __init__(self, elem, next):
        self.elem = elem
        self.next = next


def Creation(arr):
    head = Node(arr[0],None)
    tail = head 
    for i in range(1,len(arr)):
        n = Node(arr[i],None)
        tail.next = n 
        tail = tail.next 
    return head 

def iteration(head):
    p = head 
    while p!=None:
        print(p.elem,end=' ')
        p = p.next 


def last_to_fast(head):
    p = head 
    while p.next.next!=None:
        p = p.next 
    second_last = p
    last = p.next 
    last.next = head 
    head = last 
    second_last.next = None 
     

    return head 

arr = [1,2,3,4,5]

Creation(arr)
last_to_fast(Creation(arr))
iteration(last_to_fast(Creation(arr)))