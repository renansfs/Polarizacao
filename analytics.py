#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.politician import Politician
from infra.db import DataBase
from model.hashtag import HashTags
from util.writer import Writer
from graph import Graph
import urllib3
import csv
import plotly.plotly as py
import plotly.graph_objs as go
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



dbName = "Politicians"


def getHashtags():
    result = HashTags()
    politicians = Politician.getPoliticians()    
    ffile = open("AllHashTags.csv", "a+", encoding="utf8")

    for politician in politicians:
        myDb = DataBase(dbName, politician.politicianName)
        political = myDb.read(politician.politicianId)
        for followers in political:
            hashtags = followers["hashtags"]
            
            for hashtag in hashtags:
                result.addHashTag(hashtag)
    
    result.Reverse()
    for key in result.getHashTags().keys():
        ffile.write("%s; %s \n" %(key, result.getHashTags()[key]))
    ffile.close()
    return result

def getDictHashtags():
    result = dict()
    politicians = Politician.getPoliticians()    
    
    for politician in politicians:
        ffile = open("HashTags"+politician.politicianName+".csv", "a+", encoding="utf8")
        myDb = DataBase(dbName, politician.politicianName)
        political = myDb.read(politician.politicianId)
        result[politician.politicianName] = HashTags()

        for followers in political:
            hashtags = followers["hashtags"]

            for hashtag in hashtags:
                result[politician.politicianName].addHashTag(hashtag)
        result[politician.politicianName].Reverse()
        for key in result[politician.politicianName].getHashTags().keys():
            ffile.write("%s; %s \n" %(key, result[politician.politicianName].getHashTags()[key]))
        ffile.close()
            
    return result

    
def createGraphByPolitician(offset):
    politicians = Politician.getPoliticians()

    G = nx.Graph()
    for politician in politicians:
        ffile = open("Dados/HashTags"+politician.politicianName+".csv", "r", encoding="utf8")
        reader = csv.reader(ffile, delimiter=';')

        i=0
        for hash in reader:
            G.add_edge(politician.politicianName, hash[0], weight=0.6)
            if i == offset:
                break
            i= i + 1

    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.5]
    
    pos = nx.spring_layout(G)

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=2000)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6, edge_color='r')
    nx.draw_networkx_edges(G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color='b', style='dashed')

    # labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

    plt.axis('off')
    plt.show()

def main():
    #PoliticiansHash = getDictHashtags()
    #HashTags = getHashtags()

    #for hashes in PoliticiansHash:
    #    for h in PoliticiansHash[hashes].getHashTags():
    #        pass
            #print (h)
    #myGraph = Graph()
    #myGraph.createPoliticianNode(Politician.getPoliticians())
    createGraphByPolitician(10)
    print ("Done!")

if __name__ == "__main__":
    main() 