
##https://builtin.com/data-science/python-linked-list
##https://youtu.be/JlMyYuY1aXU
#linked lists are a way to store data in an ordered manner.
#has no strict linear ordering in memory. The ordering is controlled by the internals of the data structure. 

#single linked list
#only contains pointers to the next node. 

#double linked list
#contains pointers to both the next and previous node. 

#Complexities of Linked lists
##Access an element - O(n)
##Add/remove at an iterator position - O(1)
#Add/remove first element - O(1)
## Add last element - O(1)
## Remove Last element - O(n)

class Node: 
    def __init__(self, data=None):
        self.data=data
        self.next=None

#wrapper for individual nodes. 
class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        ## Add new data point to the end of the linked list.
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current != None:
            total += 1
            current = current.next
        return total

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next != None: 
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)
    
    def get(self, index):
        if index>=self.length():
            print ('ERROR - Index out of range!')
            return None
        cur_idx = 0 
        cur_node = self.head
        while True: 
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1
    def erase(self, index):
        if index>=self.length():
            print ('ERROR - Erase index out of range!')
            return None
        cur_idx = 0 
        cur_node = self.head
        while True: 
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index: 
                last_node.next = cur_node.next
                return
            cur_idx += 1



my_list = LinkedList()

my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()

my_list.erase(1)

my_list.display()