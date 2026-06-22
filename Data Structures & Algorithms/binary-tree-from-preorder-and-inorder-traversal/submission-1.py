# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Input: preorder - nodes presented in the order of parent, leftchild, right child - Breadth First Search representation of the tree
        #        inorder - nodes presented in the order of leftchild, parent, right child - Depth First Search representation of the tree
        # Output: root of the constructed treee
        # Intuition: 1. Take the first value from the preorder and parse it as the root
        #            2. Find the value in the inorder list
        #            3. Partition the preorder tree based on the index of the found value (:index) - left subtree, (index:) - right subtree
        #            4. always return the root,
        if not preorder:
            return None 
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
        