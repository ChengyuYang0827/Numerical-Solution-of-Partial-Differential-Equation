import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# 0 < x < 1; 0 < t < 1
class Problem():
	def __init__(self,a,u_x_0,ut_x_0,u_0_t,u_1_t,u_x_t):
		self.a = a
		self.u_x_0 = u_x_0
		self.ut_x_0 = ut_x_0
		self.u_0_t = u_0_t
		self.u_1_t = u_1_t
		self.u_x_t = u_x_t



def secondOrder(timeStep,spaceStep,problem):
	r=problem.a * timeStep / spaceStep
	M = int(1.0/spaceStep)
	N = int(1.0/timeStep)
	u_x_0 = problem.u_x_0
	ut_x_0 = problem.ut_x_0
	u_0_t = problem.u_0_t
	u_1_t = problem.u_1_t
	u_x_t = problem.u_x_t

	# M+1 dots on spaceAxis and N+1 dots on timeAxis
	spaceAxis = np.linspace(0,1,M+1)
	timeAxis = np.linspace(0,1,N+1)


	u = np.zeros((M+1,N+1))
	preciseAns = np.zeros((M+1,N+1))
	error = np.zeros((M+1,N +1))
	#initialize boundary value
	for j in range(0,M+1):
		u[j,0] = u_x_0(spaceAxis[j])

	for k in range(0,N+1):
		u[0,k] = u_0_t(timeAxis[k])
		u[M,k] = u_1_t(timeAxis[k])

	for j in range(1,M):
		u[j,1]=r*r*0.5*(u[j-1,0]+u[j+1,0])+(1-r*r)*u[j,0]+timeStep*ut_x_0(spaceAxis[j])


	for k in range(1,N):
		for j in range(1,M):
			u[j,k+1]=r*r*(u[j-1,k]+u[j+1,k])+2*(1-r*r)*u[j,k]-u[j,k-1]


	maxError = -1
	for j in range(0,M+1):
		for k in range(0,N+1):
			preciseAns[j,k] =  u_x_t(spaceAxis[j],timeAxis[k])
			error[j,k] = np.absolute(preciseAns[j,k]-u[j,k])
			if error[j,k]>maxError:
				maxError=error[j,k]

	return u,preciseAns,error,maxError,timeAxis,spaceAxis


def problem_one(timeStep,spaceStep):
	def ux0(x):
		return np.sin(np.pi*x)


	def utx0(x):
		return 0

	def u0t(x):
		return 0

	def u1t(x):
		return 0

	def uxt(x,t):
		return np.cos(np.pi*t) * np.sin(np.pi*x)

	problem1 = Problem(1,ux0,utx0,u0t,u1t,uxt)
	numericalAns, preciseAns, error, maxError ,timeAxis, spaceAxis= secondOrder(timeStep,spaceStep,problem1)
	# print("numerical answer:\n{}".format(numericalAns))
	# print("precise answer:\n{}".format(preciseAns))
	# print("error:\n{}".format(error))
	print("timeStep={},spaceStep={},maxError:{}".format(timeStep,spaceStep,maxError))
	return numericalAns,maxError,error

#unstable
print("stablity analisis:")
problem_one(0.005,0.01)
problem_one(0.01,0.01)
problem_one(0.02,0.01)
print("\n")

print("convergance analysis:")
spaceSteps=[0.01,0.02,0.04,0.05,0.1]
maxErrors=[]
for spaceStep in spaceSteps:
	_,maxError,_ = problem_one(0.001,spaceStep)
	maxErrors.append(maxError)

plt.plot(np.log(spaceSteps),np.log(maxErrors))
plt.title("error analysis")
plt.xlabel("ln(spaceSteps)")
plt.ylabel("ln(maxErrors)")
plt.show()

fig = plt.figure()
ax = Axes3D(fig)
x1 = np.linspace(0,1,101)
y1 = np.linspace(0,1,101)
x1,y1 = np.meshgrid(x1,y1)
z1 = np.cos(np.pi*x1) * np.sin(np.pi*y1)
numericalAns,_ ,error= problem_one(0.01,0.01)
print(numericalAns.shape)
# ax.plot_surface(x1,y1,numericalAns,rstride=1,cstride=1,cmap='rainbow')
ax.plot_surface(x1,y1,error,rstride=1,cstride=1,cmap='rainbow')
plt.title("numerical answer")
plt.xlabel("time")
plt.ylabel("space")
plt.show()




