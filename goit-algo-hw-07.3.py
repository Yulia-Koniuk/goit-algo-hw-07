class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

def delete_node(root, key):
    if not root:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)

    if root is None:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if get_balance(root.left) >= 0:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if get_balance(root.right) <= 0:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

def find_max_value(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.key

def find_min_value(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.key

def sum_values(root):
    if root is None:
        return 0
    return root.key + sum_values(root.left) + sum_values(root.right)

# Driver program to test the above functions
root = None
keys = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85, 5, 15, 27, 37, 47]

for key in keys:
    root = insert(root, key)
    print("Inserted:", key)
    print("AVL Tree:")
    print(root)

# Find max, min value and sum of all values
max_value = find_max_value(root)
min_value = find_min_value(root)
total_sum = sum_values(root)
print("Max value in the AVL Tree:", max_value)
print("Min value in the AVL Tree:", min_value)
print("Sum of all values in the AVL Tree:", total_sum)

# Delete
keys_to_delete = [5, 55]
for key in keys_to_delete:
    root = delete_node(root, key)
    print("Deleted:", key)
    print("AVL Tree:")
    print(root)

# Find max, min value and sum of all values after deletions
max_value = find_max_value(root)
min_value = find_min_value(root)
total_sum = sum_values(root)
print("Max value in the AVL Tree after deletions:", max_value)
print("Min value in the AVL Tree after deletions:", min_value)
print("Sum of all values in the AVL Tree after deletions:", total_sum)


"""
Max value in the AVL Tree: 85
Min value in the AVL Tree: 5
Sum of all values in the AVL Tree: 876

Max value in the AVL Tree after deletions: 85
Min value in the AVL Tree after deletions: 10
Sum of all values in the AVL Tree after deletions: 816
"""