import numpy as np

#deque using numpy array
class Deque:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.front = -1
        self.back = -1
        self.array = np.zeros(self.capacity, dtype=object)

    def resize(self):
        new_capacity = self.capacity * 2
        
        #new array with double the size of old one
        temp = np.zeros(new_capacity, dtype=object)

        for i in range(self.get_size()):
            temp[i] = self.array[i]
        self.array = temp
        self.capacity = new_capacity

    def empty(self):
        if self.get_size() == 0: return True
        
    def get_size(self) -> int:
        return self.back + 1
    
    def push_front(self, data):
        if self.empty():
            self.array[0] = data
            self.front = 0
            self.back = 0
        elif self.get_size() < self.capacity:
            self.array[1:] = self.array[:-1] #shifting to the right by one
            self.array[0] = data
            self.back += 1
        else:
            self.resize()
            self.array[1:] = self.array[:-1] #right shifting by one after resizing
            self.array[0] = data
            self.back += 1
        
    def push(self,data): #pushes to back
        if self.empty():
            self.array[0] = data
            self.front = 0
            self.back = 0
        elif self.get_size() < self.capacity:
            self.array[self.back + 1] = data
            self.back += 1
        else:
            self.resize()
            self.array[self.back + 1] = data
            self.back += 1

    def pop_front(self) -> str:
        if self.empty(): return
        temp = self.get_front()

        if self.get_size() == 1:
            self.array[0] = 0
            self.front = -1
        else:
            self.array[:-1] = self.array[1:] #left shift by one to remove front element

        self.back -= 1 #self.back shifts back 
        return temp

    def pop(self) -> str: 
        if self.empty(): return
        temp = self.get_back()

        if self.get_size() == 1:
            self.array[0] = 0
            self.back = -1
            self.front = -1
        else:
            self.array[self.back] = 0
            self.back -= 1  
        return temp 

    def get_front(self) -> str:
        if self.empty(): return
        return self.array[self.front]

    def get_back(self) -> str:
        if self.empty(): return
        return self.array[self.back]

def isPalindrome(s: str) -> bool:
    deque = Deque()

    for char in s:
        deque.push(char)
    print(deque.array)

    while not deque.empty():
        if deque.get_front() == deque.get_back():
            print(str(deque.get_front()), "==", str(deque.get_back()))
            deque.pop()
            deque.pop_front()
        else:
            print(str(deque.get_front()), "!=", str(deque.get_back()))
            return False
    return True

def reverse_deque(deque):
    reversed_deque = Deque()

    while not deque.empty():
        reversed_deque.push(deque.get_back())
        deque.pop()
    return reversed_deque
        

if __name__ == '__main__':

    deque = Deque()

    deque.push(1)
    deque.push(2)
    deque.push(3)

    reversed_deque = reverse_deque(deque)
    while not reversed_deque.empty():
        print(reversed_deque.pop_front())


    


    





