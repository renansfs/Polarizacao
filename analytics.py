#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.politician import Politician
from infra.db import DataBase
from model.hashtag import HashTags
from util.writer import Writer
from graph import Graph
import csv, random, urllib3
import plotly.plotly as py
import plotly.graph_objs as go
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



dbName = "Politicians"

#Get All Hashtags from the Database
def getAllHashtags():
    result = HashTags()
    politicians = Politician.getPoliticians()
    ffile = open("AllHashTags.csv", "a+", encoding="utf8")

    for politician in politicians:
        myDb = DataBase(dbName, politician.politicianName)
        political = myDb.read(politician.politicianId)
        max = politician.totalFollowers
        count = 0
        for followers in political:
            if int(count) == int(max):
                break
            count += 1
            hashtags = followers["hashtags"]
            for hashtag in hashtags:
                result.addHashTag(hashtag)
            
    result.Reverse()
    for key in result.getHashTags().keys():
        ffile.write("%s; %s \n" %(key, result.getHashTags()[key]))
    ffile.close()
    return result

#Filter and get all nodes and arestas to be applied into Gephi
def getAllNodesAndArestas():
    filtered = list()
    arestas = dict()
    politicians = Politician.getPoliticians()
    
    print("Started")
    for politician in politicians:
        arestas[politician.politicianName] = set()
        with open("Dados/HashTags"+politician.politicianName+".csv", "r", encoding="utf8") as ffile:
            line = ffile.readline()
            filtered.append(politician.politicianName)
            
            count = 0
            while line and count < 100:
                content = line.split(";")
                arestas[politician.politicianName].add(line)
                if content[0] not in filtered:
                    filtered.append(content[0])
                line = ffile.readline()
                count +=1    

            ffile.close()
        
        with open("Dados/Arestas/ArestasBy"+politician.politicianName+".csv", "+a", encoding="utf8") as ffile:
            count = 0
            ffile.write("Source, Target, Type, Id, Label, Weight\n")
            
            for hashtag in arestas[politician.politicianName]:
                line = hashtag.split(";")
                if line[0] in filtered:
                    ffile.write("{},{},Directed,{},{},{}".format(filtered.index(politician.politicianName), filtered.index(line[0]), count, line[0], line[1]))
                    count += 1
            ffile.close()
    
    with open("Dados/Nodes/NodesFiltered.csv", "+a", encoding="utf8") as ftotal:
        count = 0
        ftotal.write("Label, Id\n")
        for line in filtered:
            ftotal.write("{},{}\n".format(line, count))
            count +=1
        ftotal.close()
    
#Get the Hashtags by Politician and Save
def getDictHashtags():
    result = dict()
    politicians = Politician.getPoliticians()    
    
    for politician in politicians:
        ffile = open("HashTags"+politician.politicianName+".csv", "a+", encoding="utf8")
        myDb = DataBase(dbName, politician.politicianName)
        political = myDb.read(politician.politicianId)
        result[politician.politicianName] = HashTags()

        max = politician.totalFollowers
        count = 0
        for followers in political:
            if int(count) == int(max):
                break
            hashtags = followers["hashtags"]
            count += 1

            for hashtag in hashtags:
                result[politician.politicianName].addHashTag(hashtag)
        
        result[politician.politicianName].Reverse()

        for key in result[politician.politicianName].getHashTags().keys():
            ffile.write("%s; %s \n" %(key, result[politician.politicianName].getHashTags()[key]))
        ffile.close()
            
    return result

#No Longer used, creates a graph using Graph
def createGraphByAllPolitician(offset):
    politicians = Politician.getPoliticians()
    listEdges = list()
    G = nx.Graph()
    for politician in politicians:
        ffile = open("Dados/HashTags"+politician.politicianName+".csv", "r", encoding="utf8")
        reader = csv.reader(ffile, delimiter=';')

        i=0
        for hash in reader:
            G.add_edge(politician.politicianName, "#"+hash[0], polId=politician.politicianId)
            if i == offset:
                break
            i= i + 1
        listEdges.append([(u, v) for (u, v, d) in G.edges(data=True) if d['polId'] == politician.politicianId])

    pos = nx.spring_layout(G)

    # nodes
    nx.draw_networkx_nodes(G, pos, node_color='#D0D3D4', node_size=300)

    # edges
    for edge in listEdges:
        color = '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        nx.draw_networkx_edges(G, pos, edgelist=edge, width=6, edge_color=color)

    # labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

    plt.axis('off')
    plt.show()

#No longer use, Create a Graph by politician
def createGraphByEachPolitician(offset):
    politicians = Politician.getPoliticians()
    
    for politician in politicians:
        listEdges = list()
        G = nx.Graph()
        ffile = open("Dados/HashTags"+politician.politicianName+".csv", "r", encoding="utf8")
        reader = csv.reader(ffile, delimiter=';')

        i=0
        for hash in reader:
            G.add_edge(politician.politicianName, "#"+hash[0], polId=politician.politicianId)
            if i == offset:
                break
            i= i + 1
        listEdges.append([(u, v) for (u, v, d) in G.edges(data=True) if d['polId'] == politician.politicianId])

        pos = nx.spring_layout(G)

        # nodes
        nx.draw_networkx_nodes(G, pos, node_color='#D0D3D4', node_size=300)

        # edges
        for edge in listEdges:
            color = '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            nx.draw_networkx_edges(G, pos, edgelist=edge, width=6, edge_color=color)

        # labels
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

        plt.axis('off')
        plt.show()

def main():
    #getDictHashtags()
    #getAllHashtags()
    getAllNodesAndArestas()
    #createGraphByAllPolitician(50)
    #createGraphByEachPolitician(50)
    print ("Done!")

if __name__ == "__main__":
    main() 