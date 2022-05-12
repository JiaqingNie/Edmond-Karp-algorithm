class Graph:
    """
    Data structure to solve the max flow problem by
    using the Edmonds-Karp algorithm.
    """

    def __init__(self):
        self.V = set()
        self.E = set()
        self.c = {}
        self.s = None
        self.t = None

    def add_vertex(self, v):
        """
        add a new vertex to the graph,
        raise an Exception if it has existed!
        :param v: the new vertex
        """
        if v not in self.V:
            self.V.add(v)
        else:
            raise Exception("Vertex '{}' has already existed!!!".format(v))

    def add_edge(self, u, v):
        """
        add a new directed edge between two vertices,
        raise Exceptions if it has existed or any vertex does not exist!
        :param u: the "from" vertex
        :param v: the "to" vertex
        """
        if u not in self.V:
            raise Exception("Vertex '{}' does not exist!!!".format(u))
        elif v not in self.V:
            raise Exception("Vertex '{}' does not exist!!!".format(v))
        else:
            edge = (u, v)
            if edge not in self.E:
                self.E.add(edge)
                self.c[edge] = 0
            else:
                raise Exception("Edge from '{}' to '{}' has already existed!!!".format(u, v))

    def remove_edge(self, u, v):
        """
        remove an edge in the graph and its corresponding capacity.
        :param u: the "from" vertex
        :param v: the "to" vertex
        """
        self.E.remove((u, v))
        self.c.pop((u, v))

    def set_source(self, s):
        """
        set source vertex in the graph.
        :param s: the source vertex
        """
        if s not in self.V:
            raise Exception("Vertex '{}' does not exist!!!".format(s))
        else:
            self.s = s

    def set_target(self, t):
        """
        set the target vertex in the graph.
        :param t: the target vertex
        """
        if t not in self.V:
            raise Exception("Vertex '{}' does not exist!!!".format(t))
        else:
            self.t = t

    def set_capacity(self, u, v, c):
        """
        set the capacity for an edge in the graph.
        :param u: the "from" vertex
        :param v: the "to" vertex
        :param c: the capacity of edge(u, v)
        """
        if (u, v) not in self.E:
            raise Exception("Edge from '{}' to '{}' does not exist!!!".format(u, v))
        else:
            self.c[(u, v)] = c

    def has_vertex(self, v):
        return v in self.V

    def has_edge(self, u, v):
        return (u, v) in self.E

    def get_vertices_outgoing_from(self, v):
        """
        get all vertices outgoing from v.
        :param v: the vertex to be queried
        :return: a list of vertices outgoing from v
        """
        res = []
        for (i, j) in self.E:
            if v == i:
                res.append(j)
        res.sort()
        return res

    def get_vertices_incoming_to(self, v):
        """
        get all vertices incoming to v.
        :param v: the vertex to be queried
        :return: a list of vertices incoming to v
        """
        res = []
        for (i, j) in self.E:
            if v == j:
                res.append(i)
        res.sort()
        return res

    def get_capacity(self, u, v):
        """
        get the capacity of an edge in the graph
        :param u: the "from" vertex
        :param v: the "to" vertex
        :return: the capacity of edge (u, v)
        """
        return self.c[(u, v)]

    def __str__(self):
        string = "Graph:\n"
        string += "  Vertices: \n    "
        string += ", ".join(list(self.V))
        string += "\n"
        string += "  Source: {}, target: {}\n".format(self.s, self.t)
        string += "  Edges and capacities:\n"
        for (u, v) in self.c:
            string += "    {} -> {}: {}".format(u, v, self.c[(u, v)])
            string += "\n"
        return string

