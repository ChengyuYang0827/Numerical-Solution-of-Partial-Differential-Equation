import forwardDifferentiation as fd
import backwardDifferentiation as bd
import CrankNicolson as ck
import math
import problem as pb


def preciseAns(x,t):
	return 2*math.pow(math.e,-t*math.pow(math.pi,2)/4.0)*math.sin(2*math.pi*x)

def ux0(x):
	return 2*math.sin(2*math.pi*x)

problem1=pb.problem(1.0/16,0.0, 0.0,1.0,0.0,1.0,preciseAns,ux0,0.0,0.0)
#           def __init__(self,problem,spaceStep,timeStep)



method_one=fd.forwardDifferentiation(problem1,0.2,0.04)
method_one.numericalSolution(problem1)
method_one.getError()
print("forwardDifferentiation:")
method_one.showMaxError()
method_one.showMat(method_one.numericalAns,"numerical solution")
method_one.showMat(method_one.preciseAns,"precise solution")
method_one.showPicture(problem1)




method_two = bd.backwardDifferentiation(problem1,0.2,0.04)
method_two.numericalSolution(problem1)
method_two.getError()
print("backwardDifferentiation:")
method_two.showMaxError()
method_two.showMat(method_two.numericalAns,"numerical solution")
method_two.showMat(method_two.preciseAns,"precise solution")
method_two.showPicture(problem1)


method_three = ck.CrankNicolson(problem1,0.2,0.2)
method_three.numericalSolution(problem1)
method_three.getError()
print("CrankNicolson:")
method_three.showMaxError()
method_three.showMat(method_three.numericalAns,"numerical solution")
method_three.showMat(method_three.preciseAns,"precise solution")
method_three.showPicture(problem1)
