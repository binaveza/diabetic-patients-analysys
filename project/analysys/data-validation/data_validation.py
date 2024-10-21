import pandas as pd
import matplotlib.pyplot as plt
import os

print("Текущая рабочая директория:", os.getcwd())
# Загружаем данные из CSV файла
df = pd.read_csv('data/daiabet.csv', sep=',', header=0)

# Проверка загруженных данных
print(df.head())

# График распределения данных
df.hist(bins=30, figsize=(15, 10), edgecolor='black', color='#A43DD4')
plt.suptitle('График распределения данных', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
#plt.show()
plt.savefig('data_distribution_graph.png')


