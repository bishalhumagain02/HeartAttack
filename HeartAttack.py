import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df= pd.read_csv(r"HeartAttack\Heart Attack Data Set.csv")
# print(df.describe())
# print(df.info())
# print(df.isnull().sum())
# print(df.head())

# sns.countplot(x='target', data=df)
# plt.title('count of target variable')
# plt.show()

sns.boxplot(x='target', y='age', data=df)
plt.show()