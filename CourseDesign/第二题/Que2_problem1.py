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
		return k*np.sin(np.pi*x)

	def u(x,t):
		return k*(1-np.power(np.e,-np.pi*np.pi*t))/(np.pi*np.pi)*np.sin(np.pi*x)

	H = (1-2*r)*np.eye(N-1) + r*np.eye(N-1,k=1)+r*np.eye(N-1,k=-1)



	F = np.zeros((N-1,1))
	for i in range(1,N):
		F[i-1] = f(i/N*1,0)


	U = []
	U.append(np.zeros((N-1,1)))
	for i in range(1,M+1):
		U.append(np.matmul(H,U[i-1])+tao*F)



	AccurateU = []
	AccurateU.append(np.zeros((N-1,1)))
	for i in range(1,M+1):
		AccurateU.append(np.zeros((N-1,1)))
		for j in range(1,N):
			AccurateU[i][j-1] = u(j/N*1,i/M*1)
	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
	Errors = []
	for i in range(0,M+1):
		Errors.append(np.abs(U[i]-AccurateU[i]))

	maxError = 0
	for row in Errors:
		for item in row:
			if item>maxError:
				maxError = item
	# print("M="+str(M)+", N="+str(N)+", r="+str(r)+" max error:"+str(maxError))
	print("M="+str(M)+", N="+str(N)+" ,max error:"+str(maxError))
	# print("\n")
	#Draw the picture
	figure = plt.figure()
	figure.canvas.set_window_title("Que2_problem1")
	ax = Axes3D(figure)

	X = np.arange(0,1,1/100)
	T = np.arange(0,1,1/100)
	X,T = np.meshgrid(X,T)
	Z = k*(1-np.power(np.e,-np.pi*np.pi*T))/(np.pi*np.pi)*np.sin(np.pi*X)

	ax.plot_surface(X,T,Z,cmap="rainbow")
	plt.show()

	


def backwardDifferentiation(M,N):
	k = 1000
	a = 1

	h = 1/N
	tao = 1/M

	r = a*tao/(h*h)

	def f(x,t):
		return k*np.sin(np.pi*x)

	def u(x,t):
		return k*(1-np.power(np.e,-np.pi*np.pi*t))/(np.pi*np.pi)*np.sin(np.pi*x)

	H = (1+2*r)*np.eye(N-1) - r*np.eye(N-1,k=1)-r*np.eye(N-1,k=-1)
	H = np.matrix(H).I


	F = np.zeros((N-1,1))
	for i in range(1,N):
		F[i-1] = f(i/N*1,0)


	U = []
	U.append(np.zeros((N-1,1)))
	for i in range(1,M+1):
		U.append(np.matmul(H,U[i-1]+tao*F))



	AccurateU = []
	AccurateU.append(np.zeros((N-1,1)))
	for i in range(1,M+1):
		AccurateU.append(np.zeros((N-1,1)))
		for j in range(1,N):
			AccurateU[i][j-1] = u(j/N*1,i/M*1)
	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
	Errors = []
	for i in range(0,M+1):
		Errors.append(np.abs(U[i]-AccurateU[i]))

	maxError = 0
	for row in Errors:
		for item in row:
			if item>maxError:
				maxError = item
	print("M="+str(M)+", N="+str(N)+", max error:"+str(maxError))
	# print("\n")


#problem1
# M = 1000
# N = [3,4,5,6,7,8,9,10,11,12]
# for item in N:
# 	forwardDifferentiation(M,item)


# N = 1000
# M = [8,10,12,14,16,18,20,22,24,26]
# for item in M:
# 	backwardDifferentiation(item,N)

# forwardDifferentiation(1600,40)
forwardDifferentiation(3200,40)
# forwardDifferentiation(12800,40)
# forwardDifferentiation(3200,80)
# forwardDifferentiation(12800,80)


