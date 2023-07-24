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
def count(h):
    p = h 
    c=0
    while p!=None:
        c +=1
        p = p.next 
    return c 



def indexOf(head,elem):
    p = head 
    c=0
    while p!=None:
        if p.elem==elem:
            return c
        c+=1
        p=p.next 
    return -1 
def Insertion(head,idx,value):
    c = count(head)
    
    
    if idx == 0:
        temp = Node(value,None)
        temp.next = head 
        head = temp 
    elif 0 < idx <=c:
        temp = Node(value,None)
        p = head 
        for i in range(idx-1):
            p = p.next 
        temp.next = p.next 
        p.next = temp 
    else:
        print('Invalid Index')



arr=[1,3,5,7,9,11,13]
Creation(arr)
iteration(Creation(arr))
print()
print(indexOf(Creation(arr),13))
Insertion(Creation(arr),2,100)
iteration(Creation(arr))
