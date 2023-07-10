class LinkedList:
    '''
    This is a Linked List class that you will work on, you can define additional helper functions but do not change current member functions and variables (e.g, cant make doubly linked list)
    '''
    def __init__(self):
        self.head = None # Reference to head node
        self.size = 0 # Size of Linked List

    class Node:
        def __init__(self, element, next):
            self.data = element 
            self.next = next

    def insert_last(self, e):
        '''
        Implement this function such that given data e you will add new node with data e to the end of Linked List
        '''
        pass

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
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = left
            self.right = right

    def insert(self, e):
        '''
        Implement this function such that given data e you will add new bst node into the correct position in the tree 
        '''
        pass

    def print_inorder(self):
        '''
        Implement this function to print the contents of the BST with inorder traversal
        '''


def create_lists(filename):
    '''
    This function is used to create Linked List objects with input given in filename
    '''
    pass

def optional_concatenate(L1, L2, listToReverse): 
    '''
    Implement the function asked in Task 1
    '''
    pass

def LinkedList2BST(LL):
    '''
    Implement the function asked in Task2
    '''
    pass


