# Linked List Overview

A **Linked List** is an Abstract Data Type (ADT) that consists of nodes where each node contains data and a pointer to the next node in the sequence. Unlike arrays, nodes in a linked list are not required to be stored sequentially in memory.

## Key Characteristics of Linked Lists

- **Traversal**: Must traverse the entire linked list to find a specific node.
- **Non-Sequential Storage**: Nodes are not stored in contiguous memory, unlike arrays.
- **Node Structure**:
  - **Singly Linked List**: Each node holds data and a pointer to the next node.
  - **Doubly Linked List**: In addition to data and a pointer to the next node, each node also has a pointer to the previous node.

## Basic Structure

A Linked List typically contains:
- A **head** pointer, which points to the first node in the list.
- Nodes that each contain:
  - Data
  - Pointer to the next node

## Operations on a Linked List

### Insertion
- **Insert a node at a specific index**: Traverse the list to the index and insert the node.
- **Insert a node at the end**: Traverse the entire list to find the last node and insert the new node.
- **Insert a node at the beginning**: Create a new node and point it to the current head.

### Removal
- **Remove a node by its index**: Traverse the list to the index and remove the node.
- **Remove a node at the end**: Traverse the list to the last node and remove it.
- **Remove a node at the beginning**: Point the head to the next node, effectively removing the first node.
- **Remove a node by its value (data)**: Traverse the list to find the node with the specific value and remove it.

### Other Operations
- **Formatted output**: Display the elements of the linked list in a readable format.
- **Size of the linked list**: Calculate the total number of nodes in the list.

## Time and Space Complexity

| Operation                   | Time Complexity | Space Complexity |
|------------------------------|-----------------|------------------|
| **Insert/remove at the end**  | O(n)            | O(1)             |
| **Insert/remove at the beginning** | O(1)        | O(1)             |
| **Insert/remove in the middle**   | O(n)        | O(1)             |
| **Search for a node**             | O(n)        | O(1)             |

### Notes on Complexity:
- **O(n)**: Insertion or removal at the end or in the middle requires traversing the list, resulting in a time complexity of O(n).
- **O(1)**: Insertion or removal at the beginning only requires updating the head, making it constant time.
- **Space Complexity**: Space is constant (O(1)) for all operations as no additional space is required beyond storing the node itself and its pointers.
