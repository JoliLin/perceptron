import numpy as np
from numpy import random
from pylab import plot, ylim
import matplotlib.pyplot as plt

zerone = lambda x: 0 if x < 0 else 1

#node1
x1 = [0, 0, 1, 1]
#node2
x2 = [0, 1, 0, 1]
#threshold
bias = [1, 1, 1, 1]	
#target
target = [0, 0, 0 ,1]	

w = random.rand(3)
#learning rate
eta = 0.2

matrix = [x1, x2, bias]

errors = []

#def andGate( wrecent ) :
while(1) :
	result = np.dot(w, matrix)
	r = []
	for i in result :
		r.append( zerone(i) )
	
	error = np.subtract( target,r )
	errors.append( error )
	mt =  np.transpose(matrix)

	np.subtract( target, matrix )
	w += eta * np.dot( error, mt )
	
	x = 0
	for i in error :
		x += i
	
	if x == 0 :
		break
		
for x in np.transpose(matrix) :
	result = np.dot(x,w )
	print( '{}: {} -> {}'.format(x[:2], result, zerone(result)))
#if __name__ == '__main__' :
#	andGate( w )

ylim([-1,1])	
plt.plot(errors)
plt.show()    
