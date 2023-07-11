class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def size(self):
        return len(self.stack)


# Stack obyektini yaratish
stack = Stack()

# Elementlarni qo'shish
# stack.push(input('ism: '))
# stack.push(input('ism: '))
# stack.push(input('ism: '))
# stack.push(input('ism: '))
# stack.push(input('ism: '))
#
# Elementni o'chirish
# print(stack.pop())

# for i in range(5):
#     stack.push(input('ism: '))
#
# print(stack.peek())
#
# # Classwork
# # Leetcode: 859(easy), 155(medium), 70(easy)

# 155 -misolni ishlang leetcodeda






