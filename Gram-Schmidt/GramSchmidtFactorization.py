import numpy as np

def Transpose(X):
    T=[[0 for z in range(len(X[0]))] for j in range (len(X))]
    for i in range(len(X)):
        for j in range(len(X[0])):
            T[j][i] = X[i][j]
    return T

def dotProduct(a,b):    #dot product
    c=[0 for i in a]
    for i in range(len(a)):
        c[i] = a[i]*b[i]
    return sum(c)

def Orthogoanlize(A):
    coloumnsOfA = []
    ortho = []
    coloumnsOfA = ([[row[i] for row in A] for i in range(len(A[0]))])#taking columns
    for i in coloumnsOfA:
        vector = i
        listOfOrth = []
        for j in ortho:
            norm = dotProduct(j,j)  #norm of vectors
            if norm != 0:
                listOfOrth.append(([num*(dotProduct(j,i)/norm) for num in j]))
            else:
                listOfOrth.append([0 for num in j]) #since divison by zero
                #  not possible and norm will be zero of dependent column
        sumed = [0 for z in range(len(coloumnsOfA[0]))]
        for j in listOfOrth:
            for k in range(len(j)):
                sumed[k] += j[k]    #getting the error vectors
        for k in range(len(vector)):
            vector[k] -= sumed[k]
            if vector[k] < 0.00001 and vector[k] > 0:
                vector[k] = 0
        ortho.append(vector)
    return ortho

    
def normailze(A):
    a= Orthogoanlize(A)
    Q = []
    for i in range(len(a)):
        norm = (sum([j**2 for j in a[i]])**0.5)  #norm = square each
        # element of column sum it and then root it.
        if norm != 0:
            Q.append([j/norm for j in a[i]]) #j/norm
        else:
            Q.append(a[i].copy())
    return Q

def upperR(A):
    R=[]
    coloumnsOfA = ([[row[i] for row in A] for i in range(len(A[0]))])
    Q = normailze(A)
    
    matrix = []
    for i in range(len(coloumnsOfA)):
        for j in range(len(coloumnsOfA)):
            R.append(dotProduct(coloumnsOfA[i],Q[j]))   #R= dot product of
            # columns of A and columns of Q
        matrix.append(R)
        R=[]
    
    return Transpose(matrix)
        

def qr(A):
    '''
    This function takes a matrix represented as 2D list as the parameter,
    and returns its QR factors.
    
    syntax: return q,r
    where q and r are 2D lists.
    Do not round off any values in your calculation

    WRITE YOUR CODE BELOW THE COMMENTS
    '''
    
    return Transpose(normailze(A)),upperR(A)
        




    


