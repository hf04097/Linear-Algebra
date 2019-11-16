import numpy as np
from qrFactorization import *


#within what range the answer is acceptable.
#If y is the correct answer, then y ± ERROR is acceptable
ERROR = 0.5

matrices = [[[1,2],[3,4]],
            [[12, -51, 4], [6, 167, -68], [-4, 24, -41]],
            [[0.15797 , 0.71033 , 0.13588 ,-0.47781 , 0.43762],
             [-0.77366 , 0.69873 , 0.35560 ,-0.77672, -0.02941],
             [ 0.57911, -0.84310 , 0.76622, -0.84151 ,-0.77572],
             [-0.87032 , 0.96510 , 0.68374 , 0.79453 , 0.66207],
             [ 0.25023 ,-0.93697 , 0.86126 , 0.87264, -0.21894]],
            [[0,0,0,0,0],[1,0,1,0,0],[1,0,0,1,1],[1,0,0,0,0],[0,1,1,0,0]],
            [[1,0],[0,1]],
            [[1,0],[0,0]]]

rect_independent_col_matrices = [[[1,2],[2,3],[3,4]]]

rect_dependent_col_matrices = [[[1,2,3],[2,4,6]],
                          [[1,2],[2,4],[3,6]]]

def multiplyMatrices(a, b):
    zip_b = zip(*b)
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]

# The following test cases only work for square matrices defined above
def test_determinant():
    for matrix in matrices:
        det_0 = np.linalg.det(np.array(matrix)) #determinant of original mat0
        q,r = qr(matrix)      
        matrix_1 = multiplyMatrices(q,r) #multiple QR factors to obtain mat1
        det_1 = np.linalg.det(np.array(matrix_1)) #determinant of mat1
        det_1_range = (det_1-ERROR,det_1+ERROR) #put det(mat1) in range
        assert det_0 >= det_1_range[0]  and det_0 <= det_1_range[1]

# The following test cases only work for square matrices defined above
def test_trace():
    for matrix in matrices + rect_independent_col_matrices:
        trace_0 = np.array(matrix).diagonal().sum()
        q,r = qr(matrix)      
        matrix_1 = multiplyMatrices(q,r)
        trace_1 = np.array(matrix_1).diagonal().sum()
        trace_1_range = (trace_1-ERROR,trace_1+ERROR)
        print(matrix)
        assert trace_0 >= trace_1_range[0]  and trace_0 <= trace_1_range[1]

def test_identity():
    for matrix in matrices:
        q,r = qr(matrix)
        m = len(matrix)
        trans_q = np.array(q).transpose()
        #Q * Q^T should be m x m
        assert np.allclose(np.array(multiplyMatrices(trans_q,q)),np.eye(m),1e-5,1e-5)

def test_dotProduct():
    for matrix in rect_dependent_col_matrices + matrices + rect_independent_col_matrices:
        q,r = qr(matrix)
        q = np.array(q)
        #columns of q are orthonormal, dot product = 0
        n = len(q[0])
        for i in range(n):
            for j in range(i+1,n):
                assert round(np.dot(q[:,i],q[:,j]),1) == 0
        
def test_magnitude():
    for matrix in rect_dependent_col_matrices + matrices + rect_independent_col_matrices:
        q,r = qr(matrix)
        q = np.array(q)
        #columns of q are orthonormal, magnitude = 1
        n = len(q[0])
        for i in range(n):
            assert round(np.linalg.norm(q[:,i]),1) == 1 


test_determinant()
test_trace()
#test_identity()
#test_dotProduct()
#test_magnitude()
