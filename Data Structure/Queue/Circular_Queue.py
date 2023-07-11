class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.k == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Navbat to'la")
        elif self.is_empty():
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Navbat bo'sh")
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = self.rear = -1
            return item
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.k
            return item


# Circular Queue obyektini yaratish
cq = CircularQueue(5)

# Elementlarni navbatga qo'shish
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
# cq.enqueue(60)  # Navbat to'la, hato xabar chiqadi

# Elementlarni navbatdan olib tashlash
print(cq.dequeue())  # 10
print(cq.dequeue())  # 20
print(cq.dequeue())  # 30
print(cq.queue)
# #
# # # Elementlarni navbatga qo'shish
cq.enqueue(70)
cq.enqueue(80)
# # #
# # # Elementlarni navbatdan olib tashlash
print(cq.dequeue())  # 40
print(cq.dequeue())  # 50
print(cq.dequeue())  # 60
print(cq.dequeue())  # 70
print(cq.dequeue())  # Navbat bo'sh, hato xabar chiqadi
