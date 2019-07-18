"""
Interview question: Write a function that performes an inplace transpose of a square matrix
Category: Programming
Description: This function takes a matrix in a NxN numpy array format 
and returns it's transpose inplace.
"""
import numpy as np
A=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
A=np.asarray(A)
N=A.shape[0]
AT=[[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16]]
AT=np.asarray(AT)

def transpose_inplace(A):
    c=0
    ct=0
    for r in range(N):
        while (c+ct)<N:
            e=A[r][c+ct]
            A[r][c+ct]=A[c+ct][r]
            A[c+ct][r]=e
            c+=1
        ct+=1
        c=0
    return A
	
	
#################################
A=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def transposeMatrix(A):
	for row in range(len(A)):
		for col in range(row, len(A)):
			A[row][col], A[col][row] = A[col][row], A[row][col]
	return A

