import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df= pd.read_csv(r"HeartAttack\Heart Attack Data Set.csv")
print(df.describe())
print(df.info())
print(df.isnull().sum())
print(df.head())
