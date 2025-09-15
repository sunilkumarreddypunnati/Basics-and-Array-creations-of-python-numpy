'''Problem 5: Range Square
Create an array of integers from 1 to n and print their squares.
Input: integer n
Output: space-separated squares
Sample Input:
5
Sample Output:
1 4 9 16 25'''

import numpy as np
n=int(input("num:"))
array=np.arange(1,n+1)
squares=array**2
print(*squares)
