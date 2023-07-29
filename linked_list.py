class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
