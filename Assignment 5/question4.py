import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(-10, 10, 100)
sq = t ** 2               
sn = np.sin(t)           
ex = np.exp(t)            
lg = np.log(np.abs(t) + 1) 
plt.plot(t, sq, label="y = x^2")
plt.plot(t, sn, label="y = sin(x)")
plt.plot(t, ex, label="y = exp(x)")
plt.plot(t, lg, label="y = log(|x| + 1)")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Function Plots")
plt.legend()
plt.grid(True)
plt.show()
