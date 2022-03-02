# return all distinct binay trees with a specified number of nodes.
# input = 3
# output = (distinct five different tree)
#   0       0       0        0       0 
#    \       \     / \      /       /
#     0       0   0   0    0       0
#      \     /               \    /
#       0   0                 0  0

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def generateBinaryTree(num):
    if num == 0: return [None]

    result = []
    for leftNode in range(num):
        rightNode = num - leftNode - 1
        leftTree = generateBinaryTree(leftNode)
        rightTree = generateBinaryTree(rightNode)
        result += [TreeNode(0, left, right) for left in leftTree for right in rightTree]

    return result

def preorder(root):
    traversal = []
    def recursive(root):
        if root:
            traversal.append(root.value)
            recursive(root.left)
            recursive(root.right)
        else:
            traversal.append('#')
        
    recursive(root)
    return traversal

# return all Full Binary Tree with a specified number of nodes
def clone(tree):
    if not tree: return None
    new = TreeNode(0)
    new.left = clone(tree.left)
    new.right = clone(tree.right)
    return new

def generateFullBinaryTree(n):
    # n must be odd to form a full binary tree
    if not n & 1: return []
    elif n == 1: return [TreeNode(0)]

    result = []
    for i in range(2, n+1, 2):
        leftTree = generateFullBinaryTree(i - 1)
        rightTree = generateFullBinaryTree(n - i)
        for leftCount, left in enumerate(leftTree):
            for rightCount, right in enumerate(rightTree):
                tree = TreeNode(0)
                tree.left = clone(left) if rightCount < len(rightTree) else left
                tree.right = clone(right) if leftCount < len(leftTree) else right
                result.append(tree)
    return result

# test case
binarytrees = generateBinaryTree(3)
for tree in binarytrees:
    print(preorder(tree))

fulltrees = generateFullBinaryTree(7)
for tree in fulltrees:
    print(preorder(tree))