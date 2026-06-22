# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Input: root - tree to look through if contains the other argument from the input: subtree,
#        subRoot - tree to look for in root 
# Output: True -> there exists a subtree subRoot in root tree, else False

# Pretty straightforward:
# Brute-force solution would be to write out the whole tree as an array (it can be an array of course)
# Then iterate through the array, and iterate through the subtree, checking if each node matches 
# returning False after the main loop ends if no such subtree was found

# Intuition:
# Iterate with dfs through whole tree, marking the nodes value in the original tree that match the value
# Of the node in the subtree
# If the match is found, call the isSameTree function, and if the result is true, break and return the True value
# Else look for the matching node in the child subtrees.
# It is actually easy for the subtree to exist its nodes must contain all of the descendant nodes of the original tree.
# So the same approach can be followed

# Pseudocode:
# result = False
# if 

class Solution:
    def __init__(self, res = False):
        self.res = False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            
        if root and root.val == subRoot.val:
            self.res = True if (isSameTree(root, subRoot) or self.res) else False
        if root:
            self.res = True if (self.isSubtree(root.left, subRoot) or self.res) else False
            self.res = True if (self.isSubtree(root.right, subRoot) or self.res) else False
            
        return self.res



        
        