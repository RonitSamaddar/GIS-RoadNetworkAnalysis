



import networkx as nx
import csv

NodeList=[]
NodeDict={}
Adjacency={}
NodeFile=open("bnk_node.csv",'r')
NF=csv.reader(NodeFile)
for l in NF:
	NodeList.append(int(l[0]))
	C=(float(l[1]),float(l[2]))
	NodeDict[int(l[0])]=C
	Adjacency[int(l[0])]=[]
NodeFile.close()
#print(NodeDict)
#print(NodeList)

EdgeFile=open("bnk_edge.csv",'r')
EF=csv.reader(EdgeFile)
EdgeList=[]
for l in EF:
	EdgeList.append([int(l[0]),int(l[1]),int(l[2])])
#print(len(EdgeList))
EdgeFile.close()
#print(Adjacency)

for FL in range(0,5):
	Graphn=nx.Graph()
	for entry in EdgeList:
		if(entry[2]>=FL):
			if(NodeDict[entry[0]] not in Graphn.nodes()):
				Graphn.add_node(NodeDict[entry[0]])
			if(NodeDict[entry[1]] not in Graphn.nodes()):
				Graphn.add_node(NodeDict[entry[1]])
			Graphn.add_edge(NodeDict[entry[0]],NodeDict[entry[1]])

	#print(Graphn.nodes())
	#print(len(Graphn.edges()))
	outputfile="bnk.road"+str(FL)
	nx.write_shp(Graphn,outputfile)







