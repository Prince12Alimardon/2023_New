# 859
def buddyStrings(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    if s == goal and len(set(s)) < len(s):
        return True
    d = [(a, b) for a, b in zip(s, goal) if a != b]
    return len(d) == 2 and d[0] == d[1][::-1]


# ---------------------------------------------------------------
# 155
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


#  ----------------------------------------------------------------
#  70
def climbStairs(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    k2 = 2
    k3 = 3

    for i in range(n - 3):
        k3, k2 = k3 + k2, k3

    return k3
