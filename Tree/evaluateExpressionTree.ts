// This is an input class. Do not edit.
export class BinaryTree {
  value: number;
  left: BinaryTree | null;
  right: BinaryTree | null;

  constructor(value: number) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

const Operator = {
  add: -1,
  sub: -2,
  div: -3,
  mul: -4,
}

export function evaluateExpressionTree(tree: BinaryTree) {
  let result: number

  if (isLeaf(tree)) {
    return tree.value
  }
  
  result = calcSum(tree!, 0)
  
  return result;
}

function isLeaf(node: BinaryTree) {
  return node.left === null && node.right === null
}

function calcSum(node: BinaryTree, result: number): number {
  if (node.value >= 0) return node.value

  return calc(calcSum(node.left!, result), calcSum(node.right!, result), node.value)
}

function calc(num1: number, num2: number, operator: number): number {
  switch (operator) {
    case Operator.add:
      return num1 + num2

    case Operator.sub:
      return num1 - num2

    case Operator.div:
      return Math.trunc(num1 / num2)

    case Operator.mul:
      return num1 * num2

    default:
      throw new Error("invalid operator")
  }
}
