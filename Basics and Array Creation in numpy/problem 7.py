'''Problem 7: Diagonal Matrix
Create an n×n diagonal matrix with given elements.
Input: n (size)
Line2: n integers
Output: flattened matrix
Sample Input:
3
1 2 3
Sample Output:
1 0 0 0 2 0 0 0 3'''
import numpy as np
n=int(input("size:"))

elements=np.array(input().split(),int)
array=np.diag(elements)
print(*array.flatten())