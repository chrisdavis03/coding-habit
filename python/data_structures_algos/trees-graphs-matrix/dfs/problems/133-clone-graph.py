class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
            

def cloneGraph(node: Node) -> Node:
    if not node:
        return
    copied = {}

    def dfs(cur:Node):
        print (type(cur))
        if cur in copied:
            return copied[cur]
        clone = Node(cur.val, [])
        copied[cur] = clone

        for neighbor in cur.neighbors:
            clone_neighbors = dfs(neighbor)
            clone.neighbors.append(clone_neighbors)
        return clone

    return dfs(node)

if __name__ == '__main__':
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    #construct Graph
    node1 = Node(val=1, neighbors=[])
    node2 = Node(val=2, neighbors=[])
    node3 = Node(val=3, neighbors=[])
    node4 = Node(val=4, neighbors=[])

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    
    print (cloneGraph(node1))
    

