class RingBuffer:
    def __init__(self, capacity):
        self.curIndex = 0
        self.capacity = capacity
        self.list = [None] * self.capacity
        pass

    def append(self, item):
        self.list[self.curIndex] = item
        self.curIndex = self.curIndex + 1 if self.curIndex < self.capacity - 1 else 0

    def get(self):
        return [x for x in self.list if x]
