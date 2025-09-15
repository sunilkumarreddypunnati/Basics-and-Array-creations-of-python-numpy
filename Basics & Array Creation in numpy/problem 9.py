'''Problem 9: Repeat Elements
Create an array where each element of the list is repeated k times.
Input:
Line1: integers
Line2: integer k
Output: space-separated repeated values
Sample Input:
1 2 3
3
Sample Output:
1 1 1 2 2 2 3 3 3'''

import numpy as np

a=np.array([1,2,3])
k=int(input("value:"))
repeat=np.repeat(a,k)
print(repeat)