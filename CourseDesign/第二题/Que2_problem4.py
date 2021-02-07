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

	

	H = (1-2*r)*np.eye(N) + r*np.eye(N,k=1)+r*np.eye(N,k=-1)
	H[0][1]=2*r
	# print(H)

	F = []
	for i in range(0,M+1):
		F.append(np.zeros((N,1)))
		for j in range(0,N):
			F[i][j] = f(j/N*1,i/M*1)



	U = []
	U.append(np.zeros((N,1)))
	for i in range(0,N):
		U[0][i] = 100*(1-i/N*1)
	for i in range(1,M+1):
		U.append(np.matmul(H,U[i-1])+tao*F[i-1])


	print("Forward Differentiation:")
	print("M="+str(M)+", N="+str(N)+", U:\n")
	print(U[-10:-1])
	print("\n")


def backwardDifferentiation(M,N):
	k = 1000
	a = 1

	h = 1/N
	tao = 1/M

	r = a*tao/(h*h)

	def f(x,t):
		return k*np.sin(np.pi*x)

	H = (1+2*r)*np.eye(N) - r*np.eye(N,k=1)-r*np.eye(N,k=-1)

	H[0][1]=-2*r
	H = np.matrix(H).I
	# print(H)

	F = []
	for i in range(0,M+1):
		F.append(np.zeros((N,1)))
		for j in range(0,N):
			F[i][j] = f(j/N*1,i/M*1)


	U = []
	U.append(np.zeros((N,1)))
	for i in range(0,N):
		U[0][i] = 100*(1-i/N*1)
	for i in range(1,M+1):
		U.append(np.matmul(H,U[i-1]+tao*F[i-1]))


	print("M="+str(M)+", N="+str(N)+", U:")
	print(U[-10:-1])
	print("\n")

		#Draw the picture
	figure = plt.figure()
	figure.canvas.set_window_title("Que2_problem4")
	ax = Axes3D(figure)

	X = np.arange(0,1,1/10)
	T = np.arange(0,1,1/1000)
	X,T = np.meshgrid(X,T)
	Z = np.array(U[1:][0:]).reshape(1000,10)
	print(np.shape(Z))

	ax.plot_surface(X,T,Z,cmap="rainbow")
	plt.show()



forwardDifferentiation(1000,10)
backwardDifferentiation(1000,10)