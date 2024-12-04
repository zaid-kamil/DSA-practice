class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None:
            return []
        return TreeNode.traverse_in_order(self.left) + [self.key] + TreeNode.traverse_in_order(self.right)

    def display_tree(self, space='\t', level=0):
        if self is None:
            print(space*level, "⛔")
            return
        if self.left is None and self.right is None:
            print(f'{space*level} {self.key}🥬')
            return
        TreeNode.display_tree(self.right, space, level+1)
        print(f'{space*level} ({self.key})')
        TreeNode.display_tree(self.left, space, level+1)

    def to_tuple(self):
        if self is None:
            return None
        elif self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)

    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else: 
            node = TreeNode(data)
        return node
    
    def __str__(self):
        return f'BT{self.to_tuple()}'  
    
    def __repr__(self):
        return f'BT{self.to_tuple()}'
    

# Example usage
if __name__ == "__main__":
    tree_tuple = ((None, 1, 6), 2, ((5, 3, 5), 4, (5, 5, None)))
    root = TreeNode.parse_tuple(tree_tuple)
    print(root)
    print(root.height())
    print(root.size())
    print(root.traverse_in_order())
    root.display_tree()
    print(root.to_tuple())
