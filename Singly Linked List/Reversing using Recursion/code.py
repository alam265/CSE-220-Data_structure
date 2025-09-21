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

#global head
#def reverse(q,p):
#    global head
#    if p != None:
#        reverse(p,p.next)
#        p.next = q 
#    else:
#        head = q

def reverse(head):
    def helper(r,q,p):
        if p is None:
            q.next = r 
            return q 
        else:
            q.next = r 
        return helper(q,p,p.next)
    newHead = helper(None,head,head.next)
    return newHead
        
    
        





arr=[1,3,5,7,9,11,13]
LL = Creation(arr)
iteration(LL)
print()
RLL = reverse(LL)
iteration(RLL)



