import csv
import networkx as nx


G = nx.read_edgelist('Friendship_Flickr.csv', delimiter=',', nodetype=str) 
averageDegree = 0
count=0

with open('degrees.csv', 'w') as f:
    writeit = csv.writer(f, delimiter=',')
    for node in G.nodes():
        count = count + 1
        averageDegree = averageDegree + int(G.degree(node))
        writeit.writerow([str(node)] + [G.degree(node)])
    writeit.writerow(["Average Degree: " + str(averageDegree/count)])

with open('clustering_coefficient.csv', 'w') as f:
    writeit = csv.writer(f, delimiter=',')
    for node in G.nodes():
        writeit.writerow([str(node)] + [nx.clustering(G)]+["\n"])

with open('Betweenness.csv', 'w') as f:
    writeit = csv.writer(f, delimiter=',')
    for node in G.nodes():
        writeit.writerow([str(node)] + [nx.betweenness_centrality(G)]+["\n"])



with open('diameter.csv', 'w') as f:
    writeit = csv.writer(f, delimiter=',')
    for node in G.nodes():
        writeit.writerow([str(node)] + [nx.diameter(G)]+["\n"])

