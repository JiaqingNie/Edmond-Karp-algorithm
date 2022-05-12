class Flow:
    """
    Data structure of the flow network of a given graph.
    """

    def __init__(self, G):
        self.f = {}
        self.s = G.s
        self.t = G.t

    def augment(self, fp):
        """
        augment the flow with the given flow.
        :param fp: the given flow
        """
        for (u, v) in fp.f:
            if (u, v) in self.f:
                self.f[(u, v)] += fp.f[(u, v)]
            elif (v, u) in self.f:
                self.f[(v, u)] -= fp.f[(u, v)]
                temp = self.f[(v, u)]
                if temp <= 0:
                    self.f.pop((v, u))
                    if temp < 0:
                        self.f[(u, v)] = (- temp)
            else:
                self.f[(u, v)] = fp.f[(u, v)]

    def add_flow(self, u, v, c):
        """
        add flow to the current flow network
        :param u: the "from" vertex
        :param v: the "to" vertex
        :param c: the capacity
        """
        self.f[(u, v)] = c

    def get_flow(self):
        """
        get the flow network in forms of tuple (u, v, c).
        :return: a list of tuples
        """
        res = []
        for (u, v) in self.f:
            temp = (u, v, self.f[(u, v)])
            res.append(temp)
        return res

    def value(self):
        """
        the value of flows from s to t.
        :return: the value of flows
        """
        res = 0
        for (u, v) in self.f:
            if u == self.s:
                res += self.f[(u, v)]
        return res
