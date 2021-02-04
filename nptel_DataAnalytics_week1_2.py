#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('D:/DataScience_DataSet/DataSet/gapminder-FiveYearData.csv')

#print a row
#print(df.loc[0])

#print last row
#print(df.tail(n=1))
#print(df.iloc[-1])

#print specific columns
#subset = df.loc[:, ['year', 'lifeExp']]
#subset = df.iloc[:, [1,2,-1]]
#print(subset)

#print Specific rows
#print(df.loc[[1,99,999]])
#print(df.iloc[[1,99,999]])

#using a list to print subset
#small_range = list(range(5))
#print(df.loc[small_range])
#print(df.iloc[:, small_range])

#print specific rows and column value
#print(df.loc[42, 'country'])

#subsetting multiple rows and columns
#print(df.iloc[[1,3,5], [1,3,5]])
#print(df.loc[[1,3,5], ['gdpPercap','pop','country']])

#second method for subsetting multiple rows and columns
#print(df.iloc[10:15, [1,3,5]])
#print(df.loc[20:28, ['gdpPercap','pop','country']])

#groupedby
#print(df.groupby('year')['lifeExp'].mean())

#stacked table using groupby
multi_group_var = df.groupby(['year', 'continent'])[['lifeExp','gdpPercap']].mean()
#print(multi_group_var)

#resetting stacked table
flat = multi_group_var.reset_index()
#print(flat)
#print(df.loc[0])

#print unique frequeny
#print(df.groupby('continent')['country'].nunique())

#Plot simple graph
group_by_expectancy = df.groupby('year')['lifeExp'].mean()
group_by_expectancy.plot()
#print(group_by_expectancy.plot())


a = [1,2,3,4,5]
b = [6,7,8,9,10]
#print(a.append(b))
#print(a.extend(b))
print(a+b)

x = 10
x = x+10
x=x-5
print(x)

x,y = 20,60
y,x,y-10,x+10
print(x,y)


# %%
