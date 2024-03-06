class Node:
    def __init__(self, data: any, next_node: any = None, previous_node: any = None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node


class LinkedList:
    def __init__(self, head: Node):
        self.head = head

    def read(self, index: int) -> Node:
        if index == 0:
            return self.head.data
        current_index = 0
        current_node = self.head
        while current_index < index:
            current_node = current_node.next_node
            current_index += 1
            if current_index == index:
                return current_node.data
            elif current_node.next_node is None:
                return None
    def index_of(self, value: any):
        current_index = 0
        current_node = self.head
        while True:
            if current_node.data == value:
                return current_index
            elif current_node.next_node is None:
                return None
            current_node = current_node.next_node
            current_index += 1

    def insert_at_index(self, data: any, index: int):
        new_node = Node(data=data)
        if index == 0:
            new_node.next_node = self.head
            self.head = new_node
            return
        current_index = 0
        current_node = self.head
        while current_index < (index - 1):
            current_node = current_node.next_node
            current_index += 1
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def delete_at_index(self, index: int):
        if index == 0:
            self.head = self.head.next_node
            return
        current_node = self.head
        current_index = 0
        while current_index < (index - 1):
            current_node = current_node.next_node
            current_index += 1
        node_after_deletion = current_node.next_node.next_node
        current_node.next_node = node_after_deletion


if __name__ == "__main__":
    node1 = Node(data="Once")
    node2 = Node(data="Upon")
    node3 = Node(data="A")
    node4 = Node(data="Time")

    node1.next_node = node2
    node2.next_node = node3
    node3.next_node = node4

    linked_list = LinkedList(node1)
    print(linked_list.read(2))
    print(linked_list.read(6))
    print(linked_list.index_of("A"))
    linked_list.insert_at_index("Test", 2)
    print(linked_list.read(2), linked_list.read(3))
    linked_list.delete_at_index(2)
    print(linked_list.read(0), linked_list.read(1), linked_list.read(2), linked_list.read(3), linked_list.read(5))
