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
        print(p.elem,end=' ')
        p = p.next 


def reverse(p,q):
    if p != None:
        reverse(p.next,p)
        p.next = q 
    else:
        head = q
        return head
    
        





arr=[1,3,5,7,9,11,13]
LL = Creation(arr)
#iteration(LL)
print()

LL1=reverse(LL,None)
iteration(LL1)



