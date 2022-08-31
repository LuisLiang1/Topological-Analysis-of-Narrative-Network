#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:25:47 2022

@author: luisliang
"""
import networkx as nx
from collections import Counter
import matplotlib.pyplot as plt
# Network Graph part

# Prepare for the data

def net_graph_data(clean_edge_ls):
    # Covert tuple to list
    triple_list=[]
    for x in clean_edge_ls:
        tup=[]
        for i in range(3):
            tup.append(x[i])
        triple_list.append(tup)
    # Get S O lists saperately
    col_1=[x[0] for x in triple_list]
    col_3=[x[2] for x in triple_list]
    # Connect S and O
    col_final=col_1+col_3
    # Count the number of nodes
    result={**Counter(col_final)}
    return triple_list,result

# Graph information: G

def construct_G(triple_list):
    # select the basic style
    #G = nx.DiGraph(directed=True)
    G=nx.DiGraph(directed=True)
    # Add_edges
    for x in triple_list:
        G.add_edge(x[0],x[2],edge_label=x[1])
    return G

# Draw graph process

def draw_net_graph(triple_list,result):
    # Select the basic style
    G = nx.DiGraph(directed=True)
    # Add_edges
    for x in triple_list:
        G.add_edge(x[0],x[2],edge_label=x[1])
    pos = nx.spring_layout(G, k=1,seed=700)
    # Get the edge_labels
    edge_labels = dict([((n1, n2), n3)
                    for n1, n2,n3 in G.edges(data='edge_label')])
    # Get the Keys and Values
    keys=[]
    for x in result.keys():
        keys.append(x)
    values=[]
    for x in result.values():
        values.append(x)
    # Set the basic parameters of figure
    avg=sum(values)/len(values)
    plt.figure(3,figsize=(20,20),dpi=100) 
    # Draw the graph
    for x in range(len(keys)):
        if values[x]>200:
            color='salmon'
        elif values[x]>100:
            color='orange'
        else:
            color='forestgreen'
        node_size=values[x]*20,
        node_list=[]
        node_list.append(keys[x])
        f_size=10+values[x]/avg*5
        
        nx.draw_networkx_nodes(G, pos,nodelist=node_list,node_size=node_size,node_color=color)
        
    if len(result.keys())<20:
        f_size=25
    elif len(result.keys())<100:
        f_size=20
    else:
        f_size=15
        
    elarge = [(u, v) for (u, v, d) in G.edges(data=True)]
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=0.5,arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_labels(G, pos, font_size=f_size, font_family="sans-serif")
    
    plt.axis("off")
    plt.tight_layout()
    plt.show()  