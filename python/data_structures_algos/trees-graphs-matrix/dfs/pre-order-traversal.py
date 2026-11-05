import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from collections import deque
from models.binary_tree import BinaryTreeNode

#Depth-First Search (DFS)

## Preorder Traversal
def dfs_preorder_recursive(root):
    result = []
    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return result

def dfs_preorder_recursive_02(root):
    '''use to retype for retention and muscle memory'''
    result=[]
    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return result


def dfs_preorder_iterative(root):
    if not root:
        return
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def dfs_preorder_iterative_02(root):
    '''use to retype for retention and muscle memory'''
    pass
    if not root:
        return
    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left: 
            stack.append(node.left)

    return result

if __name__ == '__main__':
    root = BinaryTreeNode('root')
    root.left = BinaryTreeNode('l')
    root.right = BinaryTreeNode('r')
    root.left.left = BinaryTreeNode('ll')
    root.left.right = BinaryTreeNode('lr')
    root.right.left = BinaryTreeNode('rl')
    root.right.right = BinaryTreeNode('rr')

    rootA = BinaryTreeNode(0)
    rootA.left = BinaryTreeNode(1)
    rootA.right = None

    result = dfs_preorder_iterative(root=root)
    print (result)

