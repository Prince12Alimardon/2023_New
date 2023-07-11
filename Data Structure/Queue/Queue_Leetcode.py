# 1480
def runningSum(nums):
    sum = 0
    my_list = []
    for i in nums:
        sum += i
        my_list.append(sum)
    return my_list

# ---------------------------------------------------------
# 2652
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum([i for i in range(n+1) if i%3==0 or i % 5 == 0 or i % 7 == 0])
#  -------------------------------------------------------

# 622
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.size = k
        self.pointer = 0

    def enQueue(self, value: int) -> bool:
        if len(self.queue) < self.size:
            self.queue.append(value)
            return True

    def deQueue(self) -> bool:
        if self.queue:
            del self.queue[0]
            return True

    def Front(self) -> int:
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def Rear(self) -> int:
        if self.queue:
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.queue:
            return False
        else:
            return True

    def isFull(self) -> bool:
        if len(self.queue) == self.size:
            return True


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

#  -------------------------------------------------------------

#  232
class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack = [x] + self.stack

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0

#  -----------------------------------------------------------------
#  225
from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.clear()
        self.q1.append(x)
        for i in range(len(self.q1) - 1,-1,-1):
            self.q2.append(self.q1[i])

    def pop(self) -> int:
        num = self.q2.popleft()
        self.q1.clear()
        for i in range(len(self.q2) - 1,-1,-1):
            self.q1.append(self.q2[i])
        return num

    def top(self) -> int:
        return self.q2[0]

    def empty(self) -> bool:
        if len(self.q1) == 0:
            return True
        return False

