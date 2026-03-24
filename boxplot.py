import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('DATASET.xlsx')


df['population'] = pd.to_numeric(df['population'], errors='coerce')


df = df.dropna(subset=['population'])


plt.figure()
plt.boxplot(df['population'])

plt.title('Boxplot of Population')
plt.ylabel('Population')

plt.show()