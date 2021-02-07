import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def getMu(a,b):
	return 0.5*(a+np.power(a*a-4*b,0.5))


def problemSolution(a,b,M,N,u,f):
	h1=np.pi/M
	h2=np.pi/N

	mu = getMu(a,b)

	def vBorder(x,y):
		return -(1/mu+1)*u(x,y)

	def uBorder(x,y):
		return u(x,y)


	alpha0=-(2*mu*(1/(h1*h1)+1/(h2*h2)))-b
	alpha1=mu/(h1*h1)
	alpha3=alpha1
	alpha2=mu/(h2*h2)
	alpha4=alpha2

	B = alpha0*np.eye(M-1)+alpha1*np.eye(M-1,k=1)+alpha3*np.eye(M-1,k=-1)
	A = np.zeros(((M-1)*(N-1),(M-1)*(N-1)))
	for i in range(0,N-1):
		A[i*(M-1):i*(M-1)+(M-1),i*(M-1):i*(M-1)+(M-1)] = B
		if i==0:
			A[(M-1):2*(M-1),0:(M-1)] = alpha4*np.eye(M-1)
		elif i==N-2:
			A[(N-3)*(M-1):(N-2)*(M-1),(N-2)*(M-1):(N-1)*(M-1)]=alpha2*np.eye(M-1)
		else:
			A[(i-1)*(M-1):i*(M-1),i*(M-1):i*(M-1)+(M-1)] = alpha2*np.eye(M-1)
			A[(i+1)*(M-1):(i+2)*(M-1),i*(M-1):i*(M-1)+(M-1)]= alpha4*np.eye(M-1)

	F=np.zeros(((M-1)*(N-1),1))
	for index in range(0,(M-1)*(N-1)):
		xNum = index%(M-1)+1
		yNum = int(index/(M-1))+1
		xValue = xNum/M*np.pi
		yValue = yNum/N*np.pi
		F[index]=f(a,b,xValue,yValue)
		if(xNum+1==M):	#right border
			F[index] += (-alpha1)*vBorder(np.pi,yValue)
		if(yNum+1==N):	#up border
			F[index] += (-alpha2)*vBorder(xValue,np.pi)


	V = np.matrix(A).I * F



	alpha0=-(2/mu*(1/(h1*h1)+1/(h2*h2)))-1
	alpha1=1/(mu*h1*h1)
	alpha3=alpha1
	alpha2=1/(mu*h2*h2)
	alpha4=alpha2

	B = alpha0*np.eye(M-1)+alpha1*np.eye(M-1,k=1)+alpha3*np.eye(M-1,k=-1)
	A = np.zeros(((M-1)*(N-1),(M-1)*(N-1)))
	for i in range(0,N-1):
		A[i*(M-1):i*(M-1)+(M-1),i*(M-1):i*(M-1)+(M-1)] = B
		if i==0:
			A[(M-1):2*(M-1),0:(M-1)] = alpha4*np.eye(M-1)
		elif i==N-2:
			A[(N-3)*(M-1):(N-2)*(M-1),(N-2)*(M-1):(N-1)*(M-1)]= alpha2*np.eye(M-1)
		else:
			A[(i-1)*(M-1):i*(M-1),i*(M-1):i*(M-1)+(M-1)]= alpha2*np.eye(M-1)
			A[(i+1)*(M-1):(i+2)*(M-1),i*(M-1):i*(M-1)+(M-1)]= alpha4*np.eye(M-1)
	

	for index in range(0,(M-1)*(N-1)):
		xNum = index%(M-1)+1
		yNum = int(index/(M-1))+1
		xValue = xNum/M*np.pi
		yValue = yNum/N*np.pi
		if(xNum+1==M):	#right border
			V[index]+=(-alpha1)*uBorder(np.pi,yValue)
		if(yNum+1==N):	#up border
			V[index]+=(-alpha2)*uBorder(xValue,np.pi)

	U = np.matrix(A).I * V

	preciseU = np.zeros(((M-1)*(N-1),1))
	for index in range(0,(M-1)*(N-1)):
		xNum = index%(M-1)+1
		yNum = int(index/(M-1))+1
		preciseU[index]=u(xNum/M*np.pi,yNum/N*np.pi)


	# #Draw the picture
	# figure = plt.figure()
	# figure.canvas.set_window_title("Que1")
	# ax = Axes3D(figure)

	# X = np.arange(0,np.pi,np.pi/100)
	# Y = np.arange(0,np.pi,np.pi/100)
	# X,Y = np.meshgrid(X,Y)
	# Z = np.sin(X)*np.sin(Y)

	# ax.plot_surface(X,Y,Z,cmap="rainbow")
	# plt.show()





	#Error analysis
	Errors = np.abs(U-preciseU)
	maxError = 0
	for error in Errors:
		if error>maxError:
			maxError = error
	print("a = "+str(a)+" ,b = "+str(b)+" ,M = "+str(M)+" ,N = "+str(N))
	print("max error:"+str(maxError)+"\n")
	return maxError;


#problem 1
# print("Problem 1")
# def u(x,y):
# 	return np.sin(x)*np.sin(y)

# def f(a,b,x,y):
# 	return  (4+2*a+b)*np.sin(x)*np.sin(y)

# problemSolution(1,0,10,100,u,f)

# M = [3,4,5,6,7,8,9,10,11,12]
# N = 500

# h1 = []
# Errors=[]
# for item in M:
# 	h1.append(np.pi/item)
# 	Errors.append(problemSolution(1,0,item,N,u,f))

#problem2
print("Problem2")
def u(x,y):
	return x*np.sin(y)+y*np.sin(x)

def f(a,b,x,y):
	return (1+a+b)*(x*np.sin(y)+y*np.sin(x))

# problemSolution(1,0,10,100,u,f)
# M = [3,4,5,6,7,8,9,10,11,12]
# N = 500

# h1 = []
# Errors=[]
# for item in M:
# 	h1.append(np.pi/item)
# 	Errors.append(problemSolution(1,0,item,N,u,f))


problemSolution(1,0,10,10,u,f)
problemSolution(1,1/8,10,10,u,f)
problemSolution(2,1/2,10,10,u,f)
problemSolution(3,1,10,10,u,f)