'''Problem 6: Random Integers
Create an array of size n with 
random integers between 1 and 100.
Input: integer n
Output: space-separated array
Sample Input:
5
Sample Output:
12 87 45 23 9'''
import numpy as np
n=int(input("num:"))
b=np.random.randint(1,100,n)
print(b)