import numpy as np
import matplotlib.pyplot as plt  
a = ord('A') + ord('S')
s = np.array([a, a + 50, a + 100, a + 150, a + 200])
tax = ((a % 5) + 5) / 100
s_at = s * (1 - tax)
ds = np.where(s < a + 100, s * 0.95, s * 0.90)
sw = np.tile(s, (3, 1)) * np.array([1, 1.02, 1.04]).reshape(3, 1)
print("Sales after tax:", s_at)
print("Discounted sales:", ds)
print("Sales for 3 weeks:", sw)
