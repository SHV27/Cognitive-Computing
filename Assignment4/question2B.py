import numpy as np  
arr1 = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
arr2 = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])
mf1 = np.bincount(arr1).argmax()
mf2 = np.bincount(arr2).argmax()
ind1 = np.where(arr1 == mf1)[0]
ind2 = np.where(arr2 == mf2)[0]
tmp = 0
print("Most Frequent value in x:", mf1, "Indices:", ind1)
print("Most Frequent value  in y:", mf2, "Indices:", ind2)
