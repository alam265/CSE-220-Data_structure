class HashNode:
  def __init__(self, key, val, next):
    self.key = key
    self.val = val
    self.next = next


def hash(k, ht):
  return k % len(ht)

def insert(key, val, my_hash_table):  
  idx = hash(key, my_hash_table)
  if my_hash_table[idx] == None:
    my_hash_table[idx] = HashNode(key,val,None)
  else:
    newHashNode = HashNode(key,val,None)
    newHashNode.next = my_hash_table[idx]
    my_hash_table[idx] = newHashNode


def search(wanted_key,hash_table):
    for i in range(len(hash_table)):
        if hash_table[i] != None:
            temp = hash_table[i]
            c=1
            while temp!=None:
                if temp.key == wanted_key:
                    return (f"Value: {temp.val} and index: {i} and level {c}")
                temp = temp.next 
                c+=1
    return f"Key {wanted_key} does not exist"
    


    

def printHashTable(ht):
  for i in range(len(ht)):
    if ht[i] == None:
      print("Index:", i)
    else:
      print('Index:',i,end=' ')
      temp = ht[i]
      while temp != None:
        print(f"(Key: {temp.key}: Value: {temp.val}", end=" --> ")
        temp = temp.next
      print()



my_hash_table = [None] * 5

my_list = [[12, "Apple"], [5, "Orange"], [17, "Banana"], [10, "Grapes"], [22, "Watermelon"], [15, "Pineapple"]]
for item in my_list:
  insert(item[0],item[1],my_hash_table)
printHashTable(my_hash_table)



print(search(10,my_hash_table))