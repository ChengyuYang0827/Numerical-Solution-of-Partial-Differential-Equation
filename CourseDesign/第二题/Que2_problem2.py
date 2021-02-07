import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def forwardDifferentiation(M,N):

	k = 1000
	a = 1

	h = 1/N
	tao = 1/M

	r = a*tao/(h*h)

	def f(x,t):
		return k*(np.cos(np.pi*x)-np.power(np.e,-np.pi*np.pi*t))

	def u(x,t):
		return k*(1-np.power(np.e,-np.pi*np.pi*t))/(np.pi*np.pi)*(np.cos(np.pi*x)-1)

	H = (1-2*r)*np.eye(N) + r*np.eye(N,k=1)+r*np.eye(N,k=-1)
	H[N-1][N-2]=2*r
	# print(H)

	F = []
	for i in range(0,M+1):
		F.append(np.zeros((N,1)))
		for j in range(1,N+1):
			F[i][j-1] = f(j/N*1,i/M*1)


	U = []
	U.append(np.zeros((N,1)))
	for i in range(1,M+1):
		U.append(np.matmul(H,U[i-1])+tao*F[i-1])



	AccurateU = []
	AccurateU.append(np.zeros((N,1)))
	for i in range(1,M+1):
		AccurateU.append(np.zeros((N,1)))
		for j in range(1,N+1):
			AccurateU[i][j-1] = u(j/N*1,i/M*1)
	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
	Errors = []
	for i in range(0,M+1):
		Errors.append(np.abs(U[i][0:-1]-AccurateU[i][0:-1]))

	maxError = 0
	for row in Errors:
		for item in row:
			if item>maxError:
				maxError = item
	print("M="+str(M)+", N="+str(N)+", max error:"+str(maxError))
	# print("\n")

	#Draw the picture
	figure = plt.figure()
	figure.canvas.set_window_title("Que2_problem2")
	ax = Axes3D(figure)

	X = np.arange(0,1,1/100)
	T = np.arange(0,1,1/100)
	X,T = np.meshgrid(X,T)
	Z = k*(1-np.power(np.e,-np.pi*np.pi*T))/(np.pi*np.pi)*(np.cos(np.pi*X)-1)

	ax.plot_surface(X,T,Z,cmap="rainbow")
	plt.show()


def backwardDifferentiation(M,N):
	
	k = 1000
	a = 1

	h = 1/N
	tao = 1/M

	r = a*tao/(h*h)

	def f(x,t):
		return k*(np.cos(np.pi*x)-np.power(np.e,-np.pi*np.pi*t))

	def u(x,t):
		return k*(1-np.power(np.e,-np.pi*np.pi*t))/(np.pi*np.pi)*(np.cos(np.pi*x)-1)


	H = (1+2*r)*np.eye(N) - r*np.eye(N,k=1)-r*np.eye(N,k=-1)
	H[N-1][N-2]=-2*r
	H = np.matrix(H).I
	# print(H)

	F = []
	for i in range(0,M+1):
		F.append(np.zeros((N,1)))
		for j in range(1,N+1):
			F[i][j-1] = f(j/N*1,i/M*1)


	U = []
	U.append(np.zeros((N,1)))
	for i in range(1,M+1):
		U.append(np.matmul(H,U[i-1]+tao*F[i-1]))



	AccurateU = []
	AccurateU.append(np.zeros((N,1)))
	for i in range(1,M+1):
		AccurateU.append(np.zeros((N,1)))
		for j in range(1,N+1):
			AccurateU[i][j-1] = u(j/N*1,i/M*1)
	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
	Errors = []
	for i in range(0,M+1):
		Errors.append(np.abs(U[i][0:-1]-AccurateU[i][0:-1]))

	maxError = 0
	for row in Errors:
		for item in row:
			if item>maxError:
				maxError = item
	print("M="+str(M)+", N="+str(N)+", max error:"+str(maxError))
	# print("\n")


M = 1000
N = [3,4,5,6,7,8,9,10,11]
for item in N:
	forwardDifferentiation(M,item)


N = 1000
M = [8,10,12,14,16,18,20,22,24,26]
for item in M:
	backwardDifferentiation(item,N)