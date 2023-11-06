class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(nodes, index):
    if index < len(nodes):
        if nodes[index] is None:
            return None
        root1 = TreeNode(nodes[index])
        root1.left = buildTree(nodes, 2 * index + 1)
        root1.right = buildTree(nodes, 2 * index + 2)
        return root1
    return None

def print_tree(root2, level=0, prefix='Binary Tree:\nRoot: '):
    if root2 is not None:
        print(' ' * (level * 4) + prefix + str(root2.val))
        if root2.left is not None or root2.right is not None:
            print_tree(root2.left, level + 1, 'L: ')
            print_tree(root2.right, level + 1, 'R: ')

def postorderTraversal(root3):
    result = []
    stack = []
    prev = None

    while root3 or stack:
        if root3:
            stack.append(root3)
            root3 = root3.left
        else:
            peek = stack[-1]
            if peek.right and prev != peek.right:
                root3 = peek.right
            else:
                result.append(peek.val)
                prev = stack.pop()
    return result

values = [11, 12, 22, 32, 24, 55, 33]
print(f"Values used to create BT: {values}")
root = buildTree(values, 0)
print_tree(root)
res = postorderTraversal(root)
print("Postorder Traversal: ", res)
