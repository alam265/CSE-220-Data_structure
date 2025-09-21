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
    def swap_elem(head,k,l,idx):
        if head == None:
            return 
        if idx == k:
            global first_elem 
            first_elem = head.elem
        if idx == l - k + 1:
            first_elem, head.elem = head.elem, first_elem 

        swap_elem(head.next,k,l,idx+1)


    first_elem = None
    swap_elem(head,k,length(head),1)
    

    

        





LL = Creation([1,2,3,4,5])

iteration(LL)

print('---------------')

swap_nodes_value(LL,2)

iteration(LL)