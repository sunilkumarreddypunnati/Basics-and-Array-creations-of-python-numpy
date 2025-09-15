'''Problem 3: Linspace Array
n evenly spaced numbers from 0 to 1
Input: n
Output: space-separated (2 decimals)
Sample Input: 5
Sample Output: 0.00 0.25 0.50 0.75 1.00'''

import numpy as np
n=int(input("enter no.of linespaces:"))
array=(np.linspace(0,1,n))
print(*np.round(array,2))