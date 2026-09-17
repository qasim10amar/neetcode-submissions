class MinStack:

    def __init__(self):
        self.stack = []
        self.mono = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if not self.mono:
            self.mono.append(val)
        
        else:
            self.mono.append(min(self.mono[-1], val))

        
    def pop(self) -> None:
        self.stack.pop()
        self.mono.pop()

    def top(self) -> int:
        top = self.stack[-1]
        return top
        

    def getMin(self) -> int:
        return self.mono[-1]

        
