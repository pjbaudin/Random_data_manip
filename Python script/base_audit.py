import os
import pandas as pd
import numpy as np

# Create class: DataShell
class DataShellCSV:
  
	# Init method 
    def __init__(self, filepath):
        self.filepath = filepath
        self.data_as_csv = pd.read_csv(filepath)
    
    # Define method rename_column, with arguments self, column_name, and new_column_name
    def rename_column(self, column_name, new_column_name):
        self.data_as_csv.columns = self.data_as_csv.columns.str.replace(column_name, new_column_name)

    # Get the max column length
    def get_column_max_length(self):
        measurer = np.vectorize(len)
        res = measurer(self.data_as_csv.values.astype(str)).max(axis=0)
        return res

    # Define get_stats method
    def get_stats(self):
        # Return a description data_as_csv
        return self.data_as_csv.describe()

shell = DataShellCSV('./data/avocado.csv')
print(shell.filepath)
print(shell.data_as_csv.info())
print(shell.get_column_max_length())
print(shell.get_stats())


"""
@todo

file delimiter
"""
