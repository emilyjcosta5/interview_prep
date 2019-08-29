# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preorder_traversal(root):
    list = []
    if root:
        list.append(root.val)
        list += preorder_traversal(root.left)
        list += preorder_traversal(root.right)
    return list
       
if __name__=="__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    list = preorder_traversal(root = root)
    print(list)
