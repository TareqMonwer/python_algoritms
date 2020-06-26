class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self):
        # Initially head node will be blank of which data and next
        # value will be None.
        self.head = Node()
    
    def __repr__(self):
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node))

            current_node = current_node.next
        
        # Each node will be represented as comma separated string.
        return ", ".join(nodes)
    
    def append(self, data):
        # creating a node.
        node = Node(data)
        if self.head.next is None:
            # When no node is available, we take node at
            # head.next
            self.head.next = node
            return
        
        # We'll get last node by looping through all nodes,
        # current_node will be the last node.
        current_node = self.head.next

        while current_node.next:
            current_node = current_node.next
        
        # Last node's next will be the node we created,
        # and that's our last node.
        current_node.next = node

    def prepend(self, data):
        # As bcz this will be first node, we create a node
        # and copy head.next to it.
        node = Node(data, self.head.next)

        # head.next will store node as it's first node of LL.
        self.head.next = node

    def insert(self, data, new_data):
        current_node = self.head.next

        while current_node:
            if current_node.data == data:
                # We'll create node with new_data.
                # and new node's next will be current_node.next's next.
                new_node = Node(new_data, current_node.next)

                # new node will go into current_node.next.
                current_node.next = new_node

                # We setup new node in middle of LL. so we break the loop.
                break
            current_node = current_node.next

    def search(self, item):
        current_node = self.head.next

        # If current_node is None, that means it's a blank LL.
        # Loop runs if current_node is other than None.
        while current_node:
            if current_node.data == item:
                return current_node
            current_node = current_node.next
        return None

    def remove(self, item):
        prev_node = self.head
        current_node = prev_node.next

        while current_node:
            if current_node.data == item:
                break

            prev_node = current_node
            current_node = current_node.next
        
        if current_node is None:
            # It means we reach the last node and item was not found.
            return None
        
        if self.head == prev_node:
            # First node is current_node whose data is equal to item, so
            # head will point to node after current_node.
            self.head.next = current_node.next
        else:
            # Other nodes than the first one. so previous node's next will
            # be current_node's next.
            prev_node.next = current_node.next

