import networkx as nx
import csv
import sys

def Segments(PathArray,FloodLevel):
	"""
	PathArray is a list of nodes in the path where each node is represented as below list
	[Cost,Node,Parent,Strength of edge from previous node]

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
			if(PathArray[i][3]<FloodLevel):
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

def searchPL(dest,PL):

		for i in range(0,len(PL)):
			if(PL[i][0]==dest):
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
		self.permanent_list=list()
		self.temp_list=list()
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

	def dijkstra(self,root,dest):
		
		#start
		cnt=-1  #Counter for permanent list
		cnt1=0 #Counter for tentative list
		index=-1
		index1=-1


		self.temp_list.append(list())
		self.temp_list[cnt1].append(root) #storing root node
		self.temp_list[cnt1].append(0) #storing distance
		self.temp_list[cnt1].append(root) #storing predecessor
		self.temp_list[cnt1].append(-1) # storing strength

		#temp=list() #This list stores the cost of reaching each node in the tentative list 
		temp1=list() #This list stores the vertices in tentative list
		temp2=list() #This list stores the vertices in permanent list
	
		#temp.append(self.temp_list[cnt1][1])
		temp1.append(self.temp_list[cnt1][0])

		src=root
		


		while(len(self.temp_list)!=0):
			#sys.stdin.read(1)
			index=0
			#print(self.permanent_list)
			print(self.temp_list)

			min_val=9999999
			index=-1
			for i in range(0,len(self.temp_list)):
				if(self.temp_list[i][1]<min_val):
					min_val=self.temp_list[i][1]
					index=i


			
			print("MINIMUM NODE INDEX: "+str(self.temp_list[index][0]))

			cnt+=1 #as node with minimum cost shifted to permanent list
			#print("Count for permanent list: "+str(cnt))
			self.permanent_list.append(list())
			self.permanent_list[cnt].append(self.temp_list[index][0])
			self.permanent_list[cnt].append(self.temp_list[index][1])
			self.permanent_list[cnt].append(self.temp_list[index][2])
			self.permanent_list[cnt].append(self.temp_list[index][3])

			temp2.append(self.permanent_list[cnt][0])
			src=self.temp_list[index][0]
			del(self.temp_list[index])
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
						cnt1+=1					#Adjacent nodes added to the tentative list if not there
						self.temp_list.append(list())
						self.temp_list[cnt1].append(self.edges[i].dest)
						temp1.append(self.edges[i].dest)
						#temp.append(self.edges[i].weight+float(self.permanent_list[cnt][1]))
						self.temp_list[cnt1].append(self.edges[i].weight+float(self.permanent_list[cnt][1]))
						self.temp_list[cnt1].append(self.edges[i].src) #Storing predecessor
						self.temp_list[cnt1].append(self.edges[i].strength)
						#print("Cost:"+str(self.temp_list[cnt1][1]))
						
					elif(self.edges[i].dest in temp1 and self.edges[i].dest not in temp2):
						for j in range(0,len(self.temp_list)):
							if(self.temp_list[j][0]==self.edges[i].dest):
								index1=j
								break
						print("Index1:"+str(index1))

						v=float(self.temp_list[index1][1])
						u=float(self.permanent_list[cnt][1])
						w=float(self.edges[i].weight)
						if(v>=(u+w)):
							self.temp_list[index1][1]=u+w
							#temp[index1]=u+w
							self.temp_list[index1][2]=self.edges[i].src
							self.temp_list[index1][3]=self.edges[i].strength
						#print("Cost:"+str(self.temp_list[index1][1]))



					

			if(src==dest):
				break


		path=[]
		y=end
		while(y!=root):
			#print("Hello")
			for j in range(0,len(g1.permanent_list)):
				if(g1.permanent_list[j][0]==y):
					path.append(g1.permanent_list[j])
					break
			y=g1.permanent_list[j][2]
			#print("y="+str(y))
		
		#print(path)
		for j in range(0,len(g1.permanent_list)):
				if(g1.permanent_list[j][0]==y):
					path.append(g1.permanent_list[j])
					break


		print("Path to reach dest node:"+str(path))
		path.reverse()
		#print(path)
		#for j in range(0,len(path)):
		#	print(str(path[j])+"->")



		#print("Permanent list:"+str(self.permanent_list))

		#return self.permanent_list


		return path

	


	def Improvised_Dijkstra(self,root,end,PA,SL,level,NodeDict):
		#Pass the permanent list as argument to the NodeClosure function
		self.temp_list=[]
		self.permanent_list=[]
		temp1=[]
		temp2=[]

	

		cnt=-1  #Counter for permanent list
		cnt1=0 #Counter for tentative list
		index=-1
		index1=-1


		print("Path Array which has been passed as argument:"+str(PA))
		print("Segment list passes as argument"+str(SL))

		self.temp_list.append(list())
		self.temp_list[cnt1].append(PA[0][0]) #storing root node
		self.temp_list[cnt1].append(PA[0][1]) #storing distance
		self.temp_list[cnt1].append(PA[0][2]) #storing predecessor
		self.temp_list[cnt1].append(PA[0][3]) # storing strength

		temp1.append(self.temp_list[cnt1][0])

		src=root

		while(len(self.temp_list)!=0):
			#sys.stdin.read(1)

			index1=-1
			#print(self.permanent_list)
			#print("Temporary list:"+str(self.temp_list))

			min_val=9999999
			index=-1
			for i in range(0,len(self.temp_list)):
				if(self.temp_list[i][1]<min_val):
					min_val=self.temp_list[i][1]
					index=i

			print("Nodes in Permanent list = "),
			for x in self.permanent_list:
				print(str(x[0])+" "+str(NodeDict[x[0]])+"   ,  "),
			print(" ")

			print("Nodes in Temporary list = "),
			for x in self.temp_list:
				print(str(x[0])+" "+str(NodeDict[x[0]])+"   ,  "),
			print(" ")
			print("MINIMUM NODE INDEX: "+str(self.temp_list[index][0]))
			print("End="+str(end))
			#if(level>=2):
			#	sys.stdin.read(1)
			

			#print("PermanentList:"+str(self.permanent_list))
			#print("Len(temp_list):"+str(len(self.temp_list)))
			#print
			

			if(int(self.temp_list[index][0])==end):
				
				#flag=1
				self.permanent_list.append(self.temp_list[index])
				print("PermanentList:"+str(self.permanent_list))
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

			self.permanent_list,temp2,cflag=NodeClosure(self.permanent_list,PA,SL,self.temp_list[index],end)
			if(cflag==1):
				#print("PermanentList:"+str(self.permanent_list))
				#print("End="+str(end))
				print("END NODE FOUND IN NODE CLOSURE OF "+str(self.temp_list[index]))
				print("END NODE FOUND == TRUE")
				break
			
			#new_len=len(self.permanent_list)




			cnt+=len(temp2) #as node with minimum cost shifted to permanent list
			#print("Count for permanent list: "+str(cnt))
			

			#temp2.append(self.permanent_list[cnt][0])
			#src=self.temp_list[index][0]
			del(self.temp_list[index])
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
						if(self.edges[i].dest not in temp1 and searchPL(self.edges[i].dest,self.permanent_list)==0):
							cnt1+=1					#Adjacent nodes added to the tentative list if not there
							self.temp_list.append(list())
							self.temp_list[cnt1].append(self.edges[i].dest)
							temp1.append(self.edges[i].dest)
							#temp.append(self.edges[i].weight+float(self.permanent_list[cnt][1]))
							self.temp_list[cnt1].append(self.edges[i].weight+float(self.permanent_list[cnt][1]))
							self.temp_list[cnt1].append(self.edges[i].src) #Storing predecessor
							self.temp_list[cnt1].append(self.edges[i].strength)
							#print("Cost:"+str(self.temp_list[cnt1][1]))
							
						elif(self.edges[i].dest in temp1 and self.edges[i].dest not in temp2):
							
							for j in range(0,len(self.temp_list)):
								if(self.temp_list[j][0]==self.edges[i].dest):
									index1=j
									break
							#print("Index1:"+str(index1))
							#print("Len(temp_list):"+str(len(self.temp_list)))
							#print("Len(temp_list):"+str(len(self.temp_list)))
							v=float(self.temp_list[index1][1])
							u=float(self.permanent_list[cnt][1])
							w=float(self.edges[i].weight)
							if(v>=(u+w)):
								self.temp_list[index1][1]=u+w
								#temp[index1]=u+w
								self.temp_list[index1][2]=self.edges[i].src
								self.temp_list[index1][3]=self.edges[i].strength
							#print("Cost:"+str(self.temp_list[index1][1]))



						

			

			#print("Permanent list:"+str(self.permanent_list))

		path=[]
		y=end
		while(y!=root):
			#print("Hello")
			for j in range(0,len(g1.permanent_list)):
				if(g1.permanent_list[j][0]==y):
					path.append(g1.permanent_list[j])
					break
			y=g1.permanent_list[j][2]
			#print("y="+str(y))
		
		#print(path)
		for j in range(0,len(g1.permanent_list)):
				if(g1.permanent_list[j][0]==y):
					path.append(g1.permanent_list[j])
					break
		


		#print("Path to reach dest node:"+str(path))
		path.reverse()
		#print(path)
		#for j in range(0,len(path)):
		#	print(str(path[j])+"->")



		#print("Permanent list:"+str(self.permanent_list))

		#return self.permanent_list


		return path

		
















def search(PathArray,NodeIndex):
	"""
	PathArray is a list of nodes in the path where each node is represented as below list
	[Node,Cost,Parent,Strength of edge from previous node]

	This function searches for a node in the Array and returns its index.
	It returns -1 for not found
	"""
	pos=-1
	for i in range(0,len(PathArray)):
		if(PathArray[i][0]==NodeIndex):
			pos=i
	return pos



def NodeClosure(PermanentList,PathArray,SegmentList,Node,end):
	"""
	Permanent List is the Djikstra`s Permanent List, where each node is represented as
	[Node,Cost,Parent,Strength of edge from previous node]

	PathArray is a list of nodes in the path where each node is represented as below list
	[Node,Cost,Parent,Strength of edge from previous node]

	SegmentList is the list of connected Segments from PathArray as per Segments() function above

	Node is the new node which we have to append to PermanentList. Node is represented as
	[Node,Cost,Parent,Strength of edge from previous node]

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
				Cost=Node[1]+(PathArray[i][1]-PathArray[pos][1])
				PermanentList.append([PathArray[i][0],Cost,PathArray[i][2],PathArray[i][3]])
				temp2.append(PathArray[i][0])
				if(PathArray[i][0]==end):
					flag=1

			break

	

	

	return PermanentList,temp2,flag




def step(strength_count,g1,start,end,Graph,NodeDict):

	for i in range(0,strength_count):
		print("\n\n\n\n\n====================================FLOOD LEVEL "+str(i)+"====================================\n")
		if(i==0):
			#Run normal Dijkstra
			PathArray=g1.dijkstra(start,end)
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
			path="/home/user/Desktop/Intern 2018/Bankura_Ronit/Path"+str(i)
			#nx.write_shp(Graph,path)

	
		elif(i>0):
			#Run improvised Dijkstra
			flag=0
			for j in range(1,len(PathArray)):
				if(PathArray[j][3]<i):
					flag=1
					break
			if(flag==1):

				SL1=Segments(PathArray,i)
				print("PathArray:"+str(PathArray))
				print("Segment list:"+str(SL1))
				PathArray1=g1.Improvised_Dijkstra(start,end,PathArray,SL1,i,NodeDict)
				
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

			
			path="/home/user/Desktop/Intern 2018/Bankura_Ronit/Path"+str(i)
			#nx.write_shp(Graphnew,path)
			
			

			
				

		sys.stdin.read(1)
			#SL=SL1
	



if __name__=="__main__":
	
	NodeDict={}
	#Adjacency={}
	NodeFile=open("bnk_node.csv",'r')
	NF=csv.reader(NodeFile)
	NodeList=[]
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
	Graph=nx.Graph()
	Graph.add_node(NodeDict[start])
	Graph.add_node(NodeDict[end])
	#nx.write_shp(Graph,'bnk_startEndPoints.shp')
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



	step(strcount,g1,start,end,Graph1,NodeDict)


	"""
	PathArray=[
	[0,0,-1,-1],
	[1,3,0,0],
	[2,4,1,0],
	[3,5,2,1],
	[4,6,3,1]]
	#,
	#[5,7,5,1],
	#[6,8,6,3],
	#[7,9,7,3],
	#[8,10,7,3],
	#[9,11,8,3],
	#[10,12,9,3],
	#[11,13,10,1],
	#[12,14,11,1],
	#[13,15,12,1],
	#[14,16,13,3]
	 
	SL=Segments(PathArray,1)
	print("Path Array[Node,Cost,Parent,Strength of Path from previous node] = ")
	for x in PathArray:
		print(x)
	print("Segment List = "+str(SL))
	print("Closure of Node [2,4,1,0] = "+str(NodeClosure([],PathArray,SL,[2,4,1,0])))
	#print("Closure of Node [5,10,10,3] = "+str(NodeClosure([],PathArray,SL,[5,10,10,3])))
	#print("Closure of Node [1,10,10,3] = "+str(NodeClosure([],PathArray,SL,[1,10,10,3])))
	#print("Closure of Node [7,10,10,3] = "+str(NodeClosure([],PathArray,SL,[7,10,10,3])))
	"""