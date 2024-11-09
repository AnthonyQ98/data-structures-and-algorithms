# Tree Data Structure Documentation

In computer science, a **Tree** is a hierarchical data structure with a **root node** and one or many child nodes, each of which may also have its own child nodes. Trees are used to represent hierarchical relationships and can be applied in a variety of contexts, such as file systems, databases, and organizational structures.

## Table of Contents
- [Overview](#overview)
- [Types of Nodes](#types-of-nodes)
- [Binary Trees](#binary-trees)
- [Tree Traversal](#tree-traversal)
  - [Pre-Order Traversal](#pre-order-traversal)
  - [In-Order Traversal](#in-order-traversal)
  - [Post-Order Traversal](#post-order-traversal)
- [Complete Binary Tree](#complete-binary-tree)

## Overview
A tree is a hierarchical structure where each element is called a **node**. It has the following characteristics:
- **Root Node**: The top node in a tree.
- **Child Node**: A node that descends from another node.
- **Parent Node**: The node from which a child node descends.
- **Leaf Node**: A node with no children, representing the endpoints of branches in a tree.

## Types of Nodes
- **Root Node**: The top node of the tree from which all other nodes descend.
- **Leaf Node**: A node that has no children, indicating the end of a branch in the tree.

## Binary Trees
A **Binary Tree** is a specific type of tree where each node has at most two child nodes, commonly referred to as the **left** and **right** children. Each child node in a binary tree may have at most two children of its own.

## Tree Traversal
**Tree Traversal** refers to the process of visiting each node in a tree in a specific order. Common traversal methods include:

### Pre-Order Traversal
In **Pre-Order Traversal**, nodes are visited in the following order:
1. Visit the root node.
2. Traverse the left subtree recursively.
3. Traverse the right subtree recursively.

This traversal method works for both binary trees and general trees. For example, consider a book with two chapters and multiple sections:

- The book is the root node.
- **Chapter 1** is the left child of the root node (book), and **Chapter 2** is the right child.
- **Section 1.1** is the left child of the Chapter 1 node, and **Section 1.2** is the right child of Chapter 1.
- A similar structure applies to Chapter 2.

This hierarchical organization allows us to traverse each chapter and its sections in a defined order.

### In-Order Traversal
In **In-Order Traversal**, nodes are visited in this order:
1. Traverse the left subtree.
2. Visit the root node.
3. Traverse the right subtree.

In binary trees, this results in nodes being visited in ascending order if they are structured with increasing values.

### Post-Order Traversal
In **Post-Order Traversal**, nodes are visited in this order:
1. Traverse the left subtree.
2. Traverse the right subtree.
3. Visit the root node.

This method is often used for operations that require processing child nodes before their parent nodes.

## Complete Binary Tree
A **Complete Binary Tree** is a binary tree in which all levels, except possibly the last, are fully filled. Nodes in the last level are added from left to right but do not need to completely fill the level.

Complete binary trees are often used in heaps and priority queues where a balanced structure is desired for efficient operations.
