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

def remove_LL(head):
    p=head

    while p.next!=None and p.next.next!=None:
        p.next = p.next.next 
        p = p.next 
    p.next = None


 

    

#LL = Creation([10,20,30,40,50])
LL = Creation([1,2,3,4,5,6])

remove_LL(LL)

iteration(LL)