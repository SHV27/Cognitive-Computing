import numpy as np  
mat = np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 15, 20, 35]])
avg = np.mean(mat)      
med = np.median(mat)    
max_val = np.max(mat)   
min_val = np.min(mat)   
uniq = np.unique(mat)  
print("Mean  ", avg)
print("Median  ", med)
print("Max  ", max_val)
print("Min  ", min_val)
print("Unique Elements  ", uniq)
reshaped = mat.reshape(4, 3)
print("Reshaped Array:", reshaped)
resized = np.resize(mat, (2, 3))
print("Resized Array:", resized)
