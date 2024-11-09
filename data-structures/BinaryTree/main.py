import BinaryTree

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