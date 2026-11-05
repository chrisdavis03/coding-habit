import { BTreeNode } from "../models/binary_tree.js"

class NAryNode {
    constructor(val = 0, children = []) {
        this.val = val
        this.children = children
    }
}

const dfsPreOrderRecursive = (root) => {
    const result = []
    const dfs = (node) => {
        if (!node) return 
        result.push(node.val)
        dfs(node.left)
        dfs(node.right)
    }
    dfs(root)
    return result
}

const dfsPreOrderRecursive2 = (root) => {
    const result = []
    const dfs = (node) => {
        if (!node) return
        result.push(node.val)
        dfs(node.left)
        dfs(node.right)
    }
    dfs(root)
    return result
}

const dfsPreOrderIterative = (root) => {
    if (!root) return
    const result = []
    const stack = [root]
    while (stack.length) {
        const node = stack.pop()
        result.push(node.val)
        if (node.right) stack.push(node.right)
        if (node.left) stack.push(node.left)
    }
    return result
}


const root = new BTreeNode('R')
root.left = new BTreeNode('l')
root.left.left = new BTreeNode('ll')
root.left.right = new BTreeNode('lr')
root.right = new BTreeNode('r')
root.right.left = new BTreeNode('rl')
root.right.right = new BTreeNode('rr')

const result = dfsPreOrderRecursive(root)
console.log(result)
const result2 = dfsPreOrderRecursive2(root)
console.log(result2)
const resultI = dfsPreOrderIterative(root)
console.log(resultI)
