'''Problem 10: Reshape Sequential
Create an array of numbers from 1 to r×c and reshape into matrix r×c.
Input: r c
Output: row-wise matrix
Sample Input:
2 3
Sample Output:
1 2 3
4 5 6'''
import numpy as np
r=int(input("rows:"))
c=int(input("columns:"))
arr=np.arange(1,r*c +1).reshape(r,c)
for row in arr:
    print(*row)