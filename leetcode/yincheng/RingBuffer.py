from collections import deque
class RingBuffer:
    def __init__(self):
        self.buffer = deque()
        self.limit = 0
        self.locked = False

    def get(self, buffer):
        consumed = buffer[0]
        buffer.popleft()
        return consumed
    
    def push(self, buffer, char, limit):
        length = len(buffer)

        if length >= limit:
            return False
        buffer.append(char)
        return True
        


'''
buffer = [4, 5, 1, 2, 3]
limit = 5
buffer.popleft() *3

before call push: 
see if buffer.locked = False
    if not locked: set buffer.locked = True
    push


'''