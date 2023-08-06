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




def length(head):
    p = head 
    c =0
    while p!=None:
        c+=1 
        p = p.next 
    return c

def value_from_last(head,N):
    l = length(head)
    if N == l:
        return head.elem 
    else:
        return value_from_last(head.next, N)
     

     






LL = Creation([10,20,30,40,50])

print(value_from_last(LL,3))