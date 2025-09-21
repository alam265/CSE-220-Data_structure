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
        tail = tail.next 

    return head 

def iteration(head):
    p = head 
    while p!=None:
        print(p.elem,end=' ')
        p = p.next 
    

def L_rotate(head):
    first = head 
    second = head.next 
    last = head 

    while last.next !=None:
        last =last.next 
    head = second
    last.next = first 
    first.next = None
    
    return head 

def R_rotate(head):
    first = head 
    second_last = head 

    while second_last.next.next !=None:
        second_last = second_last.next
    last = second_last.next 
    last.next = first 
    second_last.next = None 
    head = last 
    return head 
 




arr=[1,2,3,4,5,6]
creation(arr)
iteration(creation(arr))
print('\n--------------------')

L_rotate(creation(arr))
iteration(L_rotate(creation(arr)))

print('\n------------------------')
iteration(R_rotate(creation(arr)))