class HashNode:
    def __init__(self,key,val,next):
        self.key = key
        self.val = val
        self.next = next 

def Hash(key, hash_table):
    return key% len(hash_table)

def Insert(key,val,hash_table):
    idx = Hash(key,hash_table)

    node = HashNode(key,val,None)
    if hash_table[idx] == None:
        hash_table[idx] = node 
    else:
        node.next = hash_table[idx]
        hash_table[idx] = node

def Search(wanted_key,hash_table):
    idx = Hash(wanted_key,hash_table)
    p = hash_table[idx]
    c = 1
    while p!= None:
        if p.key == wanted_key:
            return f"{wanted_key} is at index -> {idx}\nvalue: {p.val}\nLevel: {c} "
        
        p = p.next 
        c+=1
        
    return f"{wanted_key} doesn't exist"


def Delete_key(key,hash_table):
    for i in range(len(hash_table)):
        if hash_table[i] != None:
            q = None
            p = hash_table[i]
            if p.key == key:                               # For Deleting First Node
                deleted_key = p.key
                hash_table[i] = p.next
                return deleted_key
            else:
                while p!=None:                            # For Deleting Rest of the nodes
                    if p.key == key:
                        q.next = p.next
                        return p.key
                    else:
                        q = p
                        p = p.next 


def Print_HashTable(hash_table):
    for i in range(len(hash_table)):
        if hash_table[i] == None:
            print(f"Index: {i}")
        else:
            print(f"Index: {i}",end=' ')
            p = hash_table[i]
            while p!=None:
                print(f"({p.key}: {p.val})",end=" --> ")
                p = p.next 
            print()
        

my_hash_table = [None] * 5

my_list = [[12, "Apple"], [5, "Orange"], [17, "Banana"], [10, "Grapes"], [22, "Watermelon"], [15, "Pineapple"]]
for item in my_list:
  Insert(item[0],item[1],my_hash_table)
Print_HashTable(my_hash_table)



#Test code
print("Deleted key is",Delete_key(15,my_hash_table))   #Deleting a key

print(Search(17,my_hash_table))                        #Searching a key

print("\nUpdated Hash Table:")                         #Printing Updated Hash Table
Print_HashTable(my_hash_table)
