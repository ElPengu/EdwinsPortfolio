class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def invertTree(self, root: TreeNode)->TreeNode:
        # Quite a popular problem
        # Trivia: quite a good engineer at Google failed this problem!
        # We want to visit every node. Look at its
        # two children and swap the positions
        # 
        # We need a DFS solution. I.e. we go as deep 
        # as possible

        # If there is no root, nothing to do!
        if not root:
            return None
        
        # Swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # Now we invert these children
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


if __name__ == "__main__":
    sol = Solution()
    # root = [1,2,3,4,5,6,7]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(sol.invertTree(root)) # [1,3,2,7,6,5,4]

    # root = [3,2,1]
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(1)
    print(sol.invertTree(root)) # [3,1,2]

    # root = []
    root = None
    print(sol.invertTree(root)) # []

