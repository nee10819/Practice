# Data Preparation
# Data Preprocessing
# Handling Missing values

# importing libraries
import numpy as np
import pandas as pd

df = pd.DataFrame({'A':[1,2,np.nan],
                   'B':[3,np.nan,4],
                   'C':[5,6,7]})
# print(df)
df.describe()
df.info()

# Drops all rows having nulls
df.dropna()

# Drops all columns having nulls
df.dropna(axis=1)

# 2 or more nulls is allowed in dataframe
df.dropna(thresh=2)

# 3 or more nulls is allowed in dataframe
df.dropna(thresh=3)

# Fillup all missing values
df.fillna(value = 'MISSING')

# Filling up missing values with mean of that column
df['A'].fillna(value=df['A'].mean())