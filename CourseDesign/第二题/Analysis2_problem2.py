import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# M = 1000
# N = [3,4,5,6,7,8,9,10,11]

# tao = 1/M
# h = []
# for item in N:
# 	h.append(1/item)

# # 关于h的截断误差 O(tao + h^2)
# errors_h = [17.708872,9.78577793,6.23461638,4.33550025,3.20042079,2.46771353,1.9671828,1.61005659,1.34630575]

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
errors_tao = [36.26235871,28.16726197,22.96543281,19.29241051,16.54234605,14.60932799,13.09346247,11.83871656,10.77905392,9.87729745]

print("Convergence Order about Tao:"+str(np.log(errors_tao[0]/errors_tao[-1])/np.log(tao[0]/tao[-1])))
plt.plot(np.log(errors_tao),np.log(tao))
plt.title("Convergence Order")
plt.xlabel("ln_tao")
plt.ylabel("ln_error")
plt.show()