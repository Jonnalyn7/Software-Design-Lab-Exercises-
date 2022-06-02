def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")

        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")

        print()


HashTable = [[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)

insert(HashTable, 10, 'Urdaneta')
insert(HashTable, 25, 'Villasis')
insert(HashTable, 20, 'Sta.Barbara')
insert(HashTable, 9, 'Dagupan')
insert(HashTable, 21, 'Alaminos')
insert(HashTable, 21, 'San Nicolas')

display_hash(HashTable)