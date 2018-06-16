import networkx as nx
import csv
import sys
import math

def search(PathArray,NodeIndex):
	"""
	PathArray is a list of nodes in the path where each node is represented as below list
	[Node,Parent,f,g,h,Strength of edge from previous node]

	This function searches for a node in the Array and returns its index.
	It returns -1 for not found
	"""
	pos=-1
	for i in range(0,len(PathArray)):
		if(PathArray[i][0]==NodeIndex):
			pos=i
	return pos



def NodeClosure(PermanentList,PathArray,SegmentList,Node,end,H):
	"""
	Permanent List is the Djikstra`s Permanent List, where each node is represented as
	[Node,Parent,f,g,h,Strength of edge from previous node]

	PathArray is a list of nodes in the path where each node is represented as below list
	[Node,Parent,f,g,h,Strength of edge from previous node]

	SegmentList is the list of connected Segments from PathArray as per Segments() function above

	Node is the new node which we have to append to PermanentList. Node is represented as
	[Node,Parent,f,g,h,Strength of edge from previous node]

	This function appends not only Node but also its closure to the Permanent List

	
	"""
	flag=0
	temp2=[] #contains node numbers only which are in the Permanent List
	#print(Node[0])
	if(Node[0]==end):
		flag=1

	index=0
	pos=search(PathArray,Node[0])
	#print(pos)
	temp2.append(Node[0])
	PermanentList.append(Node)
	while(index<len(SegmentList)):
		#print("Index = "+str(index))
		if(pos>SegmentList[index][1]):
			index=index+1
		elif(pos<SegmentList[index][0]):
			#PermanentList.append(Node)
			#temp2.append(Node[0])
			break
		else:
			#PermanentList.append(Node)
			#temp2.append(Node[0])
			for i in range(pos+1,SegmentList[index][1]+1):
				#print("Position appended = "+str(i))
				#lst.append(PathArray[i][0])
				g=Node[3]+(PathArray[i][3]-PathArray[pos][3])
				h=H[Node[0]]
				f=g+h
				PermanentList.append([PathArray[i][0],PathArray[i][1],f,g,h,PathArray[i][5]])
				temp2.append(PathArray[i][0])
				if(PathArray[i][0]==end):
					flag=1

			break

	

	

	return PermanentList,temp2,flag



def Segments(PathArray,FloodLevel):
	"""
	PathArray is a list of nodes in the path where each node is represented as below list
	[Node,Parent,f,g,h,Strength of edge from previous node]

	This function reads the PathArray and creates a LinkedList of connected segments(as per FloodLevel values)
	in the array, such that each node of list represents a connected segment as
	[Index of starting node of segment,Index of ending node of segment]
	"""



	if(FloodLevel!=0):
		SegmentList=[]
		Node1=[0,len(PathArray)-1]
		SegmentList.append(Node1)
		ind=0
		for i in range(1,len(PathArray)):
			if(i-1>=SegmentList[ind][1]):
				ind+=1
			if(PathArray[i][5]<FloodLevel):
				if(i-1>SegmentList[ind][0] and i<SegmentList[ind][1]):
					end=SegmentList[ind][1]
					SegmentList[ind][1]=i-1
					SegmentList.insert(ind+1,[i,end])
				elif(i-1==SegmentList[ind][0] and i<SegmentList[ind][1]):
					SegmentList[ind][0]=i
				elif(i-1>SegmentList[ind][0] and i==SegmentList[ind][1]):
					SegmentList[ind][1]=i-1
				elif(i-1==SegmentList[ind][0] and i==SegmentList[ind][1]):
					del(SegmentList[ind])
		return SegmentList


def searchPL(dest,CL):

		for i in range(0,len(CL)):
			if(CL[i][0]==dest):
				return 1

		return 0

class Edge:
	def __init__(self,src,dest,wt,Strength):
		self.src=src
		self.dest=dest
		self.weight=wt
		self.strength=Strength
		print("Initialisation of edge done.")
	
	def printedges(self):
		print("Source vertex: "+str(self.src))
		print("Destination vertex: "+str(self.dest))
		print("Weight: "+str(self.weight))
		print("Strength: "+str(self.strength))

