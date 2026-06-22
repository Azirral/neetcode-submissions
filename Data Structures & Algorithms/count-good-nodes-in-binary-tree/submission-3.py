# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Input: root - root of the binary tree
# Output: count - count of "good" nodes
# What determines a good node?
# A node is considered "good" if it is bigger or equal to the maximum node in the path to the node
# Intuition: Maintain a maximum value in the path by passing it to the dfs function
#            if the root is none, then we simply return (base case)
#            That way we can increment the count each time, that the current value is greater than or equal to the UpTillNow maximum value
#            Having the count incremented we take a maximum of the current node and the maximum
#            The maximum has to be equal to float -infinity, so that the root of the original tree is always bigger than the maximum, provided that it isn't None of course
#            Then, we pass the maximum to the dfs function and we return the count.

class Solution:
    def __init__(self, count = 0):
        self.count = count
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maximum):
            if not root:
                return
            
            if root.val >= maximum:
                self.count += 1
                maximum = max(root.val, maximum)
            
            dfs(root.left, maximum)
            dfs(root.right, maximum)

            return
        
        dfs(root, float("-inf"))
        return self.count
        