class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_at_beginning(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def add_at_end(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete_at_beginning(self):
        if self.is_empty():
            print("Circular LinkedList bo'sh")
        elif self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

    def delete_at_end(self):
        if self.is_empty():
            print("Circular LinkedList bo'sh")
        elif self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            previous = None
            while current.next != self.head:
                previous = current
                current = current.next
            previous.next = self.head

    def display(self):
        if self.is_empty():
            print("Circular LinkedList bo'sh")
        else:
            current = self.head
            while True:
                print(current.value, end=" -> ")
                current = current.next
                if current == self.head:
                    break
            print("Head")


# Circular LinkedList obyektini yaratish
cll = CircularLinkedList()

# Elementlarni Circular LinkedListga qo'shish
cll.add_at_beginning(10)
cll.add_at_end(20)
cll.add_at_end(30)

# Circular LinkedListni chiqarish
cll.display()  # 10 -> 20 -> 30 -> Head

# Circular LinkedListdan elementlarni o'chirish
cll.delete_at_beginning()
cll.delete_at_end()

# Yangi Circular LinkedListni chiqarish
cll.display()  # 20 -> Head
