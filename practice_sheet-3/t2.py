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
    p1 = head1
    p2 = head2 

    head = None
    tail = None
     

    while p1 and p2 :
        if p1.elem == p2.elem :
            n = Node(p1.elem,None)
            if head == None:
                head = n
                tail = head 
            else:
                tail.next = n
                tail = tail.next 
            p1 = p1.next
            p2 = p2.next 

        else:
            if p1.elem < p2.elem :
                p1 = p1.next 
            else:
                p2 = p2.next 

    return head 







LL1 = Creation([1,2,3,4,5])
LL2 = Creation([2,4,6,8])

Intersecting_LL = Intersection(LL1,LL2)

iteration(Intersecting_LL)
