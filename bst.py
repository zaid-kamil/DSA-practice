from typing import Any
class TreeNode:
    def __init__(self, key: Any) -> None:
        self.key = key
        self.left: TreeNode = None
        self.right: TreeNode = None

def tree_to_tuple(node: TreeNode):
    if node is None:
        return None
    elif node.left is None and node.right is None:
        return node.key
    return (tree_to_tuple(node.left), node.key, tree_to_tuple(node.right))

def tuple_to_tree(data):
    if data is None:
        return None
    elif isinstance(data, tuple) and len(data)== 3:
        node = TreeNode(data[1]) # middle
        node.left = tuple_to_tree(data[0])
        node.right = tuple_to_tree(data[2])
        return node
    else:
        return TreeNode(data)
    
def visualize_tree(node: TreeNode, space='\t', level=0):
    if node is None:
        print(space*level, "⛔")
        return
    if node.left is None and node.right is None:
        print(f'{space*level} {node.key}🥬')
        return
    visualize_tree(node.right, space, level+1)
    print(f'{space*level} ({node.key})')
    visualize_tree(node.left, space, level+1)

def traverse_inorder(node):
    if node is None:
        return []
    return traverse_inorder(node.left) + [node.key] + traverse_inorder(node.right)

def traverse_preorder(node):
    if node is None:
        return []
    return traverse_preorder

def height(node):
    if node is None: return 0
    return 1 + max(height(node.left), height(node.right))

def size(node):
    if node is None: return 0
    return 1 + size(node.left) + size(node.right)

def minDepth(node):
    # if the node is None, return 0
    if node is None:
        return 0
    # if the node has no left and right children, return 1
    if node.left is None and node.right is None:
        return 1
    # if the node has no left child, return the right child's depth + 1
    if node.left is None:
        return minDepth(node.right) + 1
    # if the node has no right child, return the left child's depth + 1
    if node.right is None:
        return minDepth(node.left) + 1
    # return the minimum depth of the left and right children + 1
    return min(minDepth(node.left), minDepth(node.right)) + 1   
    # complexity: O(n), n is the number of nodes in the tree

from collections import deque
def minDepthO(node):
    if not node: return 0
    q = deque([node])
    depth = 1
    while q:
        size = len(q)
        for _ in range(size):
            curr = q.popleft()
            if not curr.left and not curr.right:
                return depth
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
        depth += 1
    return depth # 
        
if __name__ == "__main__":
    tree_tuple = (1,2,(5,3,(2,5,(1,2,(1,2,3)))))
    print(tree_tuple)
    tree = tuple_to_tree(tree_tuple)
    print(tree_to_tuple(tree))
    print('---tree---'*5)
    visualize_tree(tree)
    print('---tree---'*5)

    print(traverse_inorder(tree))
    print(height(tree))
    print(size(tree))
