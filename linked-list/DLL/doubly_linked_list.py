class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    
    def __repr__(self):
        return repr(self.data)
    

class DoublyLinkedList:
    def __init__(self):
        # HEAD node without data, prev, next.
        self.head = Node()
    
    def __repr__(self):
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next
        
        return ", ".join(nodes)

    def append(self, data):
        new_node = Node(data)

        if self.head.next is None:
            # If DLL is blank, we'll insert first node
            # at head's next. then we'll terminate from function.
            self.head.next = new_node
            return
        

        # DLL is not blank, find last node and make it current_node.
        current_node = self.head.next

        while current_node.next:
            current_node = current_node.next
        
        # current_node's next will be new_node, and new_node's 
        # prev will be current_node.
        current_node.next = new_node
        new_node.prev = current_node
    
    def prepend(self, data):
        # first_node is the first node of DLL.
        first_node = self.head.next

        # instantiate new_node with prev=None and next=first_node.
        new_node = Node(data, None, first_node)

        # HEAD should point new_node.
        self.head.next = new_node

        if first_node:
            # If first_node is not None, it's prev will be new_node.
            first_node.prev = new_node
    
    def search(self, item):
        current_node = self.head.next

        while current_node:
            if current_node.data == item:
                return current_node
            current_node = current_node.next
        return None
    
    def remove_node(self, node):
        if node.prev:
            # if node.prev is not none, node.next will be the next node.
            node.prev.next = node.next
        else:
            # First node of DLL, so node after head will node.next
            self.head.next = node.next
        
        if node.next:
            # If node is not last node, update node.next.prev to
            # make it skip the node and point as it's previous node.
            node.next.prev = node.prev
    
    def remove(self, item):
        # First we'll find which node the item belongs to.
        # If multiple node found, we'll take first one.
        node = self.search(item)

        if node is None:
            return
        
        self.remove_node(node)