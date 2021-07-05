from numpy.core.fromnumeric import sort
import pandas as pd
import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px 

countries=['Algeria','Angola','Benin','Botswana','Burkina Faso','Burundi','Cabo Verde','Cameroon','Central African Republic','Chad','Comoros','Democratic Republic of the Congo','Republic of the Congo','Cote d\'Ivoire','Djibouti','Egypt','Equatorial Guinea','Eritrea','Ethiopia','Gabon','Gambia','Ghana','Guinea','Guinea Bissau','Kenya','Lesotho','Liberia','Libya','Madagascar','Malawi','Mali','Mauritania','Mauritius','Morocco','Mozambique','Namibia','Niger','Nigeria','Rwanda','Sao Tome and Principe','Senegal','Seychelles','Sierra Leone','Somalia','South Africa','South Sudan','Sudan','Swaziland','Tanzania','Togo','Tunisia','Uganda','Zambia','Zimbabwe']


url= "https://developers.google.com/public-data/docs/canonical/countries_csv"
table = pd.read_html(url)

main_df = pd.DataFrame(table[0])

# print(main_df)

df_sortedCoods = pd.DataFrame({'country' : [], 'latitude' : [], 'longitude' : [], 'name' : []})

for i in countries:
    new_df = main_df.loc[main_df['name'] == i]
    df_sortedCoods = pd.concat([df_sortedCoods, new_df])

df_sortedCoods = df_sortedCoods.drop('country', axis=1)

df_sortedCoods = df_sortedCoods.reset_index(drop=True)
#prints list of African countries with their coordinates.
print(df_sortedCoods)

#convert lat and long to points
def plotMap():
    geo_df = gpd.GeoDataFrame(df_sortedCoods, geometry = gpd.points_from_xy(df_sortedCoods.longitude, 
                                                                        df_sortedCoods.latitude))

    # print(geo_df)

    # get buitin dataset from geopoints
    world_data = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    #plot map
    axis = world_data[world_data.continent == 'Africa'].plot(color='lightblue',
                                                         edgecolor='black')
    geo_df.plot(ax = axis, color='green')
    plt.title('African Countries')
    plt.show()
    
# plotMap()