
# Q1: Implement a function to serialize and deserialize a binary tree.

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def serialize(root):
    if not root:
        return "None"
    return str(root.val) + "," + serialize(root.left) + "," + serialize(root.right)

def deserialize(data):
    values = data.split(',')
    return build_tree(values)

def build_tree(values):
    val = values.pop(0)
    if val == "None":
        return None
    node = TreeNode(int(val))
    node.left = build_tree(values)
    node.right = build_tree(values)
    return node


# Q2: Write a function to find the diameter of a binary tree.

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def diameter_of_binary_tree(root):
    def height(node):
        if not node:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        diameter_of_binary_tree.result = max(diameter_of_binary_tree.result, left_height + right_height)
        return 1 + max(left_height, right_height)

    diameter_of_binary_tree.result = 0
    height(root)
    return diameter_of_binary_tree.result


# Q3: Implement a function to construct a Huffman tree from a given set of frequencies.

import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def construct_huffman_tree(frequencies):
    heap = [HuffmanNode(char, freq) for char, freq in frequencies]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged_node = HuffmanNode(None, node1.freq + node2.freq)
        merged_node.left = node1
        merged_node.right = node2

        heapq.heappush(heap, merged_node)

    return heap[0]


# Q4: Implement AVL tree insertion and deletion operations.

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if not node:
        return 0
    return node.height

def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def left_rotate(node):
    new_root = node.right
    node.right = new_root.left
    new_root.left = node

    update_height(node)
    update_height(new_root)

    return new_root

def right_rotate(node):
    new_root = node.left
    node.left = new_root.right
    new_root.right = node

    update_height(node)
    update_height(new_root)

    return new_root

def avl_insert(root, key):
    if not root:
        return TreeNode(key)

    if key < root.val:
        root.left = avl_insert(root.left, key)
    else:
        root.right = avl_insert(root.right, key)

    update_height(root)

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.val:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.val:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

def avl_delete(root, key):
        pass

# Q5: Write functions to perform rotations (left and right) in an AVL tree.
def left_rotate(node):
    new_root = node.right
    node.right = new_root.left
    new_root.left = node

    update_height(node)
    update_height(new_root)

    return new_root

def right_rotate(node):
    new_root = node.left
    node.left = new_root.right
    new_root.right = node

    update_height(node)
    update_height(new_root)

    return new_root


