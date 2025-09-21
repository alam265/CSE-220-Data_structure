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



def even_before_odd(head):
    cH1 = None
    cT1 = None 

    cH2 = None 
    cT2 = None 

    p1 = head 
    p2 = head 

    while p1!=None:
        if p1.elem%2==0:
            n = Node(p1.elem,None)
            if cH1 == None:
                cH1 = n 
                cT1 = cH1 
            else:
                cT1.next = n
                cT1 = cT1.next 
        p1 = p1.next 


    while p2!=None:
        if p2.elem%2!=0:
            n = Node(p2.elem,None)
            if cH2 == None:
                cH2 = n 
                cT2 = cH2 
            else:
                cT2.next = n 
                cT2 = cT2.next 

        p2 = p2.next 



    ptr = cH1 

    while ptr.next!=None:
        ptr = ptr.next 
    ptr.next = cH2 
    return cH1     










LL = Creation([17 , 15 , 8 , 12 , 10 , 5 , 4 , 1 , 7 , 6 ])

M_LL = even_before_odd(LL)

iteration(M_LL)