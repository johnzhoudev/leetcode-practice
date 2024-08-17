"""
make fifo with 2 stacks

tactic: input stack and output stack, shuffle between
- or just shuffle all to main always, and to input shuffle over
"""

class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        while self.output:
            self.input.append(self.output.pop())
        self.input.append(x)

    def pop(self) -> int:
        while self.input:
            self.output.append(self.input.pop())
        return self.output.pop()
        
    def peek(self) -> int:
        while self.input:
            self.output.append(self.input.pop())
        return self.output[-1]
        
    def empty(self) -> bool:
        return (len(self.input) + len(self.output)) == 0
        

