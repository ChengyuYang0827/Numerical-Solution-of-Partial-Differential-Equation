import backwardDifferentiation as bd
import CrankNicolson as ck
import problem as pb
import math
import forwardDifferentiation as fd
import numpy as np
import matplotlib.pyplot as plt

def preciseAns(x,t):
	return math.pow(math.e,-t*math.pow(math.pi,2))*math.sin(math.pi*x)+x*(1-x)

def ux0(x):
	return math.sin(math.pi*x)+x*(1-x)



# 	def __init__(self,a,f,xLeft,xRight,tLeft,tRight,preciseAns,ux0,ult,urt):
problem2=pb.problem(1.0,2.0,0.0,1.0,0.0,2.0,preciseAns,ux0,0.0,0.0)
#           def __init__(self,problem,spaceStep,timeStep)
#  in order for this method to stablize , timestep must <= 0.5*spacestep^2
# method_one=fd.forwardDifferentiation(problem2,0.01,timestep)
# method_one.numericalSolution(problem2)
# method_one.getError()
# print("forwardDifferentiation:")
# method_one.showMaxError()
# method_one.showMat(method_one.numericalAns,"numerical solution")
# method_one.showMat(method_one.preciseAns,"precise solution")
# method_one.showPicture(problem2)




spacesteps=[0.05,0.1,0.2,0.5]
error=[]
for spacestep in spacesteps:
	method_two=bd.backwardDifferentiation(problem2,spacestep,0.00001)
	method_two.numericalSolution(problem2)
	method_two.getError()
	print("backwardDifferentiation:")
	error.append(method_two.showMaxError())
	# method_two.showMat(method_two.numericalAns,"numerical solution")
	# method_two.showMat(method_two.preciseAns,"precise solution")
	# method_two.showPicture(problem2)
print("timesteps:"+str(spacesteps))
print("error:"+str(error))
print("lntimesteps:"+str(np.log(spacesteps)))
print("lnerror:"+str(np.log(error)))
x=np.log(spacesteps)
y=np.log(error)
plt.plot(x,y)
plt.show()
k=(y[-1]-y[0])/(x[-1]-x[0])
print("k="+str(k))

# method_three=ck.CrankNicolson(problem2,0.05,0.05)
# method_three.numericalSolution(problem2)
# method_three.getError()
# print("CrankNicolson")
# method_three.showMaxError()
# method_three.showMat(method_three.numericalAns,"numerical solution")
# method_three.showMat(method_three.preciseAns,"precise solution")
# method_three.showPicture(problem2)