# -*- coding: utf-8 -*-
"""
@author: Sreenivas.J
"""

# reconstruct matrix
from numpy import diag
#from numpy import dot
from numpy.linalg import inv
from numpy import array
from numpy.linalg import eig
# define matrix
A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
# calculate eigenvectors and eigenvalues
values, vectors = eig(A)
# create matrix from eigenvectors
Q = vectors
# create inverse of eigenvectors matrix
R = inv(Q)
# create diagonal matrix from eigenvalues
L = diag(values)
# reconstruct the original matrix
B = Q.dot(L).dot(R)
print(B) #You should be getting the original matrix back
