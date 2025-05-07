from typing import List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # All values in the tree are unique. This is
        # critical
        #
        # So the preorder and inorder do not have 
        # nulls!
        # Preorder: Root, left subtree, right subtree
        # Inorder: Left subtree, root, right subtree
        # 
        # Two main facts
        # FACT 1: The first value in pre-order 
        # traversal is the ROOT
        # FACT 2: Every value LEFT to the root
        # seen in the pre-order traversal is in 
        # the roots LEFT subtree, and those values
        # RIGHT of the root is in the roots RIGHT 
        # subtree
        # 
        # We begin by setting the root as a node.
        # We move on to deciding its left and right
        # subtrees!
        # 
        # We find the POSITION of this value 
        # in the IN-ORDER traversal and note that 
        # all values to the LEFT go in the LEFT 
        # SUBTREE, and those to the RIGHT go in 
        # the RIGHT subtree.
        # Refer to the definition of IN-ORDER 
        # traversal to understand WHY.
        # 
        # So we have the in-order traversals for the
        # left and right subtrees
        # 
        # Okay, but how do we know which value is 
        # that of the ROOT's LEFT and 
        # RIGHT children? 
        # 
        # The pre-order traversal maintains the
        # ordering of descendants! So we take 
        # the LENGTHS of the LEFT and RIGHT 
        # subarrays in the in-order traversal 
        # and use them to find the LEFT and RIGHT 
        # subarrays in the pre-order traversal.
        # 
        # Specifically, the LEFT subarray will be
        # all values directly AFTER the root value
        # in the pre-order traversal, and the RIGHT
        # subarray will be all values directly AFTER
        # the LEFT subarray
        # 
        # So now we have the left subtree pre-order
        # and in-order traversals, and the right 
        # subtree pre-order and in-order traversals
        # 
        # All that is left is to set the root's left 
        # child to whatever the returned is from 
        # calling buildTree on the left subtree as 
        # described by its associated pre-order and 
        # in-order traversals.
        # Ditto for the right subtree.
        # 
        # This is a long explanation, but I think 
        # it is crucial to understand exactly HOW
        # the code expresses the concept of using 
        # the pre-order and in-order traversals 
        # 
        # 

        # We start with base case of no nodes
        if not preorder or not inorder:
            return None
        
        # We create a tree node with the first value 
        # in pre-order array
        root = TreeNode(preorder[0])

        # Find position of root in inorder
        mid = inorder.index(preorder[0])


        # Now we build the tree using the new preorder
        # and inorder arrays

        # Skip the 0 index for preorder up to mid
        # For inorder we take all elements entirely
        # to the LEFT of the root, i.e. up to mid
        root.left = self.buildTree(preorder[1:mid+1],
                                   inorder[:mid])
        
        # Go from mid+1 up to end for preorder, 
        # these are the nodes to the right of 
        # the root in order of being roots
        # For inorder we want all elements to the 
        # right OF mid
        root.right = self.buildTree(preorder[mid+1:],
                                    inorder[mid+1:])

        


if __name__ == "__main__":
    sol = Solution()

    preorder = [1,2,3,4]
    inorder = [2,1,3,4]
    print(sol.buildTree(preorder, inorder)) # [1,2,3,null,null,4]

    preorder = [1]
    inorder = [1]
    print(sol.buildTree(preorder, inorder)) # [1]