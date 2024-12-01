"""

346. Moving Average from Data Stream

    
straightforward, keep track of count and total using queue

Tactic:
Use a queue, track count and total

"""

from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.maxSize = size
        self.queue = deque()
        self.total = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val

        if len(self.queue) > self.maxSize:
            self.total -= self.queue.popleft()
        
        return self.total / len(self.size)

