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


def identical_checker(head1,head2):
    while head1 and head2:
        if head1.elem != head2.elem:
            return 'Not Identical'
        head1 = head1.next 
        head2 = head2.next
    return 'Identical'



LL1 = Creation([1,2,3,4,5])
LL2 = Creation([1,2,3,4,5])


print(identical_checker(LL1,LL2))