class Graph2:

	def __init__(self,edgematrix,vertex,e):
		self.nov=vertex
		self.noe=e
		self.closed_list=list()
		self.open_list=list()
		self.edges=list()

		for i in range(0,len(edgematrix)):
			print("Edgematrix: "+str(edgematrix[i]))
			#sys.stdin.read(1)

			self.edge=Edge(edgematrix[i][0],edgematrix[i][1],edgematrix[i][3],edgematrix[i][2])
			self.edges.append(self.edge)

		print("Initialisation of graph done.")

	def printvar(self):
		print("No of vertices:"+str(self.nov))
		print("No of edges:"+str(self.noe))
		print("\n=====EDGES====\n")
		for i in range(self.noe):
			self.edges[i].printedges()

	def Astar(self,root,dest,H):
		
		#start
		cnt=-1  #Counter for permanent list
		cnt1=0 #Counter for tentative list
		index=-1
		index1=-1


		self.open_list.append([root,root,0,0,0,-1])

		
		temp1=list() #This list stores the vertices in open list
		temp2=list() #This list stores the  vertices in closed list
	
		#temp.append(self.temp_list[cnt1][1])
		temp1.append(self.open_list[cnt1][0])

		src=root #src is a temporary variable
		


		while(len(self.open_list)!=0):
			#sys.stdin.read(1)
			#index=0
			#print(self.permanent_list)
			print("Open list:	\n"+str(self.open_list))

			min_val=9999999
			index=-1
			for i in range(0,len(self.open_list)):
				if(self.open_list[i][2]<min_val):
					min_val=self.open_list[i][2]
					index=i


			
			print("MINIMUM NODE INDEX: "+str(self.open_list[index][0]))

			cnt+=1 #as node with minimum cost shifted to permanent list
			#print("Count for permanent list: "+str(cnt))
			self.closed_list.append(self.open_list[index])
			#self.permanent_list[cnt].append(self.temp_list[index][0])
			#self.permanent_list[cnt].append(self.temp_list[index][1])
			#self.permanent_list[cnt].append(self.temp_list[index][2])
			#self.permanent_list[cnt].append(self.temp_list[index][3])

			temp2.append(self.closed_list[cnt][0])   #Append the node index to the temp2 list
			src=self.open_list[index][0]
			del(self.open_list[index])
			#del(temp[index])
			del(temp1[index])

			

			

			cnt1-=1 #as node with minimum cost shifted to permanent list


			

			#print("Count for tentative list: "+str(cnt1))
			#print("Count for permanent list: " + str(cnt))
			

			for i in range(0,self.noe):
				if(self.edges[i].src==src):
					#print("MATCH FOUND! i=:"+str(i))
					print("Adjacent node:"+str(self.edges[i].dest))
					if(self.edges[i].dest not in temp1 and self.edges[i].dest not in temp2):
						cnt1+=1					#Adjacent nodes added to the open list if not there
						self.open_list.append(list())
						self.open_list[cnt1].append(self.edges[i].dest)    #First element : Node index
						temp1.append(self.edges[i].dest)                   #Append the Node Index to temp1
						self.open_list[cnt1].append(self.edges[i].src)     #Storing predecessor
						g=self.edges[i].weight+float(self.closed_list[cnt][3])
						h=H[self.closed_list[cnt][0]]
						f=g+h
						self.open_list[cnt1].append(f)   #Store f
						self.open_list[cnt1].append(g)  #Store g
						self.open_list[cnt1].append(h)  #Store h
						self.open_list[cnt1].append(self.edges[i].strength) #Store strength
						#print("Cost:"+str(self.temp_list[cnt1][1]))
						
					elif(self.edges[i].dest in temp1 and self.edges[i].dest not in temp2):
						for j in range(0,len(self.open_list)):
							if(self.open_list[j][0]==self.edges[i].dest):
								index1=j
								break
						print("Index1:"+str(index1))

						v=float(self.open_list[index1][3])
						u=float(self.closed_list[cnt][3])
						w=float(self.edges[i].weight)
						if(v>=(u+w)):
							self.open_list[index1][3]=u+w        #Update g
							self.open_list[index1][2]=u+w+self.open_list[index1][4]   #Update f
							#temp[index1]=u+w
							self.open_list[index1][1]=self.edges[i].src
							self.open_list[index1][5]=self.edges[i].strength
						#print("Cost:"+str(self.temp_list[index1][1]))



					

			if(src==dest):
				break


		path=[]
		y=end
		while(y!=root):
			#print("Hello")
			for j in range(0,len(g1.closed_list)):
				if(g1.closed_list[j][0]==y):
					path.append(g1.closed_list[j])
					break
			y=g1.closed_list[j][1]
			#print("y="+str(y))
		
		#print(path)
		for j in range(0,len(g1.closed_list)):
				if(g1.closed_list[j][0]==y):
					path.append(g1.closed_list[j])
					break


		print("Path to reach dest node:"+str(path))
		path.reverse()
		#print(path)
		#for j in range(0,len(path)):
		#	print(str(path[j])+"->")



		#print("Permanent list:"+str(self.permanent_list))

		#return self.permanent_list


		return path

	def Improvised_Astar(self,root,end,PA,SL,level,NodeDict,H):
		#Pass the closed list as argument to the NodeClosure function
		self.open_list=[]
		self.closed_list=[]
		temp1=[]
		temp2=[]

	

		cnt=-1  #Counter for closed list
		cnt1=0 #Counter for open list
		index=-1
		index1=-1


		print("Path Array which has been passed as argument:"+str(PA))
		print("Segment list passes as argument"+str(SL))

		self.open_list.append(PA[0])
		#self.temp_list[cnt1].append(PA[0][0]) #storing root node
		#self.temp_list[cnt1].append(PA[0][1]) #storing distance
		#self.temp_list[cnt1].append(PA[0][2]) #storing predecessor
		#self.temp_list[cnt1].append(PA[0][3]) # storing strength

		temp1.append(self.open_list[cnt1][0])

		src=root

		while(len(self.open_list)!=0):
			#sys.stdin.read(1)

			index1=-1
			#print(self.permanent_list)
			#print("Temporary list:"+str(self.temp_list))

			min_val=9999999
			index=-1
			for i in range(0,len(self.open_list)):
				if(self.open_list[i][2]<min_val):
					min_val=self.open_list[i][2]
					index=i

			print("Nodes in Closed list = "),
			for x in self.closed_list:
				print(str(x[0])+" "+str(NodeDict[x[0]])+"   ,  "),
			print(" ")

			print("Nodes in Open list = "),
			for x in self.open_list:
				print(str(x[0])+" "+str(NodeDict[x[0]])+"   ,  "),
			print(" ")
			print("MINIMUM NODE INDEX: "+str(self.open_list[index][0]))
			print("End="+str(end))
			#if(level>=2):
			#	sys.stdin.read(1)
			

			#print("PermanentList:"+str(self.permanent_list))
			#print("Len(temp_list):"+str(len(self.temp_list)))
			#print
			

			if(int(self.open_list[index][0])==end):
				
				#flag=1
				self.closed_list.append(self.open_list[index])
				print("Closed List:"+str(self.closed_list))
				print("End="+str(end))
				print("END NODE FOUND == TRUE")
				break
			

			#print("All neighbours of the above node:")
			#for i in range(0,self.noe):
					#if(self.edges[i].src==int(self.temp_list[index][0])):
						#print("MATCH FOUND! i=:"+str(i))
						#print("Adjacent node:"+str(self.edges[i].dest)+" "+str(self.edges[i].strength)+" "+str(NodeDict[self.edges[i].dest]))
			#prev_len=len(self.permanent_list)
			#if(level==2):
				#sys.stdin.read(1)

			self.closed_list,temp2,cflag=NodeClosure(self.closed_list,PA,SL,self.open_list[index],end,H)
			if(cflag==1):
				#print("PermanentList:"+str(self.permanent_list))
				#print("End="+str(end))
				print("END NODE FOUND IN NODE CLOSURE OF "+str(self.open_list[index]))
				print("END NODE FOUND == TRUE")
				break
			
			#new_len=len(self.permanent_list)




			cnt+=len(temp2) #as node with minimum cost shifted to permanent list
			#print("Count for permanent list: "+str(cnt))
			

			#temp2.append(self.permanent_list[cnt][0])
			#src=self.temp_list[index][0]
			del(self.open_list[index])
			#del(temp[index])
			del(temp1[index])

			

			

			cnt1-=1 #as node with minimum cost shifted to permanent list
			

			#print("Count for tentative list: "+str(cnt1))
			#print("Count for permanent list: " + str(cnt))
			
			for k in temp2:
				for i in range(0,self.noe):
					if(self.edges[i].src==int(k) and self.edges[i].strength>=level):
						#print("MATCH FOUND! i=:"+str(i))
						#print("Adjacent node:"+str(self.edges[i].dest)),
						if(self.edges[i].dest not in temp1 and searchPL(self.edges[i].dest,self.closed_list)==0):
							
							cnt1+=1					#Adjacent nodes added to the open list if not there
							self.open_list.append(list())
							self.open_list[cnt1].append(self.edges[i].dest)    #First element : Node index
							temp1.append(self.edges[i].dest)                   #Append the Node Index to temp1
							self.open_list[cnt1].append(self.edges[i].src)     #Storing predecessor
							g=self.edges[i].weight+float(self.closed_list[cnt][3])
							h=H[self.closed_list[cnt][0]]
							f=g+h
							self.open_list[cnt1].append(f)   #Store f
							self.open_list[cnt1].append(g)  #Store g
							self.open_list[cnt1].append(h)  #Store h
							self.open_list[cnt1].append(self.edges[i].strength) #Store strength
							#print("Cost:"+str(self.temp_list[cnt1][1]))
							
						elif(self.edges[i].dest in temp1 and self.edges[i].dest not in temp2):
							

							for j in range(0,len(self.open_list)):
								if(self.open_list[j][0]==self.edges[i].dest):
									index1=j
									break
							print("Index1:"+str(index1))

							v=float(self.open_list[index1][3])
							u=float(self.closed_list[cnt][3])
							w=float(self.edges[i].weight)
							if(v>=(u+w)):
								self.open_list[index1][3]=u+w        #Update g
								self.open_list[index1][2]=u+w+self.open_list[index1][4]   #Update f
								#temp[index1]=u+w
								self.open_list[index1][1]=self.edges[i].src
								self.open_list[index1][5]=self.edges[i].strength
							#print("Cost:"+str(self.temp_list[index1][1]))



						

			

			#print("Permanent list:"+str(self.permanent_list))

		path=[]
		y=end
		while(y!=root):
			#print("Hello")
			for j in range(0,len(g1.closed_list)):
				if(g1.closed_list[j][0]==y):
					path.append(g1.closed_list[j])
					break
			y=g1.closed_list[j][1]
			#print("y="+str(y))
		
		#print(path)
		for j in range(0,len(g1.closed_list)):
				if(g1.closed_list[j][0]==y):
					path.append(g1.closed_list[j])
					break
		


		#print("Path to reach dest node:"+str(path))
		path.reverse()
		#print(path)
		#for j in range(0,len(path)):
		#	print(str(path[j])+"->")



		#print("Permanent list:"+str(self.permanent_list))

		#return self.permanent_list


		return path

	



