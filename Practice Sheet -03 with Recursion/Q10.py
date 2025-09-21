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

def delete_alternate_nodes(head):
    if head is None or head.next is None :
        return 
    
    head.next = head.next.next
    delete_alternate_nodes(head.next)
    
    return head

 

    

#LL = Creation([10,20,30,40,50])
LL = Creation([1,2,3,4,5,6])
delete_alternate_nodes(LL)

iteration(LL)