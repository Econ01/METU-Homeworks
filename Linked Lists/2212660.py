class LinkedList:
    '''
    This is a Linked List class that you will work on, you can define additional helper functions but do not change current member functions and variables (e.g, cant make doubly linked list)
    '''
    def __init__(self):
        self.head = None # Reference to head node
        self.tail = None
        self.size = 0 # Size of Linked List

    class Node:
        __slots__ = "data", "next"

        def __init__(self, element, next):
            self.data = element 
            self.next = next
    
    def is_empty(self):
        return self.size == 0
    
    #Takes the last item in the list and removes it from the list
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        last = self.tail.data
        self.size -= 1
        index = self.head
        for l in range(self.size-1):
            index = index.next
        self.tail = index
        self.tail.next = None
        if self.is_empty():
            self.head = None
            self.tail = None

        return last

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

class BST:
    '''
    This is a BST class that you will work on, you can define additional helper functions but do not change current member functions and variables
    '''

    def __init__(self):
        self.root = None # Reference to root of BST

    class BSTNode:
    # Class for Binary Search Tree Node
        __slots__ = "data", "left", "right"

        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = left
            self.right = right
        
        def insert_after(self, data):
            if data < self.data:
                if self.left:
                    self.left.insert_after(data)
                else:
                    self.left = BST.BSTNode(data)
            elif data > self.data:
                if self.right:
                    self.right.insert_after(data)
                else:
                    self.right = BST.BSTNode(data)

        def print(self):
            if self: 
                if self.left:
                    self.left.print()
                print(self.data)
                if self.right:
                    self.right.print()
    
    def insert(self, e):
        if self.root==None:
            self.root=self.BSTNode(e)
        else:
            self.root.insert_after(e)
    
    def print_inorder(self):
        if self.root: 
            self.root.print()


def create_lists(filename):
    
    L1 = LinkedList()
    L2 = LinkedList()
    s = []
    
    fID1 = open(filename, "r")
    for l in fID1:
        s.append(list(map(int, l.split()))[:])

    for l in s[0]:
        L1.insert_last(l)
    for l in s[1]:
        L2.insert_last(l)

    fID1.close()
    return L1,L2

def optional_concatenate(L1, L2, listToReverse): 
    
    L3 = LinkedList()
    con = int(listToReverse[-1])
    temp_list = []

    index_1 = L1.head
    index_2 = L2.head
    if (index_1 == None and index_2 == None):
        print("Both lists are empty!")
        return L3

    if con == 1:
        index_1 = L1.tail
        while (index_1 != None or index_2 != None):
            if index_1 != None:
                last = L1.pop()
                L3.insert_last(last)
                temp_list.append(last)
                index_1 = L1.tail
            if index_2 != None:
                L3.insert_last(index_2.data)
                index_2 = index_2.next
        temp_list.reverse()
        for l in temp_list:
            L1.insert_last(l)
    
    if con == 2:
        index_2 = L2.tail
        while (index_1 != None or index_2 != None):
            if index_1 != None:
                L3.insert_last(index_1.data)
                index_1 = index_1.next
            if index_2 != None:
                last = L2.pop()
                L3.insert_last(last)
                temp_list.append(last)
                index_2 = L2.tail
        temp_list.reverse()
        for l in temp_list:
            L2.insert_last(l)

    return L3

def LinkedList2BST(L2):

    BST1 = BST()
    temp_list = []
    L_temp = LinkedList()
    index_2 = L2.tail
    
    while (index_2 != None):
        last = L2.pop()
        L_temp.insert_last(last)
        temp_list.append(last)
        index_2 = L2.tail
    temp_list.reverse()
    for l in temp_list:
        L2.insert_last(l)

    index_temp = L_temp.tail

    while (index_temp != None):
        BST1.insert(L_temp.pop())
        index_temp = L_temp.tail
    
    return BST1