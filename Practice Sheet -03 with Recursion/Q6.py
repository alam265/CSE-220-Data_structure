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
    c = 0
    while p!=None:
        c +=1 
        p = p.next 
    return c 


def middle_elem(head):

    def slow_fast(slow,fast):
        if fast == None or fast.next == None:
            return slow.elem
        return slow_fast(slow.next,fast.next.next)
    middle = slow_fast(head,head)
    return middle
    


LL = Creation([10,20,30,40,50])


print(middle_elem(LL))