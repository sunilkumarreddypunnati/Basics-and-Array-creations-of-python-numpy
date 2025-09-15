'''Problem 4: Zeros/Ones/Identity
Create zeros(r×c), ones(r×c), identity(n×n)
Input: r c n
Output: 3 lines, flattened
Sample Input: 2 3 3
Sample Output:
0 0 0 0 0 0
1 1 1 1 1 1
1 0 0 0 1 0 0 0 1'''
import numpy as np

r=int(input("enter no.of rows:"))
c=int(input("enter no.of colomns:"))
n=int(input("enter eye:"))

zero_arr=np.zeros((r,c),dtype=int)
ones_arr=np.ones((r,c),dtype=int)
eye_arr=np.eye((n), dtype=int)
print(*zero_arr.flatten())
print(*ones_arr.flatten())
print(*eye_arr.flatten())