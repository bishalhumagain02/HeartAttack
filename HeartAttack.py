import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df= pd.read_csv(r"C:\Users\humag\OneDrive\Desktop\HeartAttackAnalysis\Heart Attack Data Set.csv")
print(df.describe())
print(df.info())
