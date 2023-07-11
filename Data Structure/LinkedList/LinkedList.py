class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
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

    def delete_at_beginning(self):
        if self.is_empty():
            print("LinkedList bo'sh")
        else:
            self.head = self.head.next

    def delete_at_end(self):
        if self.is_empty():
            print("LinkedList bo'sh")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None

    def display(self):
        if self.is_empty():
            print("LinkedList bo'sh")
        else:
            current = self.head
            while current is not None:
                print(current.value, end=" -> ")
                current = current.next
            print("None")


# LinkedList obyektini yaratish
ll = LinkedList()

# Elementlarni LinkedListga qo'shish
ll.add_at_beginning(10)  #[10]
ll.add_at_beginning(20)
ll.add_at_end(30)
ll.add_at_end(40)  # [20 10 30 40]

# LinkedListni chiqarish
ll.display()  # 20 -> 10 -> 30 -> 40 -> None

# LinkedListdan elementlarni o'chirish
ll.delete_at_beginning()
ll.delete_at_end()
#
# # Yangi LinkedListni chiqarish
ll.display()  # 10 -> 30 -> None




