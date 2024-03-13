class DNode:
    def __init__(self, data: any, next_node: any = None, previous_node: any = None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node


class DoubleLinkedList:
    def __init__(self, first_node: DNode = None, last_node: DNode = None):
        self.first_node = first_node
        self.last_node = last_node

    def insert_at_end(self, data: any):
        new_node = DNode(data)
        if not self.first_node:
            self.first_node = new_node
        else:
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node

    def remove_from_front(self):
        removed_node = self.first_node
        self.first_node = self.first_node.next_node
        return removed_node

    def insert_at_index(self, data: any, index: int):
        new_node = DNode(data=data)
        if index == 0:
            new_node.next_node = self.first_node
            self.first_node = new_node
            return
        current_index = 0
        current_node = self.first_node
        while current_index < (index - 1):
            current_node = current_node.next_node
            current_index += 1
        new_node.next_node = current_node.next_node
        new_node.previous_node = current_node
        current_node.next_node = new_node

    def delete_at_index(self, index: int):
        if index == 0:
            self.first_node = self.first_node.next_node
            return
        current_node = self.first_node
        current_index = 0
        while current_index < (index - 1):
            current_node = current_node.next_node
            current_index += 1
        node_after_deletion = current_node.next_node.next_node
        node_after_deletion.previous_node = current_node
        current_node.next_node = node_after_deletion

    def print_all_backwards(self):
        current_node = self.last_node
        while current_node.previous_node:
            print(current_node.data)
            current_node = current_node.previous_node


if __name__ == "__main__":
    dnode1 = DNode("A")
    dnode2 = DNode("B")
    dnode3 = DNode("C")
    dnode4 = DNode("D")
    dnode1.next_node = dnode2
    dnode2.next_node = dnode3
    dnode3.next_node = dnode4
    dnode4.previous_node = dnode3
    dnode3.previous_node = dnode2
    dnode2.previous_node = dnode1
    d_link_list = DoubleLinkedList(dnode1, dnode4)
    d_link_list.print_all_backwards()
