class Node:
    def __init__(self,value,next):
        self.elem = value 
        self.next = next 


def creation(arr):
    dhead = Node(None,None)
    tail = dhead 
    for i in range(len(arr)):
        n = Node(arr[i],None)
        n.next = dhead
        tail.next = n
        tail = n
    return dhead 

def iteration(dh):
    p = dh.next 

    while p!=dh:
        print(p.elem,end=' ')
        p = p.next 

def Insertion(dh,idx,value):
    p = dh 
    temp = Node(value,None)
    for i in range(idx):
        p = p.next 
    temp.next = p.next 
    p.next = temp


CLL = creation([1,2,3,4,5,6])

iteration(CLL)

Insertion(CLL,1,100)

print('==============')

iteration(CLL)