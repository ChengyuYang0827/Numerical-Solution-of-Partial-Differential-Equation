import numpy
import math
# f(x,y) = 0
# (1,2) * (0,1)


def u(x,y):
	return math.log(math.pow(x,2)+math.pow(y,2))


x=[]
y=[]
u_x_0=[]
u_x_1=[]
u_1_y=[]
u_2_y=[]


h=0.25
n=int(1.0/h)

for i in range(0,n):
	x.append(1.0+h*i)
	y.append(0.0+h*i)
	u_x_0.append(2*math.log(x[i]))
	u_x_1.append(math.log(math.pow(x[i],2)+1.0))
	u_1_y.append(math.log(math.pow(y[i],2)+1.0))
	u_2_y.append(math.log(math.pow(y[i],2)+4.0))




