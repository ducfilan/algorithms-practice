function nodeDepths(root) {
  return calculateDepthSum(root, 0)
}

function calculateDepthSum(node, currentDepth) {
  if (isLeaf(node)) {
    return currentDepth
  }

  let depthSum = currentDepth

  if (node.left) {
    depthSum += calculateDepthSum(node.left, currentDepth + 1)
  }

  if (node.right) {
    depthSum += calculateDepthSum(node.right, currentDepth + 1)
  }

  return depthSum
}

function isLeaf(node) {
  return node.left === null && node.right === null
}

// This is the class of the input binary tree.
class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// Do not edit the line below.
exports.nodeDepths = nodeDepths;
