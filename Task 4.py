class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(nodes, index):
    if index < len(nodes):
        if nodes[index] is None:
            return None
        root = TreeNode(nodes[index])
        root.left = buildTree(nodes, 2 * index + 1)
        root.right = buildTree(nodes, 2 * index + 2)
        return root
    return None

def print_tree(root, level=0, prefix='Binary Tree:\nRoot: '):
    if root is not None:
        print(' ' * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, 'L: ')
            print_tree(root.right, level + 1, 'R: ')

def vertical_order_traversal(root):
    if not root:
        return []

    column_table = {}
    queue = [(root, 0)]

    while queue:
        node, column = queue.pop(0)
        if column in column_table:
            column_table[column].append(node.val)
        else:
            column_table[column] = [node.val]

        if node.left:
            queue.append((node.left, column - 1))
        if node.right:
            queue.append((node.right, column + 1))

    result = []
    for key in sorted(column_table.keys()):
        result.append(column_table[key])
    return result

values = [3, 9, 20, None, None, 15, 7]
# values = [1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, 8, None, 9]
# values = [1,
#           2, 3,
#           4, 5, 6, 7,
#           None, None, None, None, None, None, 8, 9,
#           None, None, None, None, None, None, None, None, None, None, None, None, None, None, 10, 11,
#           None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#           None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 12]
print(f"Values used to create BT: {values}")
rt = buildTree(values, 0)
print_tree(rt)

vertical_order_result = vertical_order_traversal(rt)
print(f"Vertical Order Traversal: {vertical_order_result}")
