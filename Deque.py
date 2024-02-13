class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def empty(self):
        if self.size == 0: return True
        
    def get_size(self) -> int:
        return self.size
    
    def push_front(self, data):
        if self.empty() == True:
            self.front = Node(data)
            self.back = self.front
        else:
            self.front.next = Node(data)
            self.front.next.prev = self.front
            self.front = self.front.next
        self.size += 1

    def push(self, data):
        new = Node(data)
        if self.empty():
            self.front = new
            self.back = new
        else:
            new.prev = self.back
            self.back.next = new
            self.back = new
        self.size += 1
    
    def pop_front(self) -> int:
        if self.empty(): return
        
        temp = self.front.item
        self.front = self.front.prev
        self.front.next = None

        return temp

    def pop(self) -> int:
        if self.empty(): return
        
        temp = self.back.item
        self.back = self.back.next
        self.back.prev = None

        return temp   

    def get_front(self) -> int:
        if self.empty(): return
        return self.front.item

    def get_back(self) -> int:
        if self.empty(): return
        return self.back.item


if __name__ == '__main__':
    pass
