from numpy.core.fromnumeric import sort
import pandas as pd
import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px 
from mpl_toolkits.axes_grid1 import make_axes_locatable

URL = 'http://wdi.worldbank.org/table/2.13'
WBtables = pd.read_html(URL)


url= "https://developers.google.com/public-data/docs/canonical/countries_csv"
countryTable = pd.read_html(url)

countries=['Algeria','Angola','Benin','Botswana','Burkina Faso','Burundi','Cabo Verde','Cameroon','Central African Republic','Chad','Comoros','Democratic Republic of the Congo','Republic of the Congo','Cote d\'Ivoire','Djibouti','Egypt','Equatorial Guinea','Eritrea','Ethiopia','Gabon','Gambia','Ghana','Guinea','Guinea Bissau','Kenya','Lesotho','Liberia','Libya','Madagascar','Malawi','Mali','Mauritania','Mauritius','Morocco','Mozambique','Namibia','Niger','Nigeria','Rwanda','Sao Tome and Principe','Senegal','Seychelles','Sierra Leone','Somalia','South Africa','South Sudan','Sudan','Swaziland','Tanzania','Togo','Tunisia','Uganda','Zambia','Zimbabwe']

"""
    Getting data from worldbank site
"""

#getting the table needed
df_measles = pd.DataFrame(WBtables[2])
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
# print(df_data)


"""
    getting countries and their coordinates
    
"""

main_df = pd.DataFrame(countryTable[0])
# print(main_df)

df_sortedCoods = pd.DataFrame({'country' : [], 'latitude' : [], 'longitude' : [], 'name' : []})

for i in countries:
    new_df = main_df.loc[main_df['name'] == i]
    df_sortedCoods = pd.concat([df_sortedCoods, new_df])

df_sortedCoods = df_sortedCoods.drop('country', axis=1)

#prints list of African countries with their coordinates.
# print(df_sortedCoods)

joined_df = pd.merge(df_sortedCoods, df_data,how="left",on="name")

print(joined_df)

#convert lat and long to points
def plotMap(Title, columnSelector, Cmaps):
    geo_df = gpd.GeoDataFrame(joined_df, geometry = gpd.points_from_xy(df_sortedCoods.longitude, 
                                                                        df_sortedCoods.latitude))

    # print(geo_df)

    # get buitin dataset from geopoints
    world_data = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # plot map
    axis = world_data[world_data.continent == 'Africa']
    axis = axis.plot(edgecolor='black', column="name", cmap=Cmaps)
    axis.annotate("ENC221-0079/2018  CHARITY LOVI KAGEHA", xy=(.01, .01), xycoords='axes fraction',fontsize=8)
        
    geo_df.plot(ax = axis, column=columnSelector, cmap="Blues", legend=True)
    plt.title(Title)
    plt.show()
    
plotMap('immusation of measles( 12-23months ) First Period', '2019(1st)', "Blues")
plotMap('immusation of measles( 12-23months )', '2019(2nd)', "Purples")
plotMap('immusation of measles( 12-23months ) 2019', '2019(1st)', 'YlOrRd')
plotMap('immusation of measles( 12-23months )', '2019(2nd)', 'BuGn')
