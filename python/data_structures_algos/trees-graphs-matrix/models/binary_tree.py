class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        ## Good use for bfs!
        x = 5
        return f"""{'*'*4*x}\n{' '*2*x}{self.val}   
{' '*x}{self.left.val if hasattr(self.left, 'val') else 'x'}{' '*2*x}{self.right.val if hasattr(self.right, 'val') else 'x'}"""
    def build_example(self):
        self.left = BinaryTreeNode('l')
        self.right = BinaryTreeNode('r')
        self.left.left = BinaryTreeNode('ll')
        self.left.right = BinaryTreeNode('lr')
        self.right.left = BinaryTreeNode('rl')
        self.right.right = BinaryTreeNode('rr')
        
        return self
# N-ary Trees have an arbitrary number of children. 
class NAryNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []