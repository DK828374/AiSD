from enum import Enum
from typing import Any
from typing import Dict, List
from typing import Optional
import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx


class Vertex:
    data: Any
    index: int

    def __init__(self, data, ind):
        self.data = data
        self.index = ind

    def __repr__(self):
        return f'{self.data}:v{self.index}'


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, s, d, w):
        self.source = s
        self.destination = d
        self.weight = w

    def __repr__(self):
        return f'{self.destination}'


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]
    list_from = []
    list_to = []

    def __init__(self):
        self.adjacencies = dict()
        self.list_from = []
        self.list_to = []

    def __str__(self):
        result = ""
        lis = self.adjacencies.items()
        for key, value in lis:
            result += f'- {key.data}: {key.data} ----> [] \n'
        return result

    def create_vertex(self, value):
        vertex = Vertex(value, len(self.adjacencies))
        self.adjacencies[vertex] = []

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float]):
        edge = Edge(source, destination, weight)
        self.adjacencies[source].append(edge)
        self.list_from.append(source.data)
        self.list_to.append(destination.data)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float]):
        edge = Edge(source, destination, weight)
        edge2 = Edge(destination, source, weight)
        self.adjacencies[source].append(edge)
        self.adjacencies[destination].append(edge2)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        if edge.name == "directed":
            self.add_directed_edge(source, destination, weight)
        else:
            self.add_undirected_edge(source, destination, weight)

    def traverse_breadth_first(self, visit) -> None:
        list_keys = [x for x in self.adjacencies.keys()]
        list_visited = []
        queue = ()
        queue.enqueue(list_keys[0])
        while len(queue) != 0:
            new = queue.dequeue()
            list_visited.append(new)
            visit(new)
            for new_neighbour in self.adjacencies[new]:
                if new_neighbour.destination in list_visited:
                    return None
                else:
                    queue.enqueue(new_neighbour.destination)

    def traverse_depth_first(self, visit) -> None:
        list_keys = [x for x in self.adjacencies.keys()]
        list_visited = []
        self.dfs(list_keys[0], list_visited, visit)

    def dfs(self, v: Vertex, visited: List[Vertex], visit):
        visit(v)
        visited.append(v)
        for new_neighbour in self.adjacencies[v]:
            if new_neighbour.destination in visited:
                return True
            else:
                self.dfs(new_neighbour.destination, visited, visit)

    def show(self):
        relationships = pd.DataFrame({'od': [x for x in self.list_from], 'do': [y for y in self.list_to]})
        g = nx.from_pandas_edgelist(relationships, 'od', 'do', create_using=nx.DiGraph())
        nx.draw(g, with_labels=True, arrows=True)
        plt.show()


def path_testing(g: Graph, cross_id: Any, h: Any, path=None):
    if path is None:
        path = []
    path = path + [cross_id]
    if cross_id == h:
        return path
    for data in g.adjacencies[cross_id]:
        if data != path:
            result = path_testing(g, data.destination, h, path)
            if result:
                return result
    return []


def dead_path(g: Graph, cross_id: Any) -> Optional[List[Vertex]]:
    b = cross_id
    lista = []
    for data in g.adjacencies[cross_id]:
        if data not in lista:
            lista = lista + [cross_id]
            result = path_testing(g, data.destination, b, lista)
            if result:
                return result
    if lista == [cross_id]:
        return None
    else:
        return lista


# Graf 1
graph1 = Graph()
graph1.create_vertex(0)
graph1.create_vertex(1)
graph1.create_vertex(2)
graph1.create_vertex(3)
graph1.create_vertex(4)
graph1.create_vertex(5)
list1 = graph1.adjacencies.keys()
list1_keys = [x for x in list1]
graph1.add(EdgeType(1), list1_keys[1], list1_keys[5])
graph1.add(EdgeType(1), list1_keys[5], list1_keys[2])
graph1.add(EdgeType(1), list1_keys[2], list1_keys[0])
graph1.add(EdgeType(1), list1_keys[0], list1_keys[1])
graph1.add(EdgeType(1), list1_keys[0], list1_keys[3])
graph1.add(EdgeType(1), list1_keys[1], list1_keys[3])
graph1.add(EdgeType(1), list1_keys[5], list1_keys[3])
# Graf 2
graph2 = Graph()
graph2.create_vertex(0)
graph2.create_vertex(1)
graph2.create_vertex(2)
graph2.create_vertex(3)
graph2.create_vertex(4)
graph2.create_vertex(5)
list2 = graph2.adjacencies.keys()
list2_keys = [x for x in list2]
graph2.add(EdgeType(1), list2_keys[0], list2_keys[1])
graph2.add(EdgeType(1), list2_keys[1], list2_keys[2])
graph2.add(EdgeType(1), list2_keys[2], list2_keys[3])
graph2.add(EdgeType(1), list2_keys[3], list2_keys[4])
graph2.add(EdgeType(1), list2_keys[4], list2_keys[5])
graph2.add(EdgeType(1), list2_keys[5], list2_keys[0])
graph2.add(EdgeType(1), list2_keys[0], list2_keys[4])
# Graf 3
graph3 = Graph()
graph3.create_vertex("0")
graph3.create_vertex("1")
graph3.create_vertex("2")
graph3.create_vertex("3")
graph3.create_vertex("4")
graph3.create_vertex("5")
list3 = graph3.adjacencies.keys()
list3_keys = [x for x in list3]
graph3.add(EdgeType(1), list3_keys[1], list3_keys[2])
graph3.add(EdgeType(1), list3_keys[2], list3_keys[3])
graph3.add(EdgeType(1), list3_keys[3], list3_keys[4])
graph3.add(EdgeType(1), list3_keys[4], list3_keys[5])
graph3.add(EdgeType(1), list3_keys[0], list3_keys[1])
# Test
print("Test 1  Wierzchołek = 1")
print(dead_path(graph1, list1_keys[1]))
print("Test 2  Wierzchołek = 0")
print(dead_path(graph2, list2_keys[0]))
print("Test 3  Wierzchołek = 2")
print(dead_path(graph3, list3_keys[2]))

graph1.show()
graph2.show()
graph3.show()
