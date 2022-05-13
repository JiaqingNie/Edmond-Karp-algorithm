from Edmond_Karp import *


if __name__ == '__main__':
    G = read_graph()
    f = Edmond_Karp(G)
    show_flow(f.get_flow())

