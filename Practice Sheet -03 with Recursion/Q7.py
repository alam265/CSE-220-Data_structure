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
def LL_with_Loop(head):
    p = head

    last = None
    first = head
    third = head.next.next 

    while p.next :
        p = p.next 
    last = p 
    last.next = third 

    return head

def iteration(head):
    p = head 
    while p!=None:
        print(p.elem,end=' ')
        p = p.next



def Delect_Loop(head):
    def Slow_fast(slow,fast):
        if fast == None or fast.next == None:
            return False
        elif slow == fast:
            return True 
        else:
            return Slow_fast(slow.next,fast.next.next)
    x = Slow_fast(head,head.next)
    return x 


LL = Creation([1,2,3,4,5])

LL_with_Loop(LL)


print(Delect_Loop(LL))
