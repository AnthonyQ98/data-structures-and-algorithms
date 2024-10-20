from linked_list import LinkedList

def main():
    # create a new linked list
    ll = LinkedList()

    # add nodes to the linked list
    ll.insert_at_beginning('John')
    ll.insert_at_end('Kevin')
    ll.insert_at_beginning('Philip')
    ll.insert_at_beginning('Ryan')
    ll.insert_at_index('Anthony', 2)

    # print the linked list
    print("Node Data")
    print(ll)

    # remove nodes from the linked list
    print("\nRemove First Node")
    ll.remove_first_node()
    print("Remove Last Node")
    ll.remove_last_node()
    print("Remove Node at Index 1")
    ll.remove_node_at_index(1)

    # print the linked list again
    print("\nLinked list after removing a node:")
    print(ll)

    print("\nUpdate node Value")
    ll.update_at_index('Felicia', 0)
    print(ll)

    print("\nSize of linked list :", end=" ")
    print(ll.size())

if __name__ == "__main__":
    main()