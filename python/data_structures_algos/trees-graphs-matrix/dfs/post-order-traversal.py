import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from models.binary_tree import BinaryTreeNode


def dfs_postorder_recursive(root):
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)
    dfs(root)
    return result

def dfs_postorder_recursive_02(root):
    pass

def dfs_postorder_iterative(root):
    if not root:
        return
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1] # reverse the output

if __name__ == '__main__':
    root = BinaryTreeNode('root')
    root.build_example()

    resultR = dfs_postorder_recursive(root=root)
    print (resultR)

    resultI = dfs_postorder_iterative(root=root)
    print (resultI)