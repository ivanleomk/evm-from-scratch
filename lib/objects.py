class Stack:
    def __init__(self, size = 1024):
        self.list = []
        self.maxSize = size

    def push(self, item):
        if len(self.list) == self.maxSize:
            return (True,[])
        self.list.append(item)

class Memory:
    def __init__(self):
        self.array = bytearray();

class Context:
    def __init__(self, code, pc=0):
        self.stack = Stack(1024)
        self.memory = Memory()
        self.code = code
        self.pc = pc

    def push_item(self,item):
        self.stack.push(item)