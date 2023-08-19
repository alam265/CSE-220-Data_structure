lane = [None]*4
class Node:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

def Creation(arr):
    head = Node(arr[0], None)
    tail = head
    for i in range(1, len(arr)):
        n = Node(arr[i], None)
        tail.next = n
        tail = tail.next
    return head

def iteration(head):
    p = head
    while p:
        print(p.elem, end=' ')
        p = p.next

def length(head):
    p = head
    c = 0
    while p:
        c += 1
        p = p.next
    return c

def express_lane(head):
    bucket_size = (length(head)//4)+1

    p = head 
    lane[0]= p
    idx = 1
    while p and p.next:
        for _ in range(bucket_size):
            p = p.next 
        lane[idx] = p
        idx+=1



LL = Creation([4,6,9,18,25,37,62,67,79,84])

print("Original Linked List:")
iteration(LL)
print('\n---------------')

express_lane(LL)


for i in lane:
    print(i.elem)


print(lane[0].next.elem)



