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
    while p:
        print(p.elem,end=' ')
        p = p.next 
def length(head):
    p = head
    c=0
    while p:
        c+=1
        p = p.next 
    return c 

def swap_nodes_value(head,k):
    p1 = head 
    p2 = head 

    for i in range(1,k):
        p1 = p1.next 
    for j in range(length(head)-k):
        p2 = p2.next 

    temp = p1.elem
    p1.elem = p2.elem
    p2.elem = temp 




LL = Creation([1,2,3,4,5])

iteration(LL)

print('---------------')

swap_nodes_value(LL,2)

iteration(LL)