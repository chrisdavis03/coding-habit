##https://realpython.com/linked-lists-python/

'''
They can be used to implement (spoiler alert!) queues or stacks as well as graphs. 
They're also useful for much more complex tasks, 
such as lifecycle management for an operating system application.
'''

##Queues or Stacks
#Queue and Stacks differ on in the way elements are retrieved. 
#Queues are First In/First Out(FIFO)
#Stacks are Last In/First Out(LIFO)

##Graphs
#Graphs can be used to show relationships between objects or to represent different types of networks. 

'''
Since the difference in memory usage between lists and linked lists is so insignificant, 
it’s better if you focus on their performance differences when it comes to time complexity.
'''
'''
inserting elements at the end of a list using .append() or .insert() will have constant time, O(1),
when you try inserting an element closer to or at the beginning of the list, the average time complexity will 
grow along with the size of the list: O(n). Linked lists, on the other hand, are much more straightforward 
when it comes to insertion and deletion of elements at the beginning or end of a list, 
where their time complexity is always constant: O(1).
'''