def step(strength_count,g1,start,end,Graph,NodeDict,H):

	for i in range(0,strength_count):
		print("\n\n\n\n\n====================================FLOOD LEVEL "+str(i)+"====================================\n")
		if(i==0):
			#Run normal Astar
			#PathArray consists of nodes in the shortest path from the source to the destination. Each node is of the form [nodeindex,predecessor,f,g,h,strength]
			PathArray=g1.Astar(start,end,H)  
			#print("Path Array:"+str(PathArray))
			print("Path=")
			for j in range(0,len(PathArray)):
				print(str(PathArray[j][0])+"->"),

		

			#print("Segment list:"+str(SL))

			#Now plot the graph having the shortest path
			for j in range(1,len(PathArray)-1):
				Graph.add_node(NodeDict[PathArray[j][0]])
				Graph.add_edge(NodeDict[PathArray[j-1][0]],NodeDict[PathArray[j][0]])
			#For the last edge
			Graph.add_edge(NodeDict[PathArray[j][0]],NodeDict[PathArray[j+1][0]])
			path="/home/user/Desktop/Intern 2018/Astar/Path"+str(i)
			nx.write_shp(Graph,path)

		
		elif(i>0):
			#Run improvised Dijkstra
			flag=0
			for j in range(1,len(PathArray)):
				if(PathArray[j][5]<i):
					flag=1
					break
			if(flag==1):

				SL1=Segments(PathArray,i)
				print("PathArray:"+str(PathArray))
				print("Segment list:"+str(SL1))
				PathArray1=g1.Improvised_Astar(start,end,PathArray,SL1,i,NodeDict,H)
				
				PathArray=PathArray1
				
			Graphnew=nx.Graph()

			#Now plot a new graph every time showing new shortest and safest path
		

			print("Path=")
			for j in range(0,len(PathArray)):
				print(str(PathArray[j][0])+"->"),
			for j in range(0,len(PathArray)-1):
				Graphnew.add_node(NodeDict[PathArray[j][0]])
				Graphnew.add_edge(NodeDict[PathArray[j][0]],NodeDict[PathArray[j+1][0]])
			#For the last node
			Graphnew.add_node(NodeDict[PathArray[j][0]])

			
			path="/home/user/Desktop/Intern 2018/Astar/Path"+str(i)
			nx.write_shp(Graphnew,path)

			
			

			
				

		sys.stdin.read(1)
			#SL=SL1
		
