"""

622. Design Circular Queue




"""

class MyCircularQueue:

    def __init__(self, k: int):
        self.front = 0
        self.back = 0 # exclusive
        self.count = 0
        self.queue = [0 for _ in range(k)]

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False

        self.queue[self.back] = value
        self.back = (self.back + 1) % len(self.queue)
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False

        self.front = (self.front + 1) % len(self.queue)
        self.count -= 1
        return True
        

    def Front(self) -> int:
        if self.count == 0: return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.count == 0: return -1
        return self.queue[self.back - 1]

    def isEmpty(self) -> bool:
        return self.count == 0
        
    def isFull(self) -> bool:
        return self.count == len(self.queue)
        