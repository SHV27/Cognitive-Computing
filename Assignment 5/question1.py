import numpy as np
from matplotlib import pyplot as plt  
a = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')
s = np.sum(a)
r = np.sum(a, axis=1)
c = np.sum(a, axis=0)
print("Sum of all elements:", s)
print("Row-wise sum:", r)
print("Column-wise sum:", c)
