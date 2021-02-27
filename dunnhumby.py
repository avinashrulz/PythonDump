import pandas as pd
import numpy as np
import matplotlib as mpl

rt = pd.read_csv("D:/Personal/Dataanalytics/Relevency_table.csv")
et = pd.read_csv("D:/Personal/Dataanalytics/Exclusion_table.csv")
pt = pd.read_csv('D:/Personal/Dataanalytics/Products_table.csv')

#print(rt.loc[(rt.customers == 'A10001') & (rt['product'] == 5649607)]) 
print(rt.loc[(rt.customers == 'A10001') & (rt['product'] == 5649607) | (rt['customers'] == 'A10002')  & (rt['product'] == 5649607)]) 
print(rt.loc[rt.product.isin([5649607, 5649565])])







































#for each and every product, 

# if rt.groupby('customers')['product'].nunique()<=2:
#     print(rt.groupby('customers')['product'].nunique())
#print(pt.shape)    
#print (rt.head(50))
# grouped = rt.groupby('product')['relevancy_score'].mean()
#print(grouped)
# print (et.head())
# print (pt.head())