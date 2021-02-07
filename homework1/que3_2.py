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
ux0=[]
ux2=[]
u0y=[]
u1y=[]

for i in range(0,num1+1):
	x.append(0.0+stepLength*i)
	ux0.append(math.pow(x[i],2))
	ux2.append(math.pow(x[i]-2,2))
for j in range(0,num2+1):
	y.append(0.0+stepLength*i)
	u0y.append(math.pow(y[i],2))
	u1y.append(math.pow(y[i]-1,2))

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
print("A"+str(A)+"\n")


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

print("f:\n"+str(f)+"\n")



# U=inversed(A)*F
ans=np.matrix(A).I*f
print("ans:\n"+str(ans)+"\n")

# GET precise values
def pU(x,y):
	return math.log(math.pow(x,2)+math.pow(y,2))
preciseU=[]
for j in range(0,n):
	for i in range(0,n):
		preciseU.append(pU(x[i+1],y[j+1]))
print("preciseU:")
for i in range(0,len(preciseU)):
	print(preciseU[i])

# GET errors
error=[]
for i in range(0,(num-1)*(num-1)):
	error.append(abs(float(preciseU[i])-float(ans[i])))
print("\nerror:")
for i in range(0,len(error)):
	print(str(error[i]))

# GET relative errors
relativeError=[]
for i in range(0,len(error)):
	relativeError.append(error[i]/abs(preciseU[i]))
print("\nrelative error:")
for i in range(0,len(relativeError)):
	print(str(relativeError[i]))


