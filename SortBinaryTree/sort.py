"""
This module provides a function to traverse a binary tree level by level.
It uses a Breadth-First Search (BFS) approach with an efficient queue.
"""
from collections import deque
class Node:
    """Represents a node in a binary tree with left, right, and value properties."""
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    """
    Traverses the tree level by level (from top to bottom, left to right).
    Returns a list of values in the order they were visited.
    """
    if not node:
        return None
    result = []
    queue = deque([node])
    while queue:
        curr = queue.popleft()
        result.append(curr.value)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return result