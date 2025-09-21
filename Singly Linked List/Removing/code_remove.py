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


def remove(head,idx):
    p = head 
    if idx==0:
        head = head.next
    else:
        for i in range(idx-1):
            p = p.next 
        p.next = p.next.next
    return head 



arr = [1,3,5,7,9,11]
creation(arr)
iteration(creation(arr))
remove(creation(arr),2)

print('----------------------')

iteration(remove(creation(arr),5))



