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

def swap_nodes_value(head, k):
    def swap_elem(node, k, l, idx):
        if node is None:
            return

        nonlocal first_elem

        if idx == k:
            first_elem = node.elem
        if idx == l - k + 1:
            node.elem, first_elem = first_elem, node.elem

        swap_elem(node.next, k, l, idx + 1)

    

    l = length(head)
    first_elem = None  # Store the value of the kth node from the beginning
    swap_elem(head, k, l, 1)

LL = Creation([1, 2, 3, 4, 5])

print("Original Linked List:")
iteration(LL)
print('\n---------------')

new_head = swap_nodes_value(LL, 2)

print("Linked List after Swapping:")
iteration(new_head)
