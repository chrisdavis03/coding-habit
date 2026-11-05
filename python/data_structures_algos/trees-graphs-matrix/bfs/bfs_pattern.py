from collections import deque

def bfs(start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        # process node here
        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def graph_bfs(root):
    visited = set()
    result = []
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        result.append(node.val)
        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

def tree_bfs(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        for child in node.children:   # or node.left / node.right
            queue.append(child)
    return result

def b_tree_bfs(root):
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


    