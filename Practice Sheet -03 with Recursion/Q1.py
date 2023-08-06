class Node:
    def __init__(self,value,next):
        self.elem = value
        self.next = next 


def Creation(arr):
    head = Node(arr[0],None)
    tail = head 
    for i in range(1,len(arr)):
        n = Node(arr[i],None)
        tail.next = n 
        tail = n
    return head 
def iteration(h):
    p = h 
    while p!=None:
        print(p.elem,end=' -> ')
        p = p.next 
    print(None,end='')




def last_to_front(head):
    p = head 
    q = None 
    def moving_pointers(p,q):
        if p.next == None:
            p.next = head 
            q.next = None 
            return p
        return moving_pointers(p.next, p)
    new_head = moving_pointers(head,None)
    return new_head 

arr=[1,3,5,7,9,11,13]
LL = Creation(arr)
iteration(LL)
print()
new_LL = last_to_front(LL)
iteration(new_LL)

