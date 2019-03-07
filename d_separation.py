import numpy as np
import argparse

def d_separation(num1, num2, list1):
	# Algorithm implemented from Pseudo Code in the book

	# Input 
	# Source variable
	X = num1
	# Conditioned nodes list (Observations)
	Z = list1
	filename = 'dag.txt'

	# Create numpy matrix of Bayesian network graph, G
	G = np.loadtxt(filename, delimiter =' ',  skiprows=1)
	G = np.delete(G, 0, axis=1)

	# L1: Nodes to be visited
	Ztemp = Z.copy()
	Ztemp[:] = [x - 1 for x in Ztemp]
	L1 = Ztemp

	# A: Ancestors of Z 
	A = []
	for i in range(len(Z)):
		Atemp = np.where(G[:,Z[i]-1]==1)
		A = A + list(Atemp[0])

	while len(L1) > 0:
		Y = L1.pop(0)
		if Y not in A:
			Pa_Y = np.where(G[:,Y]==1)
			L1 = L1 + list(Pa_Y[0]) 
		A = A + [Y]
	
# Phase 2:
	Ztemp1 = Z.copy()
	Ztemp1[:] = [x - 1 for x in Ztemp1]

	# (Node, Direction) to be visited
	L = [(X-1, 'up')]

	# (Node, Direction) marked as visited
	V = []

	# Nodes Reachable
	R = []
	
	while len(L) > 0:
		testNode = L.pop(0)
		Y1 = testNode[0]
		d = testNode[1]

		if testNode not in V:
			if Y1 not in Ztemp1:
				R = R + [Y1] # Add Y1 to Nodes Reachable list 
			V = V + [testNode] # Add testNode = (Y1,d) to the Visited list

			if d == 'up' and Y1 not in Ztemp1: # If Y1 not in Z, trail through Y1 active 
				Pa_Y1 = np.where(G[:,Y1]==1) # Y1's Parents
				Ch_Y1 = np.where(G[Y1,:]==1) # Y1's Children
				for i in range(len(Pa_Y1[0])):
					L = L + [(Pa_Y1[0][i],'up')] #Y1’s parents to be visited (from bottom)
				for i in range(len(Ch_Y1[0])):		
					L = L + [(Ch_Y1[0][i],'down')] #Y1 ’s children to be visited (from top)

			elif d == 'down': #Trails down through Y1
				Pa_Y1 = np.where(G[:,Y1]==1) # Y1's Parents
				Ch_Y1 = np.where(G[Y1,:]==1) # Y1's Children
				if Y1 not in Ztemp1: #Downward trails to Y1 ’s children that are active
					for i in range(len(Ch_Y1[0])):
						L = L + [(Ch_Y1[0][i],'down')] #Y1 ’s children to be visited from top

				if Y1 in A: #check for active path based on v-structure trail
					for i in range(len(Pa_Y1[0])):
						L = L + [(Pa_Y1[0][i],'up')] #Y1’s parents to be visited from bottom

	# Check for d-separation:
	if (num2-1) in R:
		print('FALSE')
		return False
	else:
		print('TRUE')
		return True

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-s', type = int,action='store',
                    dest='num1',
                    help='Store a simple value')
	parser.add_argument('-s1', type = int,action='store',
                    dest='num2',
                    help='Store a simple value')
	parser.add_argument('-list',type = int, nargs = '+', required = False, default=[])
	args=parser.parse_args()

	result = d_separation(args.num1, args.num2, args.list)
if __name__== '__main__':
	Main()







