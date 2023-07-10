############################
#Ali Cem Çakmak
#2212660
#Homework 2
############################

class Stack:

    def __init__(self):
        self._data = [] #Create an empty stack

    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e) #Add the element e to the top of the stack
    
    def top(self): #Return the top element without removing it
        if self.is_empty():
            print("Stack is empty")
        return self._data[-1]
    
    def pop(self): #Return the top element by removing it
        if self.is_empty():
            print("Stack is empty")
        return self._data.pop()

class Queue:
    DEFAULT_CAPACITY = 10 

    def __init__(self): #Create an empty queue
        self._data = [None]*Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def is_empty(self): #Return True if the queue is empty
        return self._size == 0
    
    def front(self): #Return the element at the front of the queue without removing
        if self.is_empty():
            print("Queue is empty")
        return self._data[self._front]

    def dequeue(self): # Remove and return the first element of the queue
        if self.is_empty():
            print("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e): #Add an element to the back of the queue
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front+self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk)%len(old)
        self._front = 0

def languageRecognizer(word, languageType):
    if languageType == "l2":
        Q = Queue()
        seperator = False
        for symbol in word:
            if not seperator:
                if symbol == "$":
                    seperator = True
                else:
                    Q.enqueue(symbol)
            else:
                if Q.dequeue() != symbol:
                    print("Word is not in the language")
                    return False
        if Q.is_empty():
            print("Word is in the language")
            return True
        else:
            print("Word is not in the language")
            return False
        
    if languageType == "l1":
        sorted_word = "".join(sorted(word, key=str.lower))
        counter_a = 0
        counter_b = 0
        counter_c = 0
        ab_match = False
        ac_match = False
        S1 = Stack()
        S2 = Stack()
        for symbol in sorted_word:
            if symbol == "a":
                counter_a += 1
                S1.push(symbol)
                S2.push(symbol)
            if symbol == "b" and S1.is_empty() == True:
                counter_b += 1
                ab_match = False
            if symbol == "b" and S1.is_empty() == False:
                counter_b += 1
                S1.pop()
                ab_match = True
            if symbol == "c" and S2.is_empty() == True:
                counter_c += 1
                ac_match = False
            if symbol == "c" and S2.is_empty() == False:
                counter_c += 1
                S2.pop()
                ac_match = True
            if not (symbol == "a" or symbol == "b" or symbol == "c"):
                ab_match = False
                ac_match = False
                break
            
        if counter_a == 0 or counter_b == 0 or counter_c == 0:
            ab_match = False
            ac_match = False
        
        if not S1.is_empty():
            ab_match = False
        if not S2.is_empty():
            ac_match = False

        if ab_match == True or ac_match == True:
            print("Word is in the language")
            return True
        else:
            print("Word is not in the language")
            return False
            
    else:
        print("Invalid Input")
