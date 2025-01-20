class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = set()

    def add_neighbor(self, neighbor):
        self.adjacent.add(neighbor)

    def get_connections(self):
        return self.adjacent

    def get_id(self):
        return self.id

class Graph:
    def __init__(self):
        self.vert_dict = {}

    def add_vertex(self, node):
        vertex = Vertex(node)
        self.vert_dict[node] = vertex
        return vertex

    def add_edge(self, frm, to):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        self.vert_dict[frm].add_neighbor(self.vert_dict[to])
        self.vert_dict[to].add_neighbor(self.vert_dict[frm])

    def __iter__(self):
        return iter(self.vert_dict.values())
    
    def find_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.vert_dict:
            return []
        paths = []
        for neighbor in self.vert_dict[start].get_connections():
            if neighbor.get_id() not in path:  # Avoid cycles
                new_paths = self.find_paths(neighbor.get_id(), end, path)
                for p in new_paths:
                    paths.append(p)
        return paths