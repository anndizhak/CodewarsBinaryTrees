"""
This module provides functions for binary tree traversal: 
Pre-order, In-order, and Post-order.
"""
# Pre-order traversal
def pre_order(node):
    """Returns a list of data from the tree in Root-Left-Right order."""
    info = []
    if not node:
        return []
    info.append(node.data)
    info = info + pre_order(node.left) + pre_order(node.right)
    return info

# In-order traversal
def in_order(node):
    """Returns a list of data from the tree in Left-Root-Right order."""
    info = []
    if not node:
        return []
    info = in_order(node.left) + [node.data] + in_order(node.right)
    return info

# Post-order traversal
def post_order(node):
    """Returns a list of data from the tree in Left-Right-Root order."""
    info = []
    if not node:
        return []
    info = post_order(node.left) + post_order(node.right) + [node.data]
    return info
