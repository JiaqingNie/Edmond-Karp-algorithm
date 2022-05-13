from copy import deepcopy
from Path import Path
from Flow import Flow
from utils import read_graph
from utils import show_flow


def get_residual_network(G, f):
    """
    get the residual network given the graph and flow network.
    :param G: the input graph
    :param f: the current flow network
    :return: the residual graph
    """
    Gf = deepcopy(G)
    flow = f.get_flow()
    for (u, v, value) in flow:
        old_capacity = Gf.get_capacity(u, v)
        new_capacity = old_capacity - value
        if new_capacity == 0:
            Gf.remove_edge(u, v)
        else:
            Gf.set_capacity(u, v, new_capacity)
        if not Gf.has_edge(v, u):
            Gf.add_edge(v, u)
        Gf.set_capacity(v, u, value)

    return Gf


def find_augmenting_path_by_bfs(Gf):
    """
    find the augmenting path from s to s using the BFS algorithm.
    :param Gf: the residual graph
    :return: the path object from s to t if found
    """
    root = Path(Gf, Gf.s)
    visited = set()
    l = [root]
    while l:
        path = l.pop(0)
        tail = path.tail()
        outgoing_list = Gf.get_vertices_outgoing_from(tail)
        for v in outgoing_list:
            if (tail, v) in visited:
                continue
            visited.add((tail, v))
            p = path.copy()
            p.append(v)
            if v == Gf.t:
                return p
            l.append(p)


def Edmond_Karp(G):
    """
    the Edmond Karp algorithm to solve the max flow problem.
    :param G: the input graph G = (V, E, c, s, t)
    :return: the max flow object
    """
    it = 0
    f = Flow(G)
    while True:
        it += 1
        print("Iteration {}:".format(it))
        Gf = get_residual_network(G, f)
        print(Gf)
        path = find_augmenting_path_by_bfs(Gf)
        if path:
            print(path)
        else:
            print("Path not found, Done!")
            break
        fp = path.get_path_flow()
        f.augment(fp)
    print("Max Flow: {}\n".format(f.value()))
    return f