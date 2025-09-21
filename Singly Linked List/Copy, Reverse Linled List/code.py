class Node:
    def __init__(self,value,next):
        self.elem = value
        self.next = next 




def creation(arr):
    head = Node(arr[0],None)
    tail = head 
    for i in range(1,len(arr)):
        n = Node(arr[i],None)
        tail.next = n
        tail = n 
    return head 

def iteration(head):
    p = head 
    while p!=None:
        print(p.elem,end=' ')
        p = p.next 


def copy_LL(head):
    ch = None 
    ct = None 
    p = head
    while p!=None:
        n = Node(p.elem,None)
        if ch == None:
            ch = n 
            ct = ch 
        else:
            ct.next = n
            ct = n 
        p = p.next
    return ch 

def reverse_in_place(head):
    p = head 
    q = None 
    r = None 
    while p!=None:
        r = q 
        q = p 
        p = p.next 
        q.next = r 
    head = q 
     
    return head

    
        

arr = [1,2,3,4,5,6,7,8]
creation(arr)
iteration(creation(arr))
copy_LL(creation(arr))
print('\n-----------------------')
#iteration(copy_LL(creation(arr)))

iteration(reverse_in_place(creation(arr)))


