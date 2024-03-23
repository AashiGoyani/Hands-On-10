class Node:
    def __init__(self, index, element):
        self.index = index
        self.element = element
        self.next = None
        self.prev = None

class doublylinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, index, element):
        new_node = Node(index, element)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, node):
        if node == self.head == self.tail:
            self.head = self.tail = None
        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def print_list(self):
        current = self.head
        while current:
            print(f"({current.index}, {current.element})", end=" ")
            current = current.next
        print()

class HashTable:

    def __init__(self, initial_capacity=10):
        self.size = 0
        self.capacity = initial_capacity
        self.table = []
        for _ in range(initial_capacity):
            self.table.append(doublylinkedlist())

    def hash_function(self, index):
        A = 0.6180339887  # Golden ratio
        return int(self.capacity * (index * A - int(index * A)))

    def rehash(self, new_capacity):
        new_table = []
        for _ in range(new_capacity):
            new_table.append(doublylinkedlist())

        for linked_list in self.table:
            current = linked_list.head
            while current:
                index = self.hash_function(current.index) % new_capacity
                new_table[index].insert(current.index, current.element)
                current = current.next

        self.capacity = new_capacity
        self.table = new_table


    def insert(self, index, element):
        hash_index = self.hash_function(index) % self.capacity  
        self.table[hash_index].insert(index, element)  
        self.size += 1
        if self.size >= self.capacity * 3 / 4:
            self.rehash(self.capacity * 2)

    def delete(self, index):
        hash_index = self.hash_function(index) % self.capacity
        current = self.table[hash_index].head
        while current:
            if current.index == index:
                self.table[hash_index].delete(current)
                self.size -= 1
                break
            current = current.next
        if self.size <= self.capacity / 4:
            self.rehash(self.capacity // 2)

    def search(self, index):
        hash_index = self.hash_function(index) % self.capacity
        current = self.table[hash_index].head
        while current:
            if current.index == index:
                return current.element
            current = current.next
        return None

    def print_table(self):
        for i, linked_list in enumerate(self.table):
            print(f"[{i}]: ", end="")
            linked_list.print_list()


# Example
    
hasht = HashTable()

hasht.insert(3, 30)
hasht.insert(1, 10)
hasht.insert(11, 110)

hasht.print_table()  # printing the hash table

print("Searching result for index 3:", hasht.search(3))  

hasht.delete(3)

hasht.print_table()  # printing the hash table after removing the index 2
