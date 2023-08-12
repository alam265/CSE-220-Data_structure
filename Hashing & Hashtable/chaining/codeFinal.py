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
        new_Node = HashNode(key,val,None)
        new_Node.next = hash_table[idx]
        hash_table[idx] = new_Node

def Search(wanted_key,hash_table):
    for i in range(len(hash_table)):
        if hash_table[i] != None:
            p = hash_table[i]
            c = 1
            while p!= None:
                if p.key == wanted_key:
                    return f"{wanted_key} is at index -> {i}\nvalue: {p.val}\nLevel: {c} "
                p = p.next 
                c+=1
    return f"{wanted_key} doesn't exist"

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



print(Search(10,my_hash_table))