# Exploratory Data Analysis (EDA)

# Importing libraries
import pandas as pd
import numpy as np
# Below variable assignment is for an issue in pandas_datareader library
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data, wb
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Timeframe for which stock data is analyzed
start = datetime.datetime(2009, 1, 1)
end = datetime.datetime(2018, 1, 1)

# Fetching data from Web using pandas_datareader
# Oracle
ORCL = data.DataReader("ORCL", 'morningstar', start, end)
ORCL_New = ORCL.reset_index(level=0)
# Microsoft
MSFT = data.DataReader("MSFT", 'morningstar', start, end)
MSFT_New = MSFT.reset_index(level=0)
# IBM = data.DataReader("IBM", 'morningstar', start, end)
# HPE = data.DataReader("HPE", 'morningstar', start, end)
# Accenture
ACN = data.DataReader("ACN", 'morningstar', start, end)
ACN_New = ACN.reset_index(level=0)
# SAP
SAP = data.DataReader("SAP", 'morningstar', start, end)
SAP_New = SAP.reset_index(level=0)
# ADBE = data.DataReader("ADBE", 'morningstar', start, end)
# CRM = data.DataReader("CRM", 'morningstar', start, end)

# Minimum and Maximum Closing Stock price
ACN[ACN['Close'] == ACN['Close'].min()]
ACN[ACN['Close'] == ACN['Close'].max()]
MSFT[MSFT['Close'] == MSFT['Close'].min()]
MSFT[MSFT['Close'] == MSFT['Close'].max()]
ORCL[ORCL['Close'] == ORCL['Close'].min()]
ORCL[ORCL['Close'] == ORCL['Close'].max()]
SAP[SAP['Close'] == SAP['Close'].min()]
SAP[SAP['Close'] == SAP['Close'].max()]

# list of tickers to be assigned as keys
tickers = ['ACN', 'MSFT', 'ORCL', 'SAP']

# Concat dataframes
it_stocks = pd.concat([ACN_New, MSFT_New, ORCL_New, SAP_New], axis=1, keys = tickers)

# Assign column names to tickers and it's different attributes
it_stocks.columns.names = ['IT Ticker', 'Stock Information']
it_stocks.info()
it_stocks.describe()

# EDA
# Return the maximum and minimum Stock price of all 4 IT majors
"""for tick in tickers:
    print(tick, it_stocks[tick]['Close'].min())
    
for tick in tickers:
    print(tick, it_stocks[tick]['Close'].max())"""

# More efficient way to use pandas cross section method
it_stocks.xs(key='Close',axis=1,level='Stock Information').max()
it_stocks.xs(key='Close',axis=1,level='Stock Information').min()

# Calculations of Stock returns using pandas pct_change()
# Create a returns dataframe as blank
returns = pd.DataFrame()

for tick in tickers:
    returns[tick+' Return'] = it_stocks[tick]['Close'].pct_change()
    
returns.head()

# Basic EDA using Seaborn pairplot
sns.pairplot(returns[1:])

# Percent Change in returns output minimum, maximum, standard deviation
returns.idxmin()
returns.idxmax()
returns.std()
returns.ix['2017-01-01':'2018-01-01'].std()

# Seaborn distplot to show Oracle Stock returns during 2017
figsize=(12,4)
sns.distplot(returns.ix['2017-01-01':'2018-01-01']['ORCL Return'],color='green',bins=100)

# Seaborn distplot to show Microsoft Stock returns during 2009
sns.distplot(returns.ix['2009-01-02':'2010-01-01']['MSFT Return'],color='red',bins=100)

# Matplotlib Line plot to show performance of all four IT majors year wise
for tick in tickers:
    it_stocks[tick]['Close'].plot(figsize=(12,4),label=tick)
plt.legend()

# Seaborn heatmap to plot correlation between Closing Stock prices of 4 IT majors
sns.heatmap(it_stocks.xs(key='Close',axis=1,level='Stock Information').corr(),annot=True)