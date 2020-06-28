from .doubly_linked_list import Node, DoublyLinkedList


def test_append():
    dll = DoublyLinkedList()

    assert dll.head.next == None, "DDL should be empty at first instantiation."

    item = 30
    dll.append(item)
    assert dll.head.next.data == item, "Head should point to first node."

    item2 = 32
    dll.append(item2)
    assert dll.head.next.data == item, "Head should point to first node."

    frist_node = dll.head.next
    second_node = frist_node.next

    assert frist_node.next.data == item2, "First node should point to second node"
    assert second_node.prev.data == item, "Second node should trach first node as prev referrence."
    assert str(dll) == "30, 32", "Comma separated str representation should be 30, 32"


def test_prepend():
    dll = DoublyLinkedList()

    assert dll.head.next == None, "DDL should be empty at first instantiation."

    item = 28
    dll.prepend(item)

    assert dll.head.next.data == 28, "Head has to keep track first node after prepend."

    item2 = 30
    dll.prepend(item2)
    assert dll.head.next.data == item2, "Head should point to new node."

    new_node = dll.head.next
    old_node = new_node.next

    assert new_node.prev == None, "New prepended node should be None."
    assert old_node.prev == new_node, "prev of new node should point to new_node."
    assert old_node.data == item, "old_node should contain 28"
    assert new_node.data == item2, "new_node should contain 30"
    assert str(dll) == "30, 28", "DLL should represent 30, 28 in string."


def test_search():
    dll = DoublyLinkedList()

    item = 28
    assert dll.search(item) == None, "item shouldn't be found in an empty list."
    dll.append(item)
    node = dll.search(item)
    assert node.data == item, "Item should be found in the DLL."
    dll.append(30)
    node = dll.search(30)
    assert node.data == 30, "Node data should be 30"
    node = dll.search(50)
    assert node == None, "50 shouldn't be found on DLL."


def test_remove():
    dll = DoublyLinkedList()
    [dll.append(i) for i in range(10, 14)]

    node_10 = dll.search(10)
    node_11 = dll.search(11)
    node_12 = dll.search(12)
    node_13 = dll.search(13)

    assert node_10.next == node_11
    assert node_11.prev == node_10

    # Remove from middle
    dll.remove_node(node_12)
    assert node_11.next == node_13, "node_11.next should point to node_13"
    assert node_13.prev == node_11, "node_13 should be pointed from node_11.prev"
    assert str(dll) == "10, 11, 13", "dll should not contain 12 in string representation."

    # Remove from end
    dll.remove(13)
    assert node_11.next == None, "node_11.next should be none as its last node now."
    assert str(dll) == "10, 11", "13 should not be in the representation of DLL."

    # Remove from start.
    dll.remove(10)
    assert node_11.next == None, "node_11.next should be None."
    assert node_11.prev == None, "node_11.prev should be None."
    assert dll.head.next == node_11, "head.next should point node_11."
    assert str(dll) == "11", "dll should only contain 11"
    

    