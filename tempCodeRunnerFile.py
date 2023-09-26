class Node:
    def __init__(self,val,next):
        self.elem = val 
        self.next=next 

def create_LL(arr):
    head = Node(arr[0],None)
    tail = head  
    for i  in range(1,len(arr)):
        tail.next = Node(arr[i],None)
        tail = tail.next 

    return head 

def show_elem(head):
    p = head 
    while p:
        print(p.elem,end=" -> ")
        p = p.next
    print("None") 


def merge_list(head1,head2):
    p = head1 
    q = head2 

    copy_head = None
    copy_tail = None  

    while p and q :
        if p.elem < q.elem:
            if copy_head is None:
                copy_head = Node(p.elem,None)
                copy_tail = copy_head 
            else:
                copy_tail.next = Node(p.elem,None)
                copy_tail = copy_tail.next 
            p = p.next 
        elif p.elem > q.elem:
            if copy_head is None:
                copy_head = Node(q.elem,None)
                copy_tail = copy_head 
            else:
                copy_tail.next = Node(q.elem,None)
                copy_tail = copy_tail.next
            q = q.next
        elif p.elem == q.elem:
            if copy_head is None:
                copy_head = Node(p.elem,None)
                copy_tail = copy_head 
            else:
                copy_tail.next = Node(p.elem,None)
                copy_tail = copy_tail.next 
            p = p.next 
            q = q.next 
    while p:
        copy_tail.next = Node(p.elem,None)
        copy_tail = copy_tail.next 
        p = p.next 
    while q:
        copy_tail.next = Node(q.elem,None)
        copy_tail = copy_tail.next 
        q = q.next 

    return copy_head 
 




# Diver Code
arr1 = [1,2,3,5]
arr2= [3,4,6,8]

LL_1 = create_LL(arr1)
LL_2 = create_LL(arr2)

Merged_LL = merge_list(LL_1,LL_2)

show_elem(Merged_LL)




