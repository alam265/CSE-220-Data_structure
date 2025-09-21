class Node:
    def __init__(self,value,next,prev):
        self.elem = value 
        self.next = next 
        self.prev = prev 

class Circular_Doubly_Linked_list:
    def __init__(self):
        self.dh = Node(None,None,None) 
        self.dh.next = self.dh
        self.dh.prev = self.dh
        self.tail = self.dh

    def add_Node(self,value):
        
        temp = Node(value,None,None)
        temp.next = self.dh 
        self.dh.prev = temp
        self.tail.next = temp
        temp.prev = self.tail  
        self.tail = temp 
        
        print("Node added Successfully")



    def show_all_Node(self):
        if self.dh.next:
            p = self.dh.next   

            while p!=self.dh:
                print(p.elem)
                p = p.next 
        else:
            print('No Node left')

    def serve_Node(self):
        if self.dh.next!=self.dh  :
            p = self.dh.next
            q = p.next  
            print(f"{p.elem} Served Successfully")
            self.dh.next = q 
            q.prev = self.dh 
        else:
            print('No patient to serve')

    def can_D_gohome(self):
        if self.dh.next == self.dh:
            print('Yes')
        else:
            print('No')
    def cancel_all_appnmnt(self):
        if self.dh.next.elem:
            self.dh.next = self.dh  
            self.dh.prev = self.dh 
            self.tail = self.dh
        elif  self.dh.next.elem==None:
            print('No Node to delete')



    


CDLL = Circular_Doubly_Linked_list()
"""
CDLL.add_Node(100)
CDLL.add_Node(200)



CDLL.cancel_all_appnmnt()


CDLL.serve_Node()

CDLL.can_D_gohome()
CDLL.show_all_Node()
"""
print("---Welcome---")
print("Select an Option:")

#print(f"1. Add Note\n2. Serve Node\n3. Show All Node\n4. Can doc go home?\n5. Cancel All Appointment.\n6. Exit")

while True:
    print("-----------------------------------------------")
    print(f"1. Add Note\n2. Serve Node\n3. Show All Node\n4. Can doc go home?\n5. Cancel All Appointment.\n6. Exit")

    inp = int(input("Choose option No: "))
    if inp ==1:
        CDLL.add_Node(int(input('Enter Value:')))
    elif inp ==2:
        CDLL.serve_Node()
    elif inp == 3:
        CDLL.show_all_Node()
    elif inp == 4:
        CDLL.can_D_gohome()
    elif inp == 5:
        CDLL.cancel_all_appnmnt()
    elif inp == 6:
        break

print('-----------------------------------------')

