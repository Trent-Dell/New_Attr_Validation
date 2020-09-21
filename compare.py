#%%
import os
import csv
import pandas as pd
import numpy as np
import matplotlib
from sqlalchemy import create_engine
from config import db_password

#%%
# load data into DataFrames
New_Attr = "data\W01027.csv"
GNS_load = "data\GNS_Sep_20.csv"

df_Attr = pd.read_csv(New_Attr)
df_GNS = pd.read_csv(GNS_load)

#%%
# check data frames
df_GNS
# df_Attr

#%%
# cleaning IMCG DF
df_Attr.columns = df_Attr.columns.str.replace(' ','')
df_Attr
df_GNS.columns = df_GNS.columns.str.replace(' ','')
print(
    f"{df_GNS.head()}/n/n"
    f"{df_Attr.head()}"
    )

#%%
NewNotNull = df_Attr.notnull().sum()
NewIsNull = df_Attr.isnull().sum()
print(
    f"{NewNotNull}\n\n"
    f"{NewIsNull}\n\n"
    f"Data Types:\n{df_Attr.dtypes}"
    )

#%%
GnsNotNull = df_GNS.notnull().sum()
GnsIsNull = df_GNS.isnull().sum()
print(
    f"{GnsNotNull}\n\n"
    f"{GnsIsNull}\n\n"
    f"Data Types:/n  {df_GNS.dtypes}"
    )

# %%
# df[df.string1==df.string2]
df_IMCG["In_GNS?"] = np.where(df_GNS['PARTTYPE'] == New_Attr['PARTTYPE'], 'True', 'False')

#%%
# Applying upper() method on 'PARTTYPE' column in GNS table

df_GNS['PARTTYPE'] = df_GNS['PARTTYPE'].apply(lambda x: x.upper())
df_GNS

#%%
# compare tables
New_Attr['PARTTYPE'].isin(df_GNS['PARTTYPE']).value_counts()

# %%
mergedStuff = pd.merge(df_GNS, New_Attr, on=['PARTTYPE'], how='inner')
mergedStuff

# %%
# comparing Part Type columns of truth tables
df_GNS['PARTTYPE'].isin(New_Attr['PARTTYPE']).value_counts()

# %%
outerMerge = pd.merge(df_GNS, New_Attr, on=['PARTTYPE'], how='outer')
outerMerge
outerMerge.to_csv('data\gns_imcg_fullJoin.csv')


# %%
# write outer merge to csv
# %%
