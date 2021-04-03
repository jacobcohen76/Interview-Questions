import collections

class MaxStack:
    def __init__(self):
        self.stack = collections.deque()
        self.maxes = collections.deque()
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.maxes and self.maxes[-1] > val:
            self.maxes.append(self.maxes[-1])
        else:
            self.maxes.append(val)
    
    def pop(self) -> int:
        self.maxes.pop()
        return self.stack.pop()
    
    def get_max(self) -> int:
        return self.maxes[-1]

max_stack = MaxStack()
max_stack.push(1)
max_stack.push(3)

print(max_stack.get_max())
max_stack.pop()
print(max_stack.get_max())

    