def dist(Node1,Node2):
	x1=Node1[0]
	y1=Node1[1]
	x2=Node2[0]
	y2=Node2[1]

	distance=float(math.pow(math.pow((x2-x1),2)+math.pow((y2-y1),2),0.5))
	#print(distance)
	return distance




if __name__=="__main__":
	
	NodeDict={}
	#Adjacency={}
	NodeFile=open("bnk_node.csv",'r')
	NF=csv.reader(NodeFile)
	NodeList=[]
	H={}
	for l in NF:
		NodeList.append(int(l[0]))			#NodeList consists of only the node indices
		C=(float(l[1]),float(l[2]))
		NodeDict[int(l[0])]=C 				#Nodedict: Index:(x-coordinate,y-coordinate)
		#Adjacency[int(l[0])]=[]
	NodeFile.close()
	#print(NodeDict)
	#print(NodeList)

	EdgeFile=open("bnk_edge.csv",'r')
	EF=csv.reader(EdgeFile)
	EdgeList=[]
	for l in EF:
		EdgeList.append([int(l[0]),int(l[1]),int(l[2]),float(l[3])])   #Edge list consists of nodes where each node is [starting index,ending index,Strength]
		#Adjacency[int(l[0])].append([int(l[1]),int(l[2])])

	EdgeFile.close()


	

	print("No of vertices:"+str(len(NodeDict)))
	print("No of edges"+str(len(EdgeList)))


	vertex=len(NodeDict)
	e=len(EdgeList)

	g1=Graph2(EdgeList,vertex,e)
	g1.printvar()
	start=int(input("Enter the starting node index : "))
	end=int(input("Enter the destination node index : "))
	#Find the coordinates of the destination index
	
	Node2=NodeDict[end]


	for i in NodeDict.keys():
		Node1=NodeDict[i]
		H[i]=dist(Node1,Node2)

	print("\nH=\n")
	print(H)





	Graph=nx.Graph()
	Graph.add_node(NodeDict[start])
	Graph.add_node(NodeDict[end])
	nx.write_shp(Graph,'bnk_startEndPoints.shp')
	#Find out how many strength values you have in your data
	strcount=0
	strength=[]
	for i in range(0,e):
		if EdgeList[i][2] not in strength:
			strength.append(EdgeList[i][2])
			strcount+=1

	Graph1=nx.Graph()
	Graph1.add_node(NodeDict[start])
	Graph1.add_node(NodeDict[end])



	step(strcount,g1,start,end,Graph1,NodeDict,H)
