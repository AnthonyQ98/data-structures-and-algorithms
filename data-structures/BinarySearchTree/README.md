# Binary Search Tree (BST) Documentation

A **Binary Search Tree** (BST) is a binary tree data structure that stores values in an organized way to allow efficient searching, insertion, and deletion operations. Each node in a BST follows specific properties:

- **Left Subtree Property**: Nodes in the left subtree of a given node have values smaller than the node's value.
- **Right Subtree Property**: Nodes in the right subtree of a given node have values greater than the node's value.
- **Binary Property**: Each node can have at most two child nodes, making it a "binary" tree.

This organization enables fast search, insert, and delete operations, often used in various applications that require data to be accessed or manipulated quickly.

## Table of Contents
- [Overview](#overview)
- [Properties of a Binary Search Tree](#properties-of-a-binary-search-tree)
- [Common Operations](#common-operations)
  - [Search](#search)
  - [Insertion](#insertion)
  - [Deletion](#deletion)
- [Tree Traversal Methods](#tree-traversal-methods)
  - [In-Order Traversal](#in-order-traversal)
  - [Pre-Order Traversal](#pre-order-traversal)
  - [Post-Order Traversal](#post-order-traversal)
- [Applications of Binary Search Trees](#applications-of-binary-search-trees)
- [Time Complexity](#time-complexity)

## Overview
A Binary Search Tree is a hierarchical data structure that organizes values in a sorted order. By following the left-right property described above, a BST enables efficient search and data retrieval operations. Starting from the root node, we can navigate left or right depending on whether a value is smaller or larger, allowing us to efficiently locate or manage data within the tree.

## Properties of a Binary Search Tree
- **Uniqueness**: Each value in the BST is unique; duplicates are not allowed.
- **Ordering**: Values in the left subtree of any node are always smaller than the node’s value, and values in the right subtree are always greater.
- **Height**: The height of a BST directly affects its efficiency. In an ideally balanced BST, the height is `O(log n)`, optimizing operations. However, an unbalanced BST may degrade to a linked list structure with a height of `O(n)`.

## Common Operations

### Search
To locate a specific value in the BST:
1. Start at the root node.
2. Compare the target value with the current node’s value.
   - If equal, the search is successful.
   - If smaller, continue the search in the left subtree.
   - If larger, continue the search in the right subtree.
3. Repeat until the value is found or a leaf node is reached, which indicates the value is not in the tree.

### Insertion
To add a new value to the BST:
1. Begin at the root node and use the same left/right rule to find the correct location.
2. Continue moving left or right until an appropriate leaf position is found.
3. Insert the new node as a child of the last node reached.

### Deletion
To remove a node with a specific value from the BST:
1. **Node with no children**: Simply remove the node.
2. **Node with one child**: Replace the node with its child.
3. **Node with two children**: Replace the node with its in-order successor (smallest node in the right subtree) or in-order predecessor (largest node in the left subtree), and then delete that successor or predecessor node.

## Tree Traversal Methods
Traversals are methods to visit each node in the BST in a specified order. Common traversal techniques include:

### In-Order Traversal
- Visits nodes in ascending order.
- Steps:
  1. Traverse the left subtree.
  2. Visit the root node.
  3. Traverse the right subtree.

### Pre-Order Traversal
- Visits the root node before its subtrees.
- Steps:
  1. Visit the root node.
  2. Traverse the left subtree.
  3. Traverse the right subtree.

### Post-Order Traversal
- Visits the root node after its subtrees.
- Steps:
  1. Traverse the left subtree.
  2. Traverse the right subtree.
  3. Visit the root node.

## Applications of Binary Search Trees
Binary Search Trees are used in a variety of applications:
- **Database Indexing**: Manage records for quick lookup and retrieval.
- **Searching Algorithms**: Quickly locate specific data in sorted datasets, such as in dictionaries or phonebooks.
- **Sorting**: In-order traversal of a BST provides elements in sorted order.
- **Autocomplete Systems**: Use prefix-based trees to suggest potential search terms in search engines.

## Time Complexity
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Search    | O(log n)     | O(n)       |
| Insertion | O(log n)     | O(n)       |
| Deletion  | O(log n)     | O(n)       |

**Note**: When the BST is balanced, operations are efficient (`O(log n)`). However, in the worst-case scenario (e.g., inserting nodes in sorted order), the BST becomes unbalanced, resulting in `O(n)` complexity for operations.
