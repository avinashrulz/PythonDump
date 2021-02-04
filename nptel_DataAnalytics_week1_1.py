import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('D:/DataScience_DataSet/DataSet/gapminder-FiveYearData.csv')

#Display first 5 rows of a DataFrame
print(df.head())

#Display last 5 rows of a DataFrame
print(df.tail())

#Display number of rows and columns
print(df.shape)

#Display all column names
print(df.columns)

#Display data types of each column
print(df.dtypes)

#additional information on all columns
print(df.info())

#Put one column in a separate dataframe
country_df = df['country']
print(country_df)

#Subset of the dataframe
subset = df[['country', 'year', 'continent']]
print(subset)

#Display first row
print(df.loc[0])