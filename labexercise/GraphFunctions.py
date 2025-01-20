import networkx as nx
import matplotlib.pyplot as plt

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
        """Returns all possible paths from start to end"""
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

g = Graph()

# #MRT 
g.add_edge("Taft Avenue", "Magallanes")
g.add_edge("Magallanes", "Ayala")
g.add_edge("Ayala", "Buendia")
g.add_edge("Buendia", "Guadalupe")
g.add_edge("Guadalupe", "Boni")
g.add_edge("Boni", "Shaw Boulevard")
g.add_edge("Shaw Boulevard", "Ortigas")
g.add_edge("Ortigas", "Santolan LRT")
g.add_edge("Santolan LRT","Araneta Center - Cubao")
g.add_edge("Araneta Center - Cubao", "Kamuning")
g.add_edge("Kamuning", "Quezon Avenue")
g.add_edge("Quezon Avenue", "North Avenue")

# LRT 2
g.add_edge("Recto", "Legarda")
g.add_edge("Legarda", "Pureza")
g.add_edge("Pureza", "V. Mapa")
g.add_edge("V. Mapa", "J. Ruiz")
g.add_edge("J. Ruiz", "Gilmore")
g.add_edge("Gilmore", "Betty Go Belmonte")
g.add_edge("Betty Go Belmonte", "Araneta Center - Cubao")
g.add_edge("Araneta Center - Cubao", "Anonas")
g.add_edge("Anonas", "Katipunan")
g.add_edge("Katipunan", "Santolan MRT")


# LRT 1
g.add_edge("Baclaran", "EDSA")
g.add_edge("EDSA", "Libertad")
g.add_edge("Libertad", "Gil Puyat")
g.add_edge("Gil Puyat", "Vito Cruz")
g.add_edge("Vito Cruz", "Quirino")
g.add_edge("Quirino", "Pedro Gil")
g.add_edge("Pedro Gil", "United Nations")
g.add_edge("United Nations", "Central Terminal")
g.add_edge("Central Terminal", "Carriedo")
g.add_edge("Carriedo", "Doroteo Jose")
g.add_edge("Doroteo Jose", "Bambang")
g.add_edge("Bambang", "Tayuman")
g.add_edge("Tayuman", "Blumentrit")
g.add_edge("Blumentrit", "Abad Santos")
g.add_edge("Abad Santos", "R. Papa")
g.add_edge("R. Papa", "5th Avenue")
g.add_edge("5th Avenue", "Monumento")
g.add_edge("Monumento", "Balintawak")
g.add_edge("Balintawak", "Roosevelt")

#Connecting Terminals
g.add_edge("Taft Avenue", "EDSA")
g.add_edge("Doroteo Jose", "Recto")

# Draw the graph
g.find_paths({},{})
