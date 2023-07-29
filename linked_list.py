class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def insert_at_start(self, data):
        new_node: Node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_at_rear(self, data):
        current_node: Node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        new_node: Node = Node(data)
        current_node.next_node = new_node

    def print(self):
        current_node: Node = self.head
        while current_node.next_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print(current_node.data)
