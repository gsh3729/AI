import numpy as np
import random 
import string
import random

# target_chromosome = "harshalovesgeneticalgorithm" #27+3

# # random_chromosome = "IIT Palakkad kerela"



# #create population
# population = []
# fitness = []
# def create_population():
# 	i=0
# 	while i<10:
# 		j=0
# 		random_chromosome=''
# 		fitness_value=0

# 		while (j<30):
# 			random_chromosome = ''.join([random.choice(string.ascii_letters) for n in xrange(30)])
# 			j=j+1

# 		print random_chromosome

# 		fitness_value = string_distance(random_chromosome,"harshalovesgeneticalgorithm")

# 		print random_chromosome
# 		print fitness_value
# 		population.append(random_chromosome)
# 		fitness.append(fitness_value)
# 		i=i+1




# def string_distance(x,y):
# 	i=0
# 	dist=0
# 	while(i<len(x)) :
# 		dist=dist+abs(ord(x[i])-ord(y[i]))
# 		i=i+1
# 	return dist

# print string_distance("harsha","ibqtgb")

# sample = "harsha"

# # print sample[1:3]

# def string_crossover(x,y):
# 	z = y[0:2]+x[2:8]+y[8:]
# 	return z

# print string_crossover("isharshagod","isvishnudevil")

# def string_mutation(x):
# 	x = list(x)
# 	x[random.randint(0,len(x)-1)] = chr(random.randint(65,90))
# 	''.join(x);
# 	print x

# string_mutation("harsha")

# def target_comparison(x):
# 	return x==self.target_chromosome

# # ss=list("harsha")
# # ss[0]=chr(random.randint(65,122))
# # print ss
# # print len(ss)
# # # sample[3]=chr(65)
# # print sample

# # ss = list(ss)
# # print ss

def find_fittest_two():
	mini = 0
	i=0
	index1=0
	for i in range(len(fitness)):
		if fitness[i]<mini:
			mini = fitness[i]
			index1=i
		i=i+1

	min2 = 0
	i=0
	index2=0
	for i in range(len(fitness)):
		if fitness[i]<mini and i!=index1 :
			mini = fitness[i]
			index2=i
		i=i+1
	return index1,index2

fitness = [2,1,4,2,1,5]
iii,jjj = find_fittest_two()	
print iii
print jjj




# # generation=0
# create_population()
# while (1):
# 	find_fittest_two()
# 	index1, index2 = np.random.randint(0,len(population),2)






# 	print "Generation: ",generation,"\t";
# 	print "String: " population[0].chromosome  "\t";
# 	print "Fitness: "  population[0].fitness   "\n"; 
# 	generation=generation+1
	



