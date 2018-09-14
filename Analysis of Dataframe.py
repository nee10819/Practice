# Data Preparation

# importing libraries
import numpy as np
import pandas as pd

df = pd.DataFrame({'A':[1,2,np.nan],
                   'B':[3,np.nan,4],
                   'C':[5,6,7]})
# print(df)
df.describe()
df.info()

##############################################################################################
# Handling Missing values
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


###############################################################################################
# Groupby
data = {'Company':['GOOG','GOOG','ORCL','ORCL','ACN','ACN'],
        'Person':['ABC','DEF','GHI','JKL','MNO','PQR'],
        'Sales':[500,600,200,300,700,800]}

df = pd.DataFrame(data)
df.info()
df.describe()

df.groupby('Company')
by_comp = df.groupby('Company')
by_comp.mean()
by_comp.count()

by_comp = df.groupby('Company').mean()
by_comp = df.groupby('Company').sum()

by_comp = df.groupby('Company')
by_comp.describe()
by_comp.describe().transpose()
by_comp.describe().transpose()['GOOG']

###############################################################################################
# Concatenation of Dataframes
df1 = pd.DataFrame({'A':['A1','A2','A3','A4'],
                    'B':['B1','B2','B3','B4'],
                    'C':['C1','C2','C3','C4'],
                    'D':['D1','D2','D3','D4']},
                    index = [0,1,2,3])

df2 = pd.DataFrame({'A':['A5','A6','A7','A8'],
                    'B':['B5','B6','B7','B8'],
                    'C':['C5','C6','C7','C8'],
                    'D':['D5','D6','D7','D8']},
                    index = [4,5,6,7])

df3 = pd.DataFrame({'A':['A9','A10','A11','A12'],
                    'B':['B9','B10','B11','B12'],
                    'C':['C9','C10','C11','C12'],
                    'D':['D9','D10','D11','D12']},
                    index = [8,9,10,11])

# Concat along rows
pd.concat([df1,df2,df3])

# Concat along columns
pd.concat([df1,df2,df3],axis=1)

# Merging of dataframes using key columns
left = pd.DataFrame({'key':['k0','k1','k2','k3'],
        'b':['b0','b1','b2','b3'],
        'c':['c0','c1','c2','c3']})

right = pd.DataFrame({'key':['k0','k1','k2','k3'],
        'd':['d0','d1','d2','d3'],
        'e':['e0','e1','e2','e3']})

# merge like sql
pd.merge(left, right, how ='inner', on='key')

# Joining like SQL using index only
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])

left.join(right)
left.join(right, how='outer')

############################################################################################
# Operations on dataframes
df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,666,444],
                   'col3':['abc','def','ghi','xyz']})

df.head()
df.tail()

# Information on unique values
df['col2'].unique()
df['col2'].nunique()

df['col2'].value_counts()

# Selection of Data
newdf = df[(df['col1'] > 1) & (df['col2'] < 666)]
newdf2 = df[(df['col1'] > 1) | (df['col2'] < 666)]

# Functions
def square(x):
    return x*x

square(10)

# Applying functions
df['col1'].apply(square)
df['col3'].apply(len)
df['col1'].sum()

# Permanently removing a column
del df['col1']

# Get columns and index names
df.columns
df.index

# Finding null values
df.isnull()
df.isnull().sum()


data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
df

df.pivot_table(values='D', index=['A','B'], columns='C')





































