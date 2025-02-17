import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
d = {'Subjects': ['Math', 'Physics', 'Chemistry', 'Biology', 'English'],
     'Scores': [85, 90, 78, 88, 76]}
df = pd.DataFrame(d)
plt.figure(figsize=(8, 5))
a = sns.barplot(x='Subjects', y='Scores', data=df, palette='viridis')


for b in a.patches:
    m = b.get_x() + b.get_width() / 2  
    h = b.get_height()                
    plt.text(m, h, f'{int(h)}', ha='center')

plt.title('Subject Scores')
plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.grid(True)
plt.show()
