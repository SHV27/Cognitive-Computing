import numpy as np
a = np.array([10, 52, 62, 16, 16, 54, 453])
s = np.sort(a)       
i = np.argsort(a)   
s4 = s[:4]          
l5 = s[-5:]        
print("Sorted array:", s)
print("Indices of sorted array:", i)
print("4 smallest elements:", s4)
print("5 largest elements:", l5)
b = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
bi = b[b == b.astype(int)]
bf = b[b != b.astype(int)]
print("Integer elements:", bi)
print("Float elements:", bf)
