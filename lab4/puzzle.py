import numpy as np

class Environment:
	def __init__(self):
		self.n= int(input("Please enter number n : "))
		self.a =np.zeros((self.n,self.n),dtype='int') 
		print("Please enter the elements : ")
		for i in range(0,self.n):
			for j in range (0,self.n):
				self.a[i][j]=int (input(""))     #random state input
		self.x=self.n-1                          #location of empty box
		self.y=self.n-1
	def parity(self):
		count=0
		# for i in range(0,self.n):
		# 	for j in range (0,self.n):
		# 		if((i,j)==(self.x,self.y)):
		# 			self.d=(self.n-1-self.x)+(self.n-1-self.y)  #calculating d(s)
		# 			continue
		# 		for k in range (0,self.n):
		# 			for l in range (0,self.n):
		# 				if((k,l)==(self.x,self.y)):
		# 					continue
		# 				if(i==k and j<l):    #parity calculation
		# 					if(self.a[i][j]>self.a[k][l]):count=count+1
		# 				if(i<k ):
		# 					if(self.a[i][j]>self.a[k][l]):count=count+1

		b=a.flatten()
		for i in range(0,self.n*self.n):
			for j in range(i+1,self.n*self.n)
				if b[i]>b[j]:count=count+1
		self.d=(self.n-1-self.x)+(self.n-1-self.y)

		par=(count+self.d)%2
		print(par)

class Agent:
	def action(self):
		if(self.action=='right' and s.y+1<s.n):
			(s.a[s.x][s.y],s.a[s.x][s.y+1])=(s.a[s.x][s.y+1],s.a[s.x][s.y])
			s.parity()
		if(self.action=='left'and s.y-1>=0):
			(s.a[s.x][s.y],s.a[s.x][s.y-1])=(s.a[s.x][s.y-1],s.a[s.x][s.y])
			s.parity()
		if(self.action=='up' and s.x-1>=0):
			(s.a[s.x][s.y],s.a[s.x-1][s.y])=(s.a[s.x-1][s.y],s.a[s.x][s.y])
			s.parity()
		if(self.action=='down' and s.x+1<s.n):
			(s.a[s.x][s.y],s.a[s.x+1][s.y])=(s.a[s.x+1][s.y],s.a[s.x][s.y])
			s.parity()


s=Environment()
s.parity()



# def printBoard(self):
#         print(''.center(4,'=')*self.n)
#         for i in self.grid:
#             for j in i:
#                 c=str(j)
#                 if(j == self.n*self.n):
#                     c = 'X'
#                 print(c.center(4,' '),end='')
#             print('\n')

#         print(''.center(4,'=')*self.n)