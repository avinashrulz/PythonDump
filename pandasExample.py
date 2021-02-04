import pandas as pd

df = pd.DataFrame({'little':['This is awesome', 'This is aweful', 'Have faith in yourself'], 
'more':['This is your Destiny', 'Its worthwhile', 'Sand Ki Aankh']}, index=['row 1', 'row 2', 'row 3'])
print(df)

ds = pd.Series([30, 45, 50], index=['Sales 2021', 'Sales 2022', 'Sales 2023'], name='DataVault')
print(ds)