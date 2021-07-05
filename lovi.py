import pandas as pd

countries=['Algeria','Angola','Benin','Botswana','Burkina Faso','Burundi','Cabo Verde','Cameroon','Central African Republic','Chad','Comoros','Democratic Republic of the Congo','Republic of the Congo','Cote d\'Ivoire','Djibouti','Egypt','Equatorial Guinea','Eritrea','Ethiopia','Gabon','Gambia','Ghana','Guinea','Guinea Bissau','Kenya','Lesotho','Liberia','Libya','Madagascar','Malawi','Mali','Mauritania','Mauritius','Morocco','Mozambique','Namibia','Niger','Nigeria','Rwanda','Sao Tome and Principe','Senegal','Seychelles','Sierra Leone','Somalia','South Africa','South Sudan','Sudan','Swaziland','Tanzania','Togo','Tunisia','Uganda','Zambia','Zimbabwe']


URL = 'http://wdi.worldbank.org/table/2.13'
table = pd.read_html(URL)

#getting the table needed
df_measles = pd.DataFrame(table[2])
# print(df_measles)

#gets only the first section of the table. "from the flamy deserts of Afghan to the tropical plains of Zibambwe"
rowsNeeded = df_measles.drop(labels=[214,215,216, 217,218,219, 220, 221,222, 223,224, 225 ], axis=0)
columnsNeeded = rowsNeeded.drop([1, 2,3,4,7,8,9,10,11,12], axis=1)

columnsNeeded.columns = ["name", "2019(1st)", "2019(2nd)"]

# print(columnsNeeded)


df_data = pd.DataFrame({"name" : [], "2019(1st)" : [], "2019(2nd)" : []})

for i in countries:
    NewAfricanData_df = columnsNeeded.loc[columnsNeeded['name'] == i]
    df_data = pd.concat([df_data, NewAfricanData_df])

df_data = df_data.reset_index(drop=True)

print(df_data)


#csv data
# loviCSV = pd.read_csv('./lovi.csv')

#get country latitude and longitudeS

