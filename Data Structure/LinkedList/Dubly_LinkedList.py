class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_at_beginning(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_at_end(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete_at_beginning(self):
        if self.is_empty():
            print("Doubly LinkedList bo'sh")
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_at_end(self):
        if self.is_empty():
            print("Doubly LinkedList bo'sh")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.prev.next = None

    def display_forward(self):
        if self.is_empty():
            print("Doubly LinkedList bo'sh")
        else:
            current = self.head
            while current is not None:
                print(current.value, end=" -> ")
                current = current.next
            print("None")

    def display_backward(self):
        if self.is_empty():
            print("Doubly LinkedList bo'sh")
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            while current is not None:
                print(current.value, end=" -> ")
                current = current.prev
            print("None")


# Doubly LinkedList obyektini yaratish
dll = DoublyLinkedList()

# Elementlarni Doubly LinkedListga qo'shish
dll.add_at_beginning(10)
dll.add_at_end(20)
dll.add_at_end(30)

# Doubly LinkedListni oldindan chiqarish
dll.display_forward()  # 10 -> 20 -> 30 -> None

# Doubly LinkedListni orqadan chiqarish
dll.display_backward()  # 30 -> 20 -> 10 -> None

# Doubly LinkedListdan elementlarni o'chirish
dll.delete_at_beginning()
dll.delete_at_end()

# Yangi Doubly LinkedListni chiqarish
dll.display_forward()  # 20 -> None
