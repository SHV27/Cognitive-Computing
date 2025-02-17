import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
d = pd.read_csv("https://raw.githubusercontent.com/AnjulaMehto/MCA/main/company_sales_data.csv")
plt.plot(d['month_number'], d['total_profit'])
plt.title('Total Profit Over Months')
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.grid(True)
plt.show()
d.plot(x='month_number', y=d.columns[1:], kind='line')
plt.title('Product Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
d.plot(kind='bar', figsize=(10, 6))
plt.title('All Features Data')
plt.grid(True)
plt.show()
