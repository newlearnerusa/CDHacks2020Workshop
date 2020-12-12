from functools import reduce

__author__      = "Ruben Acuna"
__copyright__   = "Copyright 2020, Ruben Acuna"

# don't do this at home
_print = print
def mp(*args):
    if "Here" in globals():
        _print(*args)
print = mp

################################################################################
# BASIC PYTHON DATA STRUCTURES
################################################################################

Here = True

################################################################################
# lists
print("==LISTS==")
lst = list(["a", "b", "c"])

# TODO testing


################################################################################
# tuples
print("==TUPLES==")
tp = ("a", "b", "c")

# TODO testing


################################################################################
# dictionary
print("==DICTIONARY==")
test = dict()

# TODO testing


################################################################################
# sets
print("==SETS==")
s = set(["a", "b"])

# TODO testing


################################################################################
# HIGHER ORDER PROGRAMMING
################################################################################

################################################################################
# generic sorting
scratch = [("Java", 0), ("LISP", 10), ("Python", 4), ("C", 3), ("JavaScript", 2)]


def first(x):
    return x[0]


def second(x):
    return x[1]

# TODO testing


################################################################################
# function builder

def inc_maker(inc):
    def tmp(x):
        return x + inc
    return tmp

# TODO testing


################################################################################
# map/filter/reduce

def sq(x):
    return x * x


def odd(x):
    return x % 2


def bigger(a, b):
    if b > a:
        return b
    else:
        return a


samples = [3, 4, 1, 2, 6]

# TODO: map/filter


# TODO: reduce


################################################################################
# DATA STRUCTURE ABSTRACTION
################################################################################


def hacky_create_graph1(G):
    G.add_edge(0, 1)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(3, 4)

    G.add_edge(2, 5)
    G.add_edge(5, 6)
    G.add_edge(6, 7)
    G.add_edge(4, 7)


def hacky_create_graph2(G):
    G.add_edge("口", "中")
    G.add_edge("口", "只")
    G.add_edge("口", "吾")
    G.add_edge("吾", "語")


class UndirectedGraph:
    def __init__(self):
        self.vertices = set()
        self.edges = dict()

    def add_vertex(self, v):
        if v not in self.vertices:
            self.vertices.add(v)
            self.edges[v] = []

    def add_edge(self, v, w):
        self.add_vertex(v)
        self.add_vertex(w)

        if w not in self.edges[v]:
            self.edges[v] += [w]
            self.edges[v].sort()

        if v not in self.edges[w]:
            self.edges[w] += [v]
            self.edges[w].sort()

    def adj(self, v):
        return self.edges[v]


class DirectedGraph:
    def __init__(self):
        self.vertices = set()
        self.edges = dict()

    def add_vertex(self, v):
        if v not in self.vertices:
            self.vertices.add(v)
            self.edges[v] = []

    def add_edge(self, v, w):
        self.add_vertex(v)
        self.add_vertex(w)

        if w not in self.edges[v]:
            self.edges[v] += [w]
            self.edges[v].sort()

    def adj(self, v):
        return self.edges[v]


class SearchQueue:
    def __init__(self):
        self.queue = []
    def add(self, i):
        self.queue.append(i)
    def remove(self):
        return self.queue.pop(0)
    def __len__(self):
        return len(self.queue)


class SearchStack:
    def __init__(self):
        self.stack = []
    def add(self, i):
        self.stack.append(i)
    def remove(self):
        return self.stack.pop()
    def __len__(self):
        return len(self.stack)


def graph_search(G, start_node, searchDS):

    container = searchDS()  # contains dictionaries with "state" and "path" keys.
    visited = set()
    paths = dict()

    container.add({"node": start_node, "path": [start_node]})
    visited.add(start_node)

    while len(container):
        packet = container.remove()
        cur_node = packet["node"]
        cur_path = packet["path"]

        paths[cur_node] = cur_path

        for neighbor in G.adj(cur_node):
            if neighbor not in visited:
                visited.add(neighbor)
                new_node = {"node": neighbor, "path": cur_path + [neighbor]}
                container.add(new_node)

    print("Paths (%s, %s):" % (G.__class__.__name__, searchDS.__name__))
    for v in sorted(paths.keys()):
        print(v, ":", paths[v])


BFS = lambda G, start: graph_search(G, start, SearchQueue)
DFS = lambda G, start: graph_search(G, start, SearchStack)


UG1 = UndirectedGraph()
hacky_create_graph1(UG1)
UG2 = UndirectedGraph()
hacky_create_graph2(UG2)

# BFS(UG1, 0)
# BFS(UG2, "口")
# DFS(UG1, 0)


DG1 = DirectedGraph()
hacky_create_graph1(DG1)

# BFS(DG1, 1)

################################################################################
# DECORATORS
################################################################################


################################################################################
# DECORATORS #1: Doing nothing.

# TODO decorator_thing()


def dec_plain_func1():
    print("inside the function")


# TODO testing as wrapper


# TODO as decorator


# TODO testing as decorator


################################################################################
# DECORATORS #2: Warning on usage.

# TODO deprecated()


# @deprecated
def dec_plain_func3():
    print("this is pretty much redundant with the other functions")


# @deprecated
def dec_plain_func4(a, b):
    print("this is pretty much redundant with +:", str(a + b))

# TODO testing


################################################################################
# DECORATORS #3: memoization

# TODO memo()


# @memo
def fib1(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib1(n-1)+fib1(n-2)


def fib2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib2(n-1)+fib2(n-2)

# TODO testing
