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
        
if __name__ == "__main__":
    tree_tuple = ((((3,5,2),3,5),3,None),2,((5,1,2),3,(1,5,(2,5,None))))
    print(tree_tuple)
    tree = tuple_to_tree(tree_tuple)
    print(tree_to_tuple(tree))
    print('---tree---'*5)
    visualize_tree(tree)
    print('---tree---'*5)
