# import queue
# q = queue.Queue()
#
# q.put(12)
# q.put(1)
# q.put(2)
# q.put(6)
# q.put(-92)
# q.put(-924)
# print(q.get())
# print(q.get())
# print(q.get())

# import queue
# q = queue.Queue()
# for i in range(0, 15, 2):
#     q.put(i)
#
# while not q.empty():
#     print(q.get())

# import queue
#
# q = queue.LifoQueue()
# q.put(12)
# q.put(1)
# q.put(1122)
# q.put(1234)
# q.put(14332)
# while not q.empty():
#     print(q.get())

# import random
# import queue
# q = queue.LifoQueue()
# for i in range(10):
#     a = random.randint(300,399)
#     q.put(a)
#
# while not q.empty():
#     print(q.get())

import queue
q = queue.PriorityQueue()

# q.put(5)
# q.put(90)
# q.put(-15)
# q.put(2)
q.put((1, 'hello'))
q.put((22, 3))
q.put((3, 'hello wold'))
q.put((-9, 'python'))
while not q.empty():
    print(q.get()[0])
