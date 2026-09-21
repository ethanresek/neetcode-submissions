class MinStack:

    def __init__(self):
        self._stack = []
        self._minstack = []
        

    def push(self, val: int) -> None:
        self._stack.append(val)
        if not self._minstack or val <= self._minstack[-1]:
            self._minstack.append(val)

    def pop(self) -> None:
        val = self._stack.pop()
        if val == self._minstack[-1]:
            self._minstack.pop()
        return val

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._minstack[-1]
