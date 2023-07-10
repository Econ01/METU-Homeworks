class LinkedList:
    '''
    This is a Linked List class that you will work on, you can define additional helper functions but do not change current member functions and variables (e.g, cant make doubly linked list)
    '''
    def __init__(self):
        self.head = None # Reference to head node
        self.size = 0 # Size of Linked List
        self.tail = None

    class Node:
        __slots__ = "data", "next"

        def __init__(self, element, next):
            self.data = element 
            self.next = next

    def len(self):
        return self.size

    def is_empty(self):
         return self.size == 0
    
    def insert_last(self, e):
        newest = self.Node(e, None)
        if not self.head:
            self.head = newest
            self.tail = newest
        elif self.tail:
            self.tail.next = newest
            self.tail = newest
        else:
            self.head.next = newest
            self.tail = newest
        self.size = self.size + 1

    def swap(self):
        swapped = False
        current = self.head
        parent = current
        temp_head = current
        while(current.next != None):
            if current.data > current.next.data:
                if current == self.head:
                    temp_node_1 = current
                    temp_node_2 = current.next
                    temp_node_3 = current.next.next
                    swapped = True
                    temp_head = self.head.next
                    current.next.next = temp_node_1
                    current.next = temp_node_3
                else:
                    temp_node_1 = current
                    temp_node_2 = current.next
                    temp_node_3 = current.next.next
                    swapped = True
                    parent.next = temp_node_2
                    current.next.next = temp_node_1
                    current.next = temp_node_3
                    parent = current
            self.head = temp_head
            current = current.next
        return swapped

    def print_contents(self):
        '''
        Do not touch to this print function this function prints the contents of the Linked List
        '''
        format_str = "%d" 
        if self.size == 0:
            print(" ")
            return
        current = self.head
        while(current.next != None):
            print((format_str + " -> ")%current.data, end="")
            current = current.next

        print(format_str%current.data)


def bubbleSinglePass(llist):
    if llist.is_empty():
        print("List is Empty!")
        return
    llist.swap()
    return llist

def bubbleSort(llist):
    if llist.is_empty():
        print("List is Empty!")
        return
    
    swapped = llist.swap()
    while swapped:
        print("Run")
        swapped = llist.swap()
    return llist