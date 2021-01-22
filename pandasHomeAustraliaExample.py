import pandas as pd
melbourne_file_path = 'C:/Users/avina/OneDrive/Desktop/Knowledge Hub/Kaggle/DataSet/archive/melb_data.csv'
aus_data = pd.read_csv(melbourne_file_path)
print(aus_data.describe())