class TreeNode:
    def __init__(self, val: int, left: any = None, right: any = None):
        self.value = val
        self.leftChild = left
        self.rightChild = right


def search(search_value: int, node: TreeNode):
    if node is None or node.value == search_value:
        return node
    elif search_value < node.value:
        return search(search_value, node.leftChild)
    elif search_value > node.value:
        return search(search_value, node.rightChild)


def insert(value: int, node: TreeNode):
    if value < node.value:
        if node.leftChild is None:
            node.leftChild = TreeNode(value)
        else:
            insert(value, node.leftChild)
    elif value > node.value:
        if node.rightChild is None:
            node.rightChild = TreeNode(value)
        else:
            insert(value, node.rightChild)


def delete(value_to_delete: int, node: TreeNode):
    if node is None:
        return None
    elif value_to_delete < node.value:
        node.leftChild = delete(value_to_delete, node.leftChild)
        return node
    elif value_to_delete > node.value:
        node.rightChild = delete(value_to_delete, node.rightChild)
        return node
    elif value_to_delete == node.value:
        if node.leftChild is None:
            return node.rightChild
        elif node.rightChild is None:
            return node.leftChild
        else:
            node.rightChild = lift(node.rightChild, node)
            return node


def lift(node: TreeNode, node_to_delete: TreeNode):
    if node.leftChild:
        node.leftChild = lift(node.leftChild, node_to_delete)
        return node
    else:
        node_to_delete.value = node.value
        return node.rightChild

def traverse_and_print(node: TreeNode):
    if node is None:
        return
    traverse_and_print(node.leftChild)
    print(node.value)
    traverse_and_print(node.rightChild)


def find_highest(node: TreeNode) -> int:
    if node.rightChild:
        return find_highest(node.rightChild)
    else:
        return node.value





if __name__ == "__main__":
    node1 = TreeNode(25)
    node2 = TreeNode(75)
    root = TreeNode(50, node1, node2)
    print(search(30, root))
    insert(100, root)
    print(search(100, root))
    delete(100, root)
    print(search(100, root))
    for i in range(0, 100, 5):
        insert(i, root)
    #traverse_and_print(root)
    print(find_highest(root))
