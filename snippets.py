"""filtering row data in Pandas"""

#creating a new dataframe based where color is the column name and green is the condition/property of the column name
green_df = df.loc[df['Color'] == 'Green']
#for numerical conditions
price_df = df.loc[df['Price'] <= 10]

#appending dataframes
df1.append(df2)
