# import queue
# q = queue.Queue()
# nums = [10, 20, 30, 40]
# for i in nums:
#     q.put(i)
#
# print(q.get())
#
#

# import queue
#
# q = queue.LifoQueue()
#
# nums = [1,2,3,4,5]
# for i in nums:
#     q.put(i)
#
# print(q.get())


import queue

q = queue.PriorityQueue()

q.put(1)
q.put(2)
q.put(21)
q.put(12)
while not q.empty():
    print(q.get())
