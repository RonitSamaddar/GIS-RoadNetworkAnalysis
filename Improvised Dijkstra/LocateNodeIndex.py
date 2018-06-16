"""
Input: 			Coordinates of location
Output:			Index of nearest Node
"""
import csv

NodeFile=open("bnk_node.csv")
NF=csv.reader(NodeFile,delimiter=',')

print("Enter the coordinates of the place(separate by comma no spaces)")
[x,y]=(raw_input().split(','))
x=float(x)
y=float(y)

minn=9999
minIndex=0
minCoord=0
for l in NF:
	Coord=(float(l[1]),float(l[2]))
	#print(Coord[0],type(Coord[0]))
	#rint(x,type(x))
	#print(Coord[1],type(Coord[1]))
	#print(y,type(y))
	Dist=((Coord[0]-x)**2+(Coord[1]-y)**2)**0.5
	if(Dist<minn):
		minn=Dist
		minIndex=int(l[0])
		minCoord=Coord
print("The Index of the Node is = "+str(minIndex))
print("The Actual Coordinates of the Node is = "+str(minCoord))