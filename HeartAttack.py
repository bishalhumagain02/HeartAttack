import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df= pd.read_csv(r"HeartAttack\Heart Attack Data Set.csv")
print(df.describe())
print(df.info())
print(df.isnull().sum())
print(df.head())

sns.countplot(x='target', data=df)
plt.title('count of target variable')

plt.savefig('HeartAttack/count_of_target_variable.png')
plt.close()

sns.boxplot(x='target', y='age', data=df)
plt.title('boxplot of age by target')
# plt.show()
plt.savefig('HeartAttack/boxplot_of_age_by_target.png')
plt.close()

sns.countplot(x='sex', hue='target', data=df)
plt.title('count of sex by target')
# plt.show()
plt.savefig('HeartAttack/count_of_sex_by_target.png')
plt.close()

plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
# plt.show()
plt.savefig('HeartAttack/correlation_heatmap.png')
plt.close()

