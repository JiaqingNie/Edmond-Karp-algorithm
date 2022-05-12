from pyvis.network import Network
from IPython.display import display
from Graph import Graph


def read_graph():
    """
    read the graph text file and convert it into the graph object.
    format of "graph.txt" file:
      first line: 2 vertices, source and target node, seperated by a whitespace;
      from second line: "fromVertex toVertex capacity", such as: s t 2.
    :return: a directed graph
    """
    res = Graph()
    with open('graph.txt', 'r') as f:
        s_t = f.readline().strip('\n').split()
        s = s_t[0]
        t = s_t[1]
        res.add_vertex(s)
        res.add_vertex(t)
        res.set_source(s)
        res.set_target(t)

        lines = f.readlines()
        for line in lines:
            l = line.strip("\n").split()
            if not res.has_vertex(l[0]):
                res.add_vertex(l[0])
            if not res.has_vertex(l[1]):
                res.add_vertex(l[1])
            if not res.has_edge(l[0], l[1]):
                res.add_edge(l[0], l[1])

            res.set_capacity(l[0], l[1], int(l[2]))
    show_graph(res)
    return res


def show_flow(flow, name="flow"):
    """
    save the flow network on disk. If invoked from notebook, it will display an interactive graph.
    :param flow: the flow network
    :param name: the file name to be saved
    """
    net = Network(directed=True, notebook=True)
    for (u, v, c) in flow:
        if u not in net.nodes:
            net.add_node(u, label=u)
        if v not in net.nodes:
            net.add_node(v, label=v)
        net.add_edge(u, v, weight=c, label=str(c))

    display(net.show('{}.html'.format(name)))


def show_graph(G, name="graph"):
    """
    save the graph on disk. If invoked from notebook, it will display an interactive graph.
    :param G: the graph
    :param name: the file name to be saved
    """
    net = Network(directed=True, notebook=True)
    colors = dict([(u, 'blue') for u in G.V if u != G.s and u != G.t])
    colors[G.s] = 'black'
    colors[G.t] = 'green'
    for (u, v) in G.c:
        c = G.get_capacity(u, v)
        if u not in net.nodes:
            net.add_node(u, label=u, color=colors[u])
        if v not in net.nodes:
            net.add_node(v, label=v, color=colors[v])
        net.add_edge(u, v, weight=c, label=str(c), color="black")
    display(net.show('{}.html'.format(name)))
