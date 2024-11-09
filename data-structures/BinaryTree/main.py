class BinaryTree:
    def __init__(self, root_obj) -> None:
        self.root_obj = root_obj
        self.left_child = None
        self.right_child = None
    
    def get_root(self):
        return self.root_obj
    
    def set_root(self, obj):
        self.root_obj = obj

    def set_right_child(self, data):
        if self.right_child == None:
            new_obj = BinaryTree(data)
            self.right_child = new_obj
        else:
            new_right_child = BinaryTree(data)
            new_right_child.set_right_child(self.right_child)
            self.right_child = new_right_child

    def set_left_child(self, data):
        if self.left_child == None:
            new_obj = BinaryTree(data)
            self.left_child = new_obj
        else:
            new_left_child = BinaryTree(data)
            new_left_child.set_right_child(self.left_child)
            self.left_child = new_left_child

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child
    

# Main function to generate a random list, sort it, and print the result
def main():
    a_tree = BinaryTree("a")
    print(a_tree.get_root())
    print(a_tree.get_left_child())
    a_tree.set_left_child("b")
    print(a_tree.get_left_child())
    print(a_tree.get_left_child().get_root())
    a_tree.set_right_child("c")
    print(a_tree.get_right_child())
    print(a_tree.get_right_child().get_root())
    a_tree.get_right_child().set_root("hello")
    print(a_tree.get_right_child().get_root())

if __name__ == "__main__":
    main()
