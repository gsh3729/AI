import math
import numpy
count=0
l=5;

x = math.ceil(l/2)
y = math.ceil(l/2)
z = math.ceil(l/2)

while x!=l or y!=l or z!=l :
	rand = numpy.random.randint(6)
	count = count + 1
	if rand==0 and y!=l:
		print x,y,z,"Up"
		y+=1
	if rand==1 and y!=0:
		print x,y,z,"Down"
		y-=1
	if rand==2 and z!=l:
		print x,y,z,"Front"
		z+=1
	if rand==3 and z!=0:
		print x,y,z,"Back"
		z-=1
	if rand==4 and x!=l:
		print x,y,z,"Right"
		x+=1
	if rand==5 and x!=0:
		print x,y,z,"Left"
		x-=1

print "Destination reached"
print count


class Agent:





class Environment:


