import { BTreeNode } from "../models/binary_tree.js";

const dfsInOrderRecursive = (root) => {
    const result = []
    const dfs = (node) => {
        if (!node) return
        dfs(node.left)
        result.push(node.val)
        dfs(node.right)
    }
    dfs(root)
    return result
}

const dfsInOrderRecursive02 = (root) => {
    const result = []
    const dfs = (node) => {
        if (!node) return
        dfs(node.left)
        result.push(node.val)
        dfs(node.right)
    }
    dfs(root)
    return result
}

const dfsInOrderIterative = (root) => {
    const result = [];
    const stack = [];
    let current = root;

    while (stack.length || current) {
        while (current) {
            stack.push(current);
            current = current.left;
        }
        current = stack.pop();
        result.push(current.val);
        current = current.right;
    } 
    return result;
}

const dfsInOrderIterative2 = (root) => {
    const result = [];
    const stack = [];
    let current = root;

    while (stack.length || current) {
        while (current) {
            stack.push(current)
            current = current.left
        }
        current = stack.pop()
        result.push(current.val)
        current = current.right
    }
    return result
}

const root = new BTreeNode('ROOT')
root.left = new BTreeNode('l')
root.left.left = new BTreeNode('ll')
root.left.right = new BTreeNode('lr')
root.right = new BTreeNode('r')
root.right.left = new BTreeNode('rl')
root.right.right = new BTreeNode('rr')

const result = dfsInOrderRecursive(root)
console.log(result)
const result2 = dfsInOrderRecursive02(root)
console.log(result2)
const resultI = dfsInOrderIterative(root)
console.log(resultI)
const resultI2 = dfsInOrderIterative2(root)
console.log(resultI2)