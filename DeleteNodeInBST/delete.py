"""
This module provides a solution for deleting a node from a Binary Search Tree (BST).
It maintains the BST property: left subtree < root < right subtree.
"""
# Definition for a binary tree node.
class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Task 3"""
    def deleteNode(self, root, key: int):
        """
        Deletes the node with the specified key from the BST and returns the new root.
        
        The process involves:
        1. Searching for the node.
        2. Handling three scenarios: no children, one child, or two children.
        3. Using the in-order successor (min node in right subtree) for the two-child case.
        """
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right and not root.left:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            min_node = root.right
            while min_node.left:
                min_node = min_node.left

            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        return root             