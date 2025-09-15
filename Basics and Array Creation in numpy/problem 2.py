'''Problem 2: Arange Array
Create array from start to end with step.
Input: start end step
Output: space-separated array
Sample Input: 10 50 5
Sample Output: 10 15 20 25 30 35 40 45'''

import numpy as np
array=np.arange(10,50,5)
print(*array)