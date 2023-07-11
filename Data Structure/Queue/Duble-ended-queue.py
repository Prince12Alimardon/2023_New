# class Deque:
#     def __init__(self):
#         self.deque = []
#
#     def is_empty(self):
#         return len(self.deque) == 0
#
#     def add_front(self, item):
#         self.deque.insert(0, item)
#
#     def add_rear(self, item):
#         self.deque.append(item)
#
#     def remove_front(self):
#         if not self.is_empty():
#             return self.deque.pop(0)
#         else:
#             print("Deque bo'sh")
#
#     def remove_rear(self):
#         if not self.is_empty():
#             return self.deque.pop()
#         else:
#             print("Deque bo'sh")
#
#     def size(self):
#         return len(self.deque)
#
#
# # Deque obyektini yaratish
# dq = Deque()
#
# # Elementlarni boshidan qo'shish
# dq.add_front(10)
# dq.add_front(20)
# dq.add_front(30)
#
# # Elementlarni ohiridan qo'shish
# dq.add_rear(40)
# dq.add_rear(50)
# dq.add_rear(60)  #[30, 20, 10, 40, 50, 60]
#
# # Deque elementlarini o'chirish
# print(dq.remove_front())  # 30
# print(dq.remove_rear())  # 60
# print(dq.remove_front())  # 20
# print(dq.remove_rear())  # 50 [10 60 20 50]
#
#
# # Deque hajmi
# print(dq.size())  # 3
#
#
#
