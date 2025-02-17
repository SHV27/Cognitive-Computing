import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

s = int(input())
np.random.seed(s)
r = np.random.randn(50)
df = pd.DataFrame({'val': r})
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.lineplot(data=df.cumsum(), color="b")
plt.title("Cumulative Sum")
plt.grid()
plt.subplot(1, 2, 2)
sns.scatterplot(x=range(50), y=df['val'], color="r")
plt.title("Scatter Plot with Noise")
plt.grid()
plt.tight_layout()
plt.show()
