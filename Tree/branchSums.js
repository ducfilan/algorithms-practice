// This is the class of the input root.
// Do not edit it.
class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function branchSums(root) {
  let result = [];
  let sum = 0;
  getSum(sum, root, result);

  return result;
}

function getSum(sum, node, result) {
  if (node.left == null && node.right == null) {
    result.push(sum + node.value);
    return;
  }

  if (node.left) {
    getSum(sum + node.value, node.left, result)
  }

  if (node.right) {
    getSum(sum + node.value, node.right, result)
  }
}

// Do not edit the lines below.
exports.BinaryTree = BinaryTree;
exports.branchSums = branchSums;
