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


def reverse(q,p):
    if p != None:
        reverse(p,p.next)
        p.next = q 
    else:
        head = q
    
        
    
        





arr=[1,3,5,7,9,11,13]
LL = Creation(arr)
#iteration(LL)
print()
reverse(None,LL)
iteration(LL)



