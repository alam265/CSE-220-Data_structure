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

def middle(head):
    slow = head 
    fast = head 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
    return slow

def Palindrome_Checker(head):
    p = head
    rev = reverse_LL(middle(head))
    while p :
        if p.elem != rev.elem:
            return False 
        rev = rev.next 
        p = p.next       
    return True 

def reverse_LL(head):
    
    r = None
    q = None 
    p = head 
 
    while p!=None:
        r = q 
        q = p
        p = p.next 
        q.next = r 
     
    return q 


 




LL = Creation([1,2])

print('=-----------=====')

print(Palindrome_Checker(LL))



