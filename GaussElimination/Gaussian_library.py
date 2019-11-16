import numpy 
import scipy.linalg 
import time
import random
import matplotlib.pyplot as plt

def GaussTime(a,b):
    numpy.linalg.solve(a, b)


def LUTime(a):
    return scipy.linalg.lu_factor(a)


LU_time =[]
gauss_time=[]

Nums = [3,10,50,100,200]
for N in Nums:
    start_time = time.time()
    equations = [[random.randint(-50, 50) for i in range(N)] for i in range(N)]
    b= [[random.randint(-50, 50) for i in range(N)] for i in range(N)]
    for i in b:
        GaussTime(equations,i)
    end_time = time.time()
    gauss_time.append(end_time-start_time)


for N in Nums:
    start_time = time.time()
    equations = [[random.randint(-50, 50) for i in range(N)] for i in range(N)]
    b = [[random.randint(-50, 50) for i in range(N)] for i in range(N)]
    LU = LUTime(equations)
    for i in b:
        scipy.linalg.lu_solve(LU, i)
    end_time = time.time()
    LU_time.append(end_time - start_time)


print(LU_time)
print(gauss_time)

plt.plot(Nums, LU_time, label = 'LU time', marker = 'o')
plt.plot(Nums, gauss_time, label = 'Gauss time', marker = 'o')
plt.grid()
plt.xlabel('number of variables');
plt.ylabel('time taken');
plt.legend()
plt.show()
