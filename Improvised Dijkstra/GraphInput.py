import networkx as nx
import csv
import math

def dist(Node1,Node2):
	x1=Node1[0]
	y1=Node1[1]
	x2=Node2[0]
	y2=Node2[1]

	distance=float(math.pow(math.pow((x2-x1),2)+math.pow((y2-y1),2),0.5))
	#print(distance)
	return distance




NodeFile=open("bnk_node.csv",'w')
NF=csv.writer(NodeFile)
NodeList=[]
NodeDict={}  #Nodedict = (x,y): index

EdgeInput=open("q_result.csv",'r')
EI=csv.reader(EdgeInput)

EdgeFile=open("bnk_edge.csv",'w')
EF=csv.writer(EdgeFile)
index=1
for l in EI:
	#ll=str(l[0]).replace('(',':').replace(' ',':').replace(',',':').replace(')',':').split(':')
	print(l)
	ll=str(l[0]).split()
	#print(ll[1])
	#print(ll[2])
	#print(ll[4])
	#print(ll[5])
	#print(ll[8])
	#print(len(ll))
	Node1=(float(ll[1]),float(ll[2]))
	Node2=(float(ll[4]),float(ll[5]))
	if(Node1 not in NodeList):
		NodeList.append(Node1)
		NF.writerow([index,Node1[0],Node1[1]])
		NodeDict[Node1]=index
		index+=1
	if(Node2 not in NodeList):
		NodeList.append(Node2)
		NF.writerow([index,Node2[0],Node2[1]])
		NodeDict[Node2]=index
		index+=1

	#dist(Node1,Node2)
	#dist(Node2,Node1)
	EF.writerow([NodeDict[Node1] , NodeDict[Node2] , int(ll[8]),dist(Node1,Node2)])
	EF.writerow([NodeDict[Node2] , NodeDict[Node1] , int(ll[8]),dist(Node1,Node2)])


NodeFile.close()
EdgeFile.close()
EdgeInput.close()
