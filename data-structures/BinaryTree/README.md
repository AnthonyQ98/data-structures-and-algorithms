Trees have a root node and one or many child nodes, of which have child nodes.

A node with no children is a leaf node.

Binary trees have at most child nodes, of which each child can have max two child nodes.

Tree traversal is the order in which you visit each node in a tree.

- Pre-order traversal visits the root node, then the left sub tree recursively, then the right sub tree recursively. Can work in binary trees or regular trees, but lets look at a binary tree example below.
  - Think of a 2 chaper, multiple section book as an example. The book would be the root node. Chapter 1 would be the left child node of the root node (book) and chapter 2 would be the right child node of the root node (book). Then section 1.1 would be the left child node of the Chaper 1 node. Section 1.2 would be the right child node of the Chaper 1 node. The same logic would apply for the Chapter 2 node.

- In-order traversal visits the left sub-tree, then the root node, then the right sub-tree.

- Post-order travel visits the left sub-tree, then the right sub-tree then the root node.

A complete binary tree is one in which all child nodes are filled on each level of the tree except the lastl level, to which the nodes must be filled from left-to-right, but does not need to be fully complete.

