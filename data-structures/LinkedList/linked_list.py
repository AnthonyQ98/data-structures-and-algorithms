from node import Node

class LinkedList():
    def __init__(self):
        self.head = None

    # insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # insert at index
    def insert_at_index(self, data, index):
        if index == 0:
            self.insert_at_beginning(data)

        position = 1
        current_node = self.head
        while current_node != None and position != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)    
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("index not present in linked list")

    # insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while (current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    # update node at index
    def update_at_index(self, data, index):
        if index == 0:
            self.head.data = data
            return

        current_node = self.head

        position = 1
        while (current_node.next != None and position != index):
            current_node = current_node.next
            position += 1

        if current_node is not None:
            current_node.data = data 
        else:
            print("node not present in linked list")  

    # remove first node
    def remove_first_node(self):
        if self.head is None:
            return
        
        self.head = self.head.next

    # remove last node
    def remove_last_node(self):
        if self.head is None:
            return

        current_node = self.head

        # loop until the node after next node is None.
        # ie: mynode.next => foobar. foobar.next => None.
        # break out when currrent_node = mynode in this case.
        # set mynode.next = None (removing any pointer to foobar, which is the last node)
        while current_node and current_node.next.next is not None:
            current_node = current_node.next

        current_node.next = None

    # remove at index
    def remove_node_at_index(self, index):
        if self.head == None:
            return
        
        position = 0
        current_node = self.head

        if position == index:
            self.remove_first_node()
        else:
            # stop before the node want to remove (position+1 != index)
            # or stop if we exceeded the nodes in the linked list
            while current_node and position + 1 != index:
                position = position + 1
                current_node = current_node.next
            if current_node: # if we still have nodes, and we know the next node is the index we want to remove.
                current_node.next = current_node.next.next # replace the pointer to next (what we want to remove) to point to next.next (next node of the node we want to remove)
            else:
                print("index not present")

    # remove node (by data/value)
    def remove_node(self, data):
        current_node = self.head

        if current_node.data == data:
            self.remove_first_node()
            return
        
        while current_node and current_node.next.data != data:
            current_node = current_node.next

        if not current_node:
            return
        else:
            current_node.next = current_node.next.next

    # return the size of the linked list    
    def size(self):
        size = 0
        if (self.head):
            current_node = self.head
            while(current_node):
                size += 1
                current_node = current_node.next
            return size
        else:
            return 0

    # print the linked list
    def __repr__(self) -> str:
        if self.head is None:
            return "empty linked list"
        else:
            current_node = self.head
            nodes = []
            while current_node is not None:
                nodes.append(current_node.data)
                current_node = current_node.next

        return "->".join(nodes)

        