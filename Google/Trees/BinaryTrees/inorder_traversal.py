class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def inorder_traversal(root):
    list = []
    if root:
        list += inorder_traversal(root.left)
        list.append(root.val)
        list += inorder_traversal(root.right)
    return list
