#data import and convert to data frame
import pandas as pd

df=pd.read_csv('air-pollution.csv')
print(df)

#clean data rows empty
cleaned_df = df.dropna(how="all")

# Replace null values with 0
cleaned_df = cleaned_df.fillna(0)

#remove duplicate entities
cleaned_df.drop_duplicates(inplace=True)