'''Problem 8: Even Numbers Array
Generate an array of even numbers from 2 to n (inclusive).
Input: integer n
Output: space-separated array
Sample Input:
10
Sample Output:
2 4 6 8 10'''

import numpy as np
n=int(input("num:"))
arr=np.arange(2,n+1,2)
print(*arr)