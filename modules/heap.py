


class Heap:

    def __init__(self, data=None):
        if data is None:
            data = []
        self.data = data

    def left_child_index(self, index: int) -> int:
        return (index * 2) + 1

    def right_child_index(self, index: int) -> int:
        return (index * 2) + 2

    def parent_index(self, index: int) -> int:
        return (index - 1) // 2
    def root_node(self):
        return self.data[0]

    def last_node(self):
        return self.data[-1]

    def insert(self, value: int):
        self.data += value
        new_node_index = len(self.data) - 1

        while new_node_index > 0 and self.data[new_node_index] > self.data[self.parent_index(new_node_index)]:
            (self.data[self.parent_index(new_node_index)],
             self.data[new_node_index]) = self.data[new_node_index], self.data[self.parent_index(new_node_index)]
            new_node_index = self.parent_index(new_node_index)

    def has_greater_child(self, index:int) -> bool:
        left_index = self.left_child_index(index)
        right_index = self.right_child_index(index)
        has_left = left_index < len(self.data)
        has_right = right_index < len(self.data)

        left_greater = has_left and self.data[left_index] > self.data[index]
        right_greater = has_right and self.data[right_index] > self.data[index]

        return left_greater or right_greater

    def calculate_larger_child_index(self, index: int) -> int:
        if self.right_child_index(index) > len(self.data) - 1:
            return self.left_child_index(index)
        if self.data[self.right_child_index(index)] > self.data[self.left_child_index(index)]:
            return self.right_child_index(index)
        else:
            return self.left_child_index(index)

    def delete(self) -> int:
        value_to_delete = self.root_node()

        self.data[0] = self.data.pop()
        trickle_node_index = 0

        while self.has_greater_child(trickle_node_index):
            larger_child_index = self.calculate_larger_child_index(trickle_node_index)
            self.data[trickle_node_index], self.data[larger_child_index] = (
                self.data[larger_child_index], self.data[trickle_node_index])
            trickle_node_index = larger_child_index

        return value_to_delete





