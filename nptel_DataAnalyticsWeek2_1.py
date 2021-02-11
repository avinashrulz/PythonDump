#%%
import pandas as pd
import numpy as np
import scipy
from scipy import stats
import statistics
from scipy.stats import skew
import matplotlib
from matplotlib import pyplot as plt

path = "D:/DataScience_DataSet/IBM-313 Marks.xlsx"
table = pd.read_excel(path)
print(table)

x = table['Total']
print(np.mean(x))
print(np.median(x))
print(stats.mode(x))
print(np.var(x))

# Numpy by default has population standard deviation
print(np.std(x))

#import statistics to calculate sample as well as population standard deviation
print(statistics.pstdev(x))
print(statistics.stdev(x))

#import skew from scipy.stats
print(skew(x))

import matplotlib
from matplotlib import pyplot as plt

#for drawing box and whisker plots, import pyplot from matplotlib
plt.boxplot(x, sym='*')
plt.show()
# %%
