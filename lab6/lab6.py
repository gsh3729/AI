import numpy   
import Queue
class Environment:
  
  def __init__(self,n):
     self.goal = numpy.array[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
     self.n = n
     self.state = numpy.arange(0,n*n).reshape(n,n)
     numpy.random.shuffle(self.state)
     k = 0

     for i in range(0,n):
       for j in range(0,n):
         if self.state[i][j] == 0:
           self.empty_index[0] = i
           self.empty_index[1] = j
           k = 1

         if k == 1:
           break

  def percept(self,a):
     if self.goal == a:
       return True
     else:
       return False
  


class Agent:    

    def parity(self):
       result = (2*(self.n-1))-(self.empty_index[0] + self.empty_index[1])

       a = self.state.flatten()
       
       for i in range(0,len(a)):
          for j in range(0,len(a)):
             if j > i:
               if a[j] < a[i]:
                 result += 1

       return result%2

    def move(self,d):

      if d == "r":
        if self.empty_index[0] < (self.n-1):
           i = self.empty_index[0]
           j = self.empty_index[1]
           self.empty_index[0] += 1
           self.state[i][j] = self.state[i+1][j]
           self.state[i+1][j] = 0

      elif d == "l":
        if self.empty_index[0] > 0:
           i = self.empty_index[0]
           j = self.empty_index[1]
           self.empty_index[0] -= 1
           self.state[i][j] = self.state[i-1][j]
           self.state[i-1][j] = 0

      elif d == "u":
        if self.empty_index[1] > 0:
           i = self.empty_index[0]
           j = self.empty_index[1]
           self.empty_index[1] -= 1
           self.state[i][j] = self.state[i][j-1]
           self.state[i][j-1] = 0

      elif d == "d":
        if self.empty_index[1] < (self.n-1):
           i = self.empty_index[0]
           j = self.empty_index[1]
           self.empty_index[1] += 1
           self.state[i][j] = self.state[i][j+1]
           self.state[i][j+1] = 0
    
    def bfs(self):
      
      l = Queue.Queue(maxsize = 1000)
      l.put(self.state)

      if s.percept(l.get()):
        print "Found Goal State"
      
      else:


a = Environment(4)
print(a.state)


# import numpy as np 

# class Environment(object):
# 	"""docstring for Environment"""
# 	def __init__(self, arg):
# 		self.matrix = [[1,1,0,1,1],[1,0,1,0,1],[1,1,0,0,0],[0,1,1,0,1],[0,1,1,0,0]];

# 	def move():
# 		if :
