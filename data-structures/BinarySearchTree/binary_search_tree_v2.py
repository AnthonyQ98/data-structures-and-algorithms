# another option for BST using a single class

class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

# insert into tree
    def insert(self, value):
        if value < self.value:
            if self.left_child is None:
                self.left_child = TreeNode(value)
            else:
                self.left_child.insert(value)
        else:
            if self.right_child is None:
                self.right_child = TreeNode(value)
            else:
                self.right_child.insert(value)


# search the tree
    def search(self, value):
        if value < self.value:
            if self.left_child is None:
                return None
            else:
                return self.left_child.search(value)

        elif value > self.value:
            if self.right_child is None:
                return None
            else:
                return self.right_child.search(value)
        else:
            return self

# delete from the tree
    def delete(self, value):
        if self.value is None:
            return self
        
        if value < self.value: # find the value
            self.left_child = self.left_child.delete(value)
        elif value > self.value:
            self.right_child = self.right_child.delete(value)
        else: # found the value, perform delete
            if self.left_child is None and self.right_child is None: # no children
                return None
            elif self.left_child is None: # right child only
                return self.right_child
            elif self.right_child is None: # left child only
                return self.left_child
            else: # has left and right child...
                successor = self.right_child.find_min() # find min node on right subtree
                self.value = successor.value # get the value of min node of right subtree
                self.right_child = self.right_child.delete(successor.value)
        
        return self

    def find_min(self):
        current = self
        while current.left_child is not None: # keep going left
            current = current.left_child
        return current # returns left most node


# traverse the tree
    def preorder_traversal(self): # root, left, right
        print(self.value)
        if self.left_child:
            self.left_child.preorder_traversal()
        if self.right_child:
            self.right_child.preorder_traversal()

    def inorder_traversal(self): # left, root, right
        if self.left_child:
            self.left_child.preorder_traversal()
        print(self.value)
        if self.right_child:
            self.right_child.preorder_traversal()

    def postorder_traversal(self): # left, right, root
        if self.left_child:
            self.left_child.preorder_traversal()
        if self.right_child:
            self.right_child.preorder_traversal()
        print(self.value)



def main():
    tree = TreeNode(20)

    tree.insert(2)

    tree.insert(9)

    tree.insert(30)

    tree.insert(10)

    tree.insert(19)

    tree.insert(14)

    tree.insert(32)

    tree.insert(31)

    tree.insert(1)

    tree.insert(5)

    print(tree.left_child.left_child.value) # should print back 1

    print(tree.left_child.right_child.right_child.right_child.left_child.value) # should print back 14

    print(tree.search(32).value) # is in the tree, print the value for this node.

    print(tree.search(7)) # not in the tree... should print None

    print(tree.delete(32))

    print(tree.search(32)) # no longer found in the tree

    print(tree.right_child.right_child.value) # was 32... but we deleted it, so should now be 31.

    tree.preorder_traversal()

    tree.inorder_traversal()

    tree.postorder_traversal()
 

if __name__ == "__main__":
    main()