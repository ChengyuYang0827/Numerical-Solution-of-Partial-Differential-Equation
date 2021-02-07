import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#problem1
# M = 1000
# N = [3,4,5,6,7,8,9,10,11]

# tao = 1/M
# h = []
# for item in N:
# 	h.append(1/item)

# # 关于h的截断误差 O(tao + h^2)
# errors_h = [8.47146344,5.36955155,3.23196454,2.34573721,1.67414082,1.31168414,1.01904954,0.83724296,0.68435128]

# print("Convergence Order about h:"+str(np.log(errors_h[0]/errors_h[-1])/np.log(h[0]/h[-1])))

# plt.plot(np.log(errors_h),np.log(h))
# plt.title("Convergence Order")
# plt.xlabel("ln_h")
# plt.ylabel("ln_error")
# plt.show()


N = 1000
M = [8,10,12,14,16,18,20,22,24,26]

h = 1/N
tao = []
for item in M:
	tao.append(1/item)

# 关于tao的截断误差
errors_tao = [15.85417129,13.22983537,11.08050174,10.11674849,9.25187011,8.4242567,7.66244544,6.97465569,6.54379523,6.14359815]

print("Convergence Order about Tao:"+str(np.log(errors_tao[0]/errors_tao[-1])/np.log(tao[0]/tao[-1])))
plt.plot(np.log(errors_tao),np.log(tao))
plt.title("Convergence Order")
plt.xlabel("ln_tao")
plt.ylabel("ln_error")
plt.show()

