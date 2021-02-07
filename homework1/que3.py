import numpy as np
import math
import sys
# f(x,y) = cos(x+y)+cos(x-y)
# (0,pi)*(0,pi/2)
# u(x,0) = cos x , u(x,pi/2) = 0
# u(0,y) = cos y , u(pi,y) = - cos y


print("Input the number of pieces you want each interval to be broken into:")
num=int(input())
h1=(math.pi)/num
h2=(math.pi/2)/num
n=num-1

a1=a3=1.0/(h1*h1)
a2=a4=1.0/(h2*h2)
a0=a1+a2+a3+a4

x=[]
y=[]
uxy0=[]
uxy1=[]
ux0y=[]
ux1y=[]

for i in range(0,num+1):
	x.append(0.0+h1*i)
	y.append(0.0+h2*i)
	uxy0.append(math.cos(x[i]))
	uxy1.append(0.0)
	ux0y.append(math.cos(y[i]))
	ux1y.append(-math.cos(y[i]))


# GET A
B=a0*np.eye(n)-a1*np.eye(n,k=1)-a3*np.eye(n,k=-1)
A=np.zeros(((n*n,n*n)))
for i in range(0,n):
	A[i*n:i*n+n,i*n:i*n+n]=B
	if i==0:
		A[n:2*n,0:n]=(-a4)*np.eye(n)
	elif i==n-1:
		A[(n-2)*n:(n-1)*n,(n-1)*n:n*n]=(-a2)*np.eye(n)
	else:
		A[(i-1)*n:i*n,i*n:i*n+n]=(-a2)*np.eye(n)
		A[(i+1)*n:(i+2)*n,i*n:i*n+n]=(-a4)*np.eye(n)
print("A"+str(A)+"\n")


# GET F
f=np.zeros((n*n,1))

for index in range(0,n*n):
	tox=index%n+1
	toy=int(index/n)+1
	f[index]=math.cos(x[tox]+y[toy])+math.cos(x[tox]-y[toy])
	if(toy-1==0):
		f[index]=f[index]+uxy0[tox]*a4
	if(toy+1==num):
		f[index]=f[index]+uxy1[tox]*a2
	if(tox-1==0):
		f[index]=f[index]+ux0y[toy]*a3
	if(tox+1==num):
		f[index]=f[index]+ux1y[toy]*a1

print("f:\n"+str(f)+"\n")



# U=inversed(A)*F
ans=np.linalg.inv(A)*np.matrix(f)
print("ans:\n"+str(ans)+"\n")

# GET precise values
def pU(x,y):
	return math.cos(x)*math.cos(y)
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
print("\nerror:")
for i in range(0,len(errors)):
	print(str(errors[i]))

# GET relative errors
relativeError=[]
for i in range(0,len(errors)):
	if preciseU[i]!=0:
		relativeError.append(errors[i]/abs(preciseU[i]))
	else:
		relativeError.append(errors[i])
# print("\nrelative error:")
# for i in range(0,len(relativeError)):
# 	print(str(relativeError[i]))

maxError = -1
for error in errors:
	if error>maxError:
		maxError=error
print("\nmaxError = "+str(maxError))


