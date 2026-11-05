import { BTreeNode } from "../models/binary_tree.js";

const bfsLevelOrder = (root) => {
    if (!root) return []
    const result = []
    const queue = [root]

    while (queue.length) {
        const node = queue.shift()
        result.push(node.val)
        if (node.left) queue.push(node.left)
        if (node.right) queue.push(node.right)
    }
    return result
}

const bfsLevelOrder_02 = (root) => {
    if (!root) return []
    const result = []
    const queue = [root]

    while (queue.length) {
        const node = queue.shift()
        result.push(node.val)
        if (node.left) queue.push(node.left)
        if (node.right) queue.push(node.right)
    }

    return result
}

const root = new BTreeNode('root')
root.left = new BTreeNode('l')
root.left.left = new BTreeNode('ll')
root.left.right = new BTreeNode('lr')
root.right = new BTreeNode('r')
root.right.left = new BTreeNode('rl')
root.right.right = new BTreeNode('rr')

const result = bfsLevelOrder(root)
console.log(result)
const result2 = bfsLevelOrder_02(root)
console.log(result2)