import random
import time
import numpy as np
import matplotlib.pyplot as plt

##y = []
##x = []
##for i in range(1,250):
##    A =  np.random.rand(i,i)
##    start_time = time.time()
##    np.linalg.qr(A)
##    stime = time.time()-start_time
##    x.append(i)
##    y.append(stime)

Rows = [i**2 for i in range(2,50)]
Time = []
for i in Rows:
    matrix = np.random.rand(i,i)
    start = time.time()
    np.linalg.qr(matrix)
    Time.append(time.time() - start)

n = [i**2 for i in range(2,50)]
y = []
for i in n:
    y.append(0.0000000001871*(i**3))
    

plt.plot(Rows,Time, label = 'library QR')
plt.plot(n,y, label = 'y = 0.0000000001871 (n^3)' , color = 'green')
plt.grid()
plt.xlabel('n by n');
plt.ylabel('time taken in seconds');
plt.legend()
plt.show()



    

