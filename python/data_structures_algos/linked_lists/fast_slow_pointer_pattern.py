import random
from linked_lists import LinkedList, Node

def find_middle(head):
    slow = head
    fast = head

    # Move until fast reaches the end
    while fast is not None and fast.next is not None:
        slow = slow.next          # move slow by 1
        fast = fast.next.next     # move fast by 2

    return slow  # slow is at the middle

def has_cycle(head) -> bool:
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
        
    return False

if __name__ == '__main__':
    random.seed(1)
    my_list = LinkedList()

    for i in range(9):
        my_list.append(random.randint(1, 100))

    head = my_list.get(0)
    my_list.display()
    middle = find_middle(my_list.get(0))
    tail = my_list.get(my_list.length()-1)
    print (has_cycle(head))
    # Create a cycle
    tail.next = (my_list.get(4))

    print (has_cycle(head))

