import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from models.binary_tree import BinaryTreeNode
from collections import deque

def bfs_level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def bfs_level_order_002(root):
    '''use to retype for retention and muscle memory'''
    pass
    if not root:
        return []
    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


if __name__ == '__main__':
    root = BinaryTreeNode('root')
    root.build_example()

    result = bfs_level_order(root)
    print (result)\
    
    result = bfs_level_order_002(root)
    print (result)