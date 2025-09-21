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

def Intersection(head1,head2):



    if head1 == None or head2 == None:
        return None
    elif head1.elem == head2.elem:
        new_Node = Node(head1.elem,None)
        new_Node.next = Intersection(head1.next,head2.next)
        return new_Node
    elif head1.elem < head2.elem :
        return Intersection(head1.next , head2)
    elif head1.elem > head2.elem:
        return Intersection(head1, head2.next)







LL1 = Creation([1,2,3,4,5])
LL2 = Creation([2,4,6,8])

Intersecting_LL = Intersection(LL1,LL2)

iteration(Intersecting_LL)
