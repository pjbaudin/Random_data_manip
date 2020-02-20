#!/usr/bin/env python

"""
Script to read csv files by chunk and insert to a database table
Uses pandas interpretation of the data type to create the table
"""

import pandas as pd
import sqlalchemy as sa

# Set up parameters
file_path =

conn = ""
db_connection = sa.engine(conn)

db_table_cible = "FCI_client"  # Fichier Client Initial

chunk_size = 1000000

# Insert by chunk into the DB
chunk_cnt = 0

for chunk in pd.read_csv(file_path, chunksize=chunksize):
    chunk.to_sql(db_table_cible,
                 con=db_connection,
                 if_exists="append",
                 method="multi")    
    chunk_cnt += 1

# Result output
print("Number of chunks processed ", chunk_cnt)

sql_top = "SELECT TOP (10) * FROM" + db_table_cible
sample = pd.read_sql_query(sql_top, con=db_connection)

print("First 10 rows : ")
print(sample)
print("Sample info :")
print(sample.info())