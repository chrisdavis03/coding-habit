import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from models.binary_tree import BinaryTreeNode

'''Left, Root, Right'''

def dfs_inorder_recursive(root):
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result

def dfs_inorder_recursive_02(root):
    '''use to retype for retention and muscle memory'''
    result = []
    def dfs(node):
        if not node:
            return

        dfs(node.left)
        result.append(node.left)
        dfs(node.right)
    dfs(root)
    return result


def dfs_inorder_iterative(root):
    if not root:
        return
    result = []
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result
        
def dfs_inorder_iterative_02(root):
    '''use to retype for retention and muscle memory'''
    pass


if __name__ == '__main__':
    root = BinaryTreeNode('root')
    root.left = BinaryTreeNode('l')
    root.right = BinaryTreeNode('r')
    root.left.left = BinaryTreeNode('ll')
    root.left.right = BinaryTreeNode('lr')
    root.right.left = BinaryTreeNode('rl')
    root.right.right = BinaryTreeNode('rr')

    resultR = dfs_inorder_recursive(root=root)
    print (resultR)
    resultI = dfs_inorder_iterative(root=root)
    print (resultI)
    resultNone = dfs_inorder_iterative(root=None)
    print (resultNone)