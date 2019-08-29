class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def postorder_traversal(root):
    list = []
    if root:
        list += postorder_traversal(root.left)
        list += postorder_traversal(root.right)
        list.append(root.val)
    return list
