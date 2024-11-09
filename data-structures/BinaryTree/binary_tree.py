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
    
    def preorder(self):
        print(self.root_obj)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def postorder(self):
        if self.root_obj:
            self.left_child.postorder()
            self.right_child.postorder()
            print(self.root_obj)

    def inorder(self):
        if self.root_obj:
            self.left_child.inorder()
            print(self.root_obj)
            self.right_child.inorder()
    
