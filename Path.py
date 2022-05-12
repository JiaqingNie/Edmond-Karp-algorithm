from copy import deepcopy
from Flow import Flow


class Path:
    """
    Data structure of a path from s to t.
    It maintains both the path and the value of flow in the path.
    """

    def __init__(self, G, s):
        self.G = G
        if not self.G.has_vertex(s):
            raise Exception("Vertex {} not in Graph!!!".format(s))
        self.path = [s]
        self.flow = None

    def append(self, v):
        """
        add a new vertex into the path and update the flow.
        :param v: the vertex to be added
        """
        last_vertex = self.path[-1]
        if not self.G.has_vertex(v):
            raise Exception("Vertex {} not in Graph!!!".format(v))
        elif not self.G.has_edge(last_vertex, v):
            raise Exception("Edge {} -> {} not in Graph!!!".format(last_vertex, v))
        else:
            self.path.append(v)
            c = self.G.get_capacity(last_vertex, v)
            if not self.flow:
                self.flow = c
            else:
                self.flow = min(self.flow, c)

    def pop(self):
        """
        pop up the last vertex and update the flow.
        """
        self.path.pop()
        if len(self.path) == 1:
            self.flow = None
            return
        if len(self.path) >= 2:
            self.flow = self.G.get_capacity(self.path[0], self.path[1])
            for i in range(2, len(self.path)):
                self.flow = min(self.flow, self.G.get_capacity(self.path[i - 1], self.path[i]))

    def size(self):
        """
        :return: the number of edges along the path
        """
        return len(self.path) - 1

    def tail(self):
        """
        :return: the last vertex in the path
        """
        return self.path[-1]

    def copy(self):
        """
        create a copy of the path.
        :return: a copy of the path
        """
        path = Path(self.G, self.path[0])
        path.path = deepcopy(self.path)
        path.flow = self.flow
        return path

    def get_path_flow(self):
        """
        calculating the flow corresponding to the path.
        :return: a flow for the path
        """
        res = Flow(self.G)
        for i in range(1, len(self.path)):
            res.add_flow(self.path[i - 1], self.path[i], self.flow)
        return res

    def __str__(self):
        string = "Path: \n    "
        string += " -> ".join(self.path)
        string += "    flow: " + str(self.flow) + "\n"
        return string
