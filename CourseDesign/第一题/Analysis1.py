import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# #problem 1
# M = [3,4,5,6,7,8,9,10,11,12]
# N = 500

# h1 = []
# for item in M:
# 	h1.append(np.pi/item)


# errors = [0.06732562,0.04334654,0.0262749,0.0191423,0.01369274,0.010744,0.00835547,0.00686979,0.00561833,0.00476874]

# print("Convergence Order:"+str(np.log(errors[0]/errors[-1])/np.log(h1[0]/h1[-1])))

# plt.plot(np.log(errors),np.log(h1))
# plt.title("Convergence Order")
# plt.xlabel("ln_h")
# plt.ylabel("ln_error")
# plt.show()


#problem 2
M = [3,4,5,6,7,8,9,10,11,12]
N = 500

h1 = []
for item in M:
	h1.append(np.pi/item)

errors = [0.10779185,0.06958135,0.04222973,0.03078633,0.02203101,0.01729085,0.01344944,0.01105918,0.00904552,0.00767803]

print("Convergence Order:"+str(np.log(errors[0]/errors[-1])/np.log(h1[0]/h1[-1])))


plt.plot(np.log(errors),np.log(h1))
plt.title("Convergence Order")
plt.xlabel("ln_h")
plt.ylabel("ln_error")
plt.show()