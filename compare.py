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
# df_GNS
df_Attr

#%%
# cleaning IMCG DF
df_IMCG.columns = df_IMCG.columns.str.replace(' ','')
df_IMCG
df_GNS.columns = df_GNS.columns.str.replace(' ','')
print(
    f"{df_GNS.head()}/n/n"
    f"{df_IMCG.head()}"
    )

#%%
ImcgNotNull = df_IMCG.notnull().sum()
ImcgIsNull = df_IMCG.isnull().sum()
print(
    f"{ImcgNotNull}\n\n"
    f"{ImcgIsNull}\n\n"
    f"Data Types:\n{df_IMCG.dtypes}"
    )

#%%
GnsNotNull = df_GNS.notnull().sum()
GnsIsNull = df_GNS.isnull().sum()
print(
    f"{GnsNotNull}\n\n"
    f"{GnsIsNull}\n\n"
    f"Data Types:/n  {df_GNS.dtypes}"
    )
#%%
ImcgNotNull = df_IMCG.notnull().sum()
ImcgIsNull = df_IMCG.isnull().sum()
print(
    f"{ImcgNotNull}\n\n"
    f"{ImcgIsNull}\n\n"
    f"Data Types:/n  {df_IMCG.dtypes}"
    )

# %%
# df[df.string1==df.string2]
df_IMCG["In_GNS?"] = np.where(df_GNS['PARTTYPE'] == df_IMCG['PARTTYPE'], 'True', 'False')

#%%
# Applying upper() method on 'PARTTYPE' column in GNS table

df_GNS['PARTTYPE'] = df_GNS['PARTTYPE'].apply(lambda x: x.upper())
df_GNS

#%%
# compare tables
df_IMCG['PARTTYPE'].isin(df_GNS['PARTTYPE']).value_counts()

# %%
mergedStuff = pd.merge(df_GNS, df_IMCG, on=['PARTTYPE'], how='inner')
mergedStuff

# %%
# comparing Part Type columns of truth tables
df_GNS['PARTTYPE'].isin(df_IMCG['PARTTYPE']).value_counts()

# %%
outerMerge = pd.merge(df_GNS, df_IMCG, on=['PARTTYPE'], how='outer')
outerMerge
outerMerge.to_csv('data\gns_imcg_fullJoin.csv')


# %%
# write outer merge to csv
# %%
