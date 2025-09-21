
class Node:
    def __init__(self,value,next):
        self.value = value 
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def creation(self,arr):
        self.head  = Node(arr[0],None)
        self.tail = self.head 

        for i in range(1,len(arr)):
            n = Node(arr[i],None)
            self.tail.next = n
            self.tail = self.tail.next 

    def iteration(self):
        self.c = 0
        p = self.head
        while p!=None :
            self.c +=1
            print(p.value,end=' ')
            p = p.next 
        print()
    def count(self):
        count = 0
        p = self.head 
        while p!=None:
            count += 1
            p = p.next 
        return count 

    #def elemAt(self,idx):
        #p = self.head
        #if 0 <= idx <= self.c:
            #for i in range(idx):
                #p = p.next 
            #return p.value
        #return 'Invalid Index'
    
    def elemAt(self,idx):
        count = 0
        p = self.head 
        while p!=None:
            if count == idx:
                return p.value
            count+=1
            p = p.next 
        return 'Invalid Index'
    
    def nodeAt(self,idx):
        c = 0
        p = self.head 

        while p!=None:
            if c==idx:
                return p 
            c+=1
            p = p.next 
        return -1 
    def Insertion(self,idx,value):
        c = SLL.count()
        
        if idx == 0:
            temp = Node(value,None)
            temp.next = self.head 
            self.head = temp 
        elif 0 < idx <c:
            temp = Node(value,None)
            p = self.head 
            for i in range(idx-1):
                p = p.next 
            temp.next = p.next 
            p.next = temp 
        else:
            print('Invalid Index')
    
    def indexOf(self,elem):
        p = self.head 
        c=0
        while p!=None:
            if p.value==elem:
                return c
            c+=1
            p=p.next 
        return -1 
    def reverse_LL(self):
        p = self.head 
        q = None
        r = None 
        while p!=None:
            r = q
            q = p
            p = p.next
            q.next = r 
        self.head= q 
    def remove(self,idx):
        p = self.head 
        for i in range(idx-1):
            p = p.next
        p.next = p.next.next 


    def L_rotate(self):
        first = self.head 
        second = self.head.next 
        last = self.head 

        while last.next !=None:
            last =last.next 
        self.head = second
        last.next = first 
        first.next = None
    
    

    def R_rotate(self):
        first = self.head 
        second_last = self.head 

        while second_last.next.next !=None:
            second_last = second_last.next
        last = second_last.next 
        last.next = first 
        second_last.next = None 
        self.head = last 
        
 

       


            


        
    





SLL = LinkedList()
SLL.creation([1,2,3,4,5,6])
SLL.Insertion(5,10)
SLL.iteration()
SLL.reverse_LL()
SLL.iteration()
SLL.remove(5)
SLL.iteration()
print(SLL.indexOf(10))


print('\n--------------------')

SLL.L_rotate()
SLL.iteration()