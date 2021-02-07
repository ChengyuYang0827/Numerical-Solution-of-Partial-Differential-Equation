import numpy as np
import math
import matplotlib.pyplot
# f(x,y) = 0
# (1,2)*(0,1)

def getMaxError(stepLength):
	# print("Input step length for this time:")
	# stepLength=input()
	# if len(stepLength)<1:
	# 	stepLength="0.25"
	stepLength=float(stepLength)
	num=int(1.0/stepLength)
	n=num-1

	a1=a3=1.0
	a2=a4=1.0
	a0=a1+a2+a3+a4

	x=[]
	y=[]
	ux0=[]
	ux1=[]
	u1y=[]
	u2y=[]

	for i in range(0,num+1):
		x.append(1.0+stepLength*i)
		y.append(0.0+stepLength*i)
		ux0.append(2*math.log(x[i]))
		ux1.append(math.log(math.pow(x[i],2)+1.0))
		u1y.append(math.log(math.pow(y[i],2)+1.0))
		u2y.append(math.log(math.pow(y[i],2)+4.0))


	# GET A
	ide=np.identity(num-1)
	minusOneMat=ide*(-1)
	zeroMat=np.zeros((num-1,num-1))
	B=a0*np.eye(num-1)-a1*np.eye(num-1,k=1)-a3*np.eye(num-1,k=-1)
	A=np.zeros(((num-1)*(num-1),(num-1)*(num-1)))
	for i in range(0,n):
		A[i*n:i*n+n,i*n:i*n+n]=B
		if i==0:
			A[n:2*n,0:n]=(-a4)*np.eye(n)
		elif i==n-1:
			A[(n-2)*n:(n-1)*n,(n-1)*n:n*n]=(-a2)*np.eye(n)
		else:
			A[(i-1)*n:i*n,i*n:i*n+n]=(-a2)*np.eye(n)
			A[(i+1)*n:(i+2)*n,i*n:i*n+n]=(-a4)*np.eye(n)
	# print("A"+str(A)+"\n")


	# GET F
	f=np.zeros((n*n,1))
	for index in range(0,n*n):
		tox=index%n+1
		toy=int(index/n)+1
		if(toy-1==0):
			f[index]=f[index]+ux0[tox]
		if(toy+1==num):
			f[index]=f[index]+ux1[tox]
		if(tox-1==0):
			f[index]=f[index]+u1y[toy]
		if(tox+1==num):
			f[index]=f[index]+u2y[toy]

	# print("f:\n"+str(f)+"\n")



	# U=inversed(A)*F
	ans=np.matrix(A).I*f
	# print("ans:\n"+str(ans)+"\n")

	# GET precise values
	def pU(x,y):
		return math.log(math.pow(x,2)+math.pow(y,2))
	preciseU=[]
	for j in range(0,n):
		for i in range(0,n):
			preciseU.append(pU(x[i+1],y[j+1]))
	# print("preciseU:")
	# for i in range(0,len(preciseU)):
	# 	print(preciseU[i])

	# GET errors
	errors=[]
	for i in range(0,(num-1)*(num-1)):
		errors.append(abs(float(preciseU[i])-float(ans[i])))
	# print("\nerror:")
	# for i in range(0,len(errors)):
	# 	print(str(errors[i]))

	# GET relative errors
	relativeError=[]
	for i in range(0,len(errors)):
		relativeError.append(errors[i]/abs(preciseU[i]))
	# print("\nrelative error:")
	# for i in range(0,len(relativeError)):
	# 	print(str(relativeError[i]))

	maxError=-1;
	for error in errors:
		if error>maxError:
			maxError=error
	# print("\nmaxError = "+ str(maxError))

	return maxError


h=[0.025,0.05,0.1,0.2,0.25,0.5]
maxErrors=[]
for item in h:
	maxErrors.append(getMaxError(item))
print("\nmaxErrors:"+str(maxErrors))


p=[]
for i in range(1,len(h)):
	p.append(math.log(maxErrors[i]/maxErrors[i-1])/math.log(h[i]/h[i-1]))
print("\np:"+str(p))

lnx=[]
lny=[]
for item in h:
	lnx.append(math.log(item))
	lny.append(math.log(getMaxError(item)))
matplotlib.pyplot.plot(lnx,lny)
matplotlib.pyplot.show()