from binarytree import build

# tree builds like 1st line - 3 2nd line - 6 and 8 - 3rd - 2, 11, None, 13, etc.

nodes = [3, 6, 8, 2, 11, None, 13, 22, 14, 41, 37, None, None, 71, 20]
binary_tree = build(nodes)
print("Binary tree from list :\n", binary_tree)
print('\nList from binary tree: ', binary_tree.values)
