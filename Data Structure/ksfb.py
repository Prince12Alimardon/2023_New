import queue

q = queue.Queue(maxsize=6)

q.put(12)
q.put(1)
q.put(2)
q.put(132)
q.put(-112)
q.put(90)
print(q.get())
print(q.get())
print(q.get())


# import queue
#
# a = queue.Queue()
# a.put(12)
# a.put(52)
# a.put(32)
# a.put(52)
# a.put(22)
# a.put(1112)
# a.put(-2112)
# while not a.empty():
#     print(a.get())


# from queue import LifoQueue
# import queue
# a = queue.LifoQueue()
#
# for i in range(1, 10+1, 2):
#     a.put(i)
#
# print(a.get())
# while not a.empty():
#     print(a.get())
#
# import queue
# l = queue.PriorityQueue()
# # l.put(1)
# # l.put(91)
# # l.put(-81)
# # l.put(5)
# l.put((1, 'Hello'))
# l.put((71, 67))
# l.put((9, 'olma'))
# l.put((-1, 3))
# while not l.empty():
#     print(l.get()[0])

def mydeco(fact):
    def Wrapper(*args,**kwargs):
        print("strat deco")
        fact()
        print("end deco")
    return Wrapper
@mydeco
def hello():
    print("hi")
mydeco(hello())
print()
hello()