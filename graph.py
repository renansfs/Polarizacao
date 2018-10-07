import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import networkx as nx
import matplotlib.pyplot as plt

class Graph(object):

    def __init__(self):
        self.politicians = dict()
        self.G = nx.Graph()
    
    def createPoliticianNode(self, politicians):

        for policitian in politicians:
            self.politicians[policitian.politicianId] = policitian.politicianName
        
        self.G = nx.path_graph(len(politicians))
        H = nx.relabel_nodes(self.G, self.politicians)

        nx.draw(H)
        plt.show() 
