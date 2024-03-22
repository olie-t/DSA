import queue


class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_verticies(self, vertex):
        if vertex in self.adjacent_vertices:
            return True
        else:
            self.adjacent_vertices.append(vertex)
            vertex.add_adjacent_verticies(self)


def dfs_traverse(start: Vertex, visited_vertex: dict = {}):
    visited_vertex[start.value] = True
    print(start.value)
    for adjacent_vertex in start.adjacent_vertices:
        if adjacent_vertex.value in visited_vertex:
            continue
        dfs_traverse(adjacent_vertex, visited_vertex)
    return


def dfs(vertex: Vertex, search_value: str, visited_vertices: dict = {}) -> Vertex:
    if vertex.value == search_value:
        return vertex
    visited_vertices[vertex.value] = True
    for adjacent_vertex in vertex.adjacent_vertices:
        if adjacent_vertex.value in visited_vertices:
            continue
        if adjacent_vertex.value == search_value:
            return adjacent_vertex
        vertex_were_searching_for = dfs(adjacent_vertex, search_value, visited_vertices)
        if vertex_were_searching_for:
            return vertex_were_searching_for
    return


def bfs_traverse(start: Vertex):
    que = queue.Queue()

    visited_vertices = {start.value: True}
    que.put(start)

    while not que.empty():
        current_vertex = que.get()
        print(current_vertex.value)
        for adjacent_vertex in current_vertex.adjacent_vertices:
            if adjacent_vertex.value in visited_vertices:
                continue
            visited_vertices[adjacent_vertex.value] = True
            que.put(adjacent_vertex)


if __name__ == "__main__":
    alice = Vertex("Alice")
    bob = Vertex("Bob")
    steve = Vertex("Steve")
    dave = Vertex("Dave")
    ben = Vertex("Ben")
    syd = Vertex("Syd")
    olie = Vertex("Olie")
    marg = Vertex("Marge")
    dyl = Vertex("Dyl")

    alice.add_adjacent_verticies(bob)
    alice.add_adjacent_verticies(steve)
    bob.add_adjacent_verticies(steve)
    alice.add_adjacent_verticies(dave)
    dave.add_adjacent_verticies(syd)
    syd.add_adjacent_verticies(olie)
    olie.add_adjacent_verticies(ben)
    ben.add_adjacent_verticies(syd)
    steve.add_adjacent_verticies(marg)
    marg.add_adjacent_verticies(dyl)

    dfs_traverse(bob)
    print(dfs(bob, "Steve"))
    bfs_traverse(bob)
