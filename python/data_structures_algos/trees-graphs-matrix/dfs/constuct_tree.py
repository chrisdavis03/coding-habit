import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from models.binary_tree import BinaryTreeNode

if __name__ == '__main__':
    root = BinaryTreeNode('R')
    print (root)

    root.build_example()
    print (root.left.left)