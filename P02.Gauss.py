import numpy as np

A = np.array(([1,1,-1,7],[1,-1,2,3],[2,1,1,9]),dtype=float)

print(A)

#1ER PIVOTE
A[0]=A[0]/A[0,0] #Primer renglón entre 1er elemento
A[1]=A[1]-A[1,0]*A[0]
A[2]=A[2]-A[2,0]*A[0]

print('================')
print(A)

#2DO PIVOTE
A[2]=A[2]/A[2,1]
A[1]=A[1]-A[1,1]*A[2]
A[0]=A[0]-A[0,1]*A[2]

print("=============")
print(A)

#3ER PIVOTE
A[1]=A[1]/A[1,2]
A[0]=A[0]-A[0,2]*A[1]
A[2]=A[2]-A[2,2]*A[1]

print("=============")
print(A)

#A2 = np.array(([A[0]],[A[2]],[A[1]]))
#print(A2)