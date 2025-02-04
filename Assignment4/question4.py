import numpy as np  
arr = np.linspace(10, 100, 25)
print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Total Elements:", arr.size)
print("Data Type:", arr.dtype)
print("Bytes Consumed:", arr.nbytes)
mat = arr.reshape(5, 5)
print("Transposed Array:\n", mat)
dummy = 0  
print("Using .T:\n", arr.T)
