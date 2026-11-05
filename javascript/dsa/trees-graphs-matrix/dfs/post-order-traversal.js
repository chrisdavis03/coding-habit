import { BTreeNode } from "../models/binary_tree.js";

const dfsPostOrderRecursive = (root) => {
    const result = []
    const dfs = (node) => {
        if (!node) return
        dfs(node.left)
        result.push(node.val)
        dfs(node.right)
    }
    dfs(root)
    return result.reverse()
}

const root = new BTreeNode('ROOT')
root.left = new BTreeNode('l')
root.left.left = new BTreeNode('ll')
root.left.right = new BTreeNode('lr')
root.right = new BTreeNode('r')
root.right.left = new BTreeNode('rl')
root.right.right = new BTreeNode('rr')

const result = dfsPostOrderRecursive(root)
console.log(result)