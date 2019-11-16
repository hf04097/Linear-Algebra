import time
import random
import numpy
import matplotlib.pyplot as plt

def GaussianElimination(A):
    start_time = time.time()
    A.sort(reverse= True)
    for i in range(len(A)):
        if A[i][i] != 0:
            A[i] = [num/A[i][i] for num in A[i]]
        for j in range(i+1,len(A)):
           temp = [A[j][i] * num for num in A[i]]
           A[j]= sub(A[j],temp)
    end_time = time.time()
    return end_time - start_time

def sub(a,b):   
    ans =[]
    for i in range(len(a)):
        ans.append(a[i]-b[i])
    return ans

def usingNumpy(a,b):
    start_time = time.time()
    numpy.linalg.solve(equations,b)
    end_time = time.time()
    return end_time - start_time
