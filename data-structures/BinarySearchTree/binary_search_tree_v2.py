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

# traverse the tree



# delete from the tree



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
 

if __name__ == "__main__":
    main()