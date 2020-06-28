""" 
Learning bit by bit. Practice each method over and over.
"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def __repr__(self):
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next
        
        return ", ".join(nodes)
    
    def append(self, data):
        node = Node(data=data)

        # If head is last node (Empty LL).
        if self.head.next is None:
            self.head.next = node
            return

        # Handling append if head is not the last node.
        current_node = self.head.next

        while current_node.next:
            current_node = current_node.next
        
        # We reached last node through loop. Now we change the
        # last node's next to the node we created.
        current_node.next = node
    
    def prepend(self, data):
        node = Node(data, self.head.next)
        self.head.next = node
    
    def insert(self, data, new_data):
        current_node = self.head.next

        while current_node:
            if current_node.data == data:
                new_node = Node(new_data, current_node.next)
                current_node.next = new_node
                break
            current_node = current_node.next
    
    def search(self, item):
        current_node = self.head.next

        while current_node.next:
            if current_node.data == item:
                return item
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
            # Item not found until last iteration of loop.
            return None

        if self.head == prev_node:
            # 1st node is to be deleted.
            self.head.next = current_node.next
        else:
            # Other than 1st node is to be deleted.
            prev_node.next = current_node.next
        
