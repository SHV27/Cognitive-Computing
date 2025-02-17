import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
factor = float(input())  
values = np.linspace(-10, 10, 400)
data = pd.DataFrame({
    'values': values,
    'quadratic': factor * values**2,
    'sine': factor * np.sin(values)
})

sns.set_style("whitegrid")
plt.figure(figsize=(8, 5))
sns.lineplot(data=data, x='values', y='quadratic', color="r", linestyle="-", label="y = factor * x²")
sns.lineplot(data=data, x='values', y='sine', color="b", linestyle="--", label="y = factor * sin(x)")
plt.legend()
plt.title('Graph of Functions')
plt.show()
