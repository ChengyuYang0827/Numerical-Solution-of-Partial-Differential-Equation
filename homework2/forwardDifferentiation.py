import numpy as np
import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# from itertools import product

class forwardDifferentiation:
	def __init__(self,problem,spaceStep,timeStep):
		self.spaceStep=spaceStep
		self.timeStep=timeStep
		self.r=1.0*problem.a*self.timeStep/(math.pow(self.spaceStep,2))
		self.N=int((problem.xRight-problem.xLeft)/self.spaceStep)
		self.M=int((problem.tRight-problem.tLeft)/self.timeStep)
		self.error=[]


		self.preciseAns=[]
		# from 0 to M
		for i in range(0,self.M+1):
			self.preciseAns.append([])
			# from 0 to N
			for j in range(0,self.N+1):
				x=problem.xLeft+self.spaceStep*j;
				t=problem.tLeft+self.timeStep*i;
				self.preciseAns[i].append(problem.preciseAns(x,t))

		self.numericalAns=[]
		# from 0 to M
		for i in range(0,self.M+1):
			self.numericalAns.append([])
			# x from 0 to N
			for j in range(0,self.N+1):
				if i==0:
					x=problem.xLeft+self.spaceStep*j
					self.numericalAns[0].append(problem.ux0(x))
				else:
					if j==0:
						self.numericalAns[i].append(problem.ult)
					elif j!=self.N:
						self.numericalAns[i].append(0)
					else:
						self.numericalAns[i].append(problem.urt)


	def numericalSolution(self,problem):
		I=np.eye(self.N-1)
		C=np.eye(self.N-1,k=1)+np.eye(self.N-1,k=-1)
		f=problem.f*np.ones(self.N-1)

		self.numericalAns=np.array(self.numericalAns)
		self.preciseAns=np.array(self.preciseAns)

		for k in range(0,self.M):
			self.numericalAns[k+1,1:self.N]=np.dot((1.0 -2*self.r)*I+self.r*C,self.numericalAns[k,1:self.N])+self.timeStep*f

	def getError(self):
		for i in range(0,self.M+1):
			self.error.append([])
			for j in range(0,self.N+1):
				self.error[i].append(abs(self.numericalAns[i][j]-self.preciseAns[i][j]))
		return self.error


	def showMaxError(self):
		maxE=0.0
		for row in self.error:
			for singleE in row:
				if singleE>maxE:
					maxE=singleE
		print("max error:"+str(maxE))
		return maxE



	def showPicture(self,problem):
		# print(type(self.numericalAns))
		figure=plt.figure()
		figure.canvas.set_window_title('forward differentiation')
		ax=Axes3D(figure)

		T=np.arange(problem.tLeft,problem.tRight+self.timeStep,self.timeStep)
		X=np.arange(problem.xLeft,problem.xRight+self.spaceStep,self.spaceStep)
		T,X=np.meshgrid(T,X)
		Z=2*np.power(np.e,-T*np.power(np.pi,2)/4.0)*np.sin(2*np.pi*X)
		# Z=np.array(self.numericalAns).transpose()
		ax.plot_surface(T,X,Z,cmap="rainbow")
		plt.show()



	def showMat(self,mat,name):
		print(name+":")
		for i in range(0,len(mat)):
			print(mat[i])
		print("\n")

		










