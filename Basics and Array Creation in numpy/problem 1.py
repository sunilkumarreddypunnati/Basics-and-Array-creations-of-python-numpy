'''Problem 1: Multiply List
Multiply all elements of a list by n.
Input:
Line1: integers
Line2: integer n
Output: space-separated multiplied values
Sample Input:
5 10 15 20
3
Sample Output:
15 30 45 60
'''
import numpy as np
array=np.array([15,20,25,30])
result=array*3
print(*result)
