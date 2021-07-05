from numpy.core.fromnumeric import sort
import pandas as pd
import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px 


URL = 'http://wdi.worldbank.org/table/2.13'
table = pd.read_html(URL)


url= "https://developers.google.com/public-data/docs/canonical/countries_csv"
table = pd.read_html(url)

countries=['Algeria','Angola','Benin','Botswana','Burkina Faso','Burundi','Cabo Verde','Cameroon','Central African Republic','Chad','Comoros','Democratic Republic of the Congo','Republic of the Congo','Cote d\'Ivoire','Djibouti','Egypt','Equatorial Guinea','Eritrea','Ethiopia','Gabon','Gambia','Ghana','Guinea','Guinea Bissau','Kenya','Lesotho','Liberia','Libya','Madagascar','Malawi','Mali','Mauritania','Mauritius','Morocco','Mozambique','Namibia','Niger','Nigeria','Rwanda','Sao Tome and Principe','Senegal','Seychelles','Sierra Leone','Somalia','South Africa','South Sudan','Sudan','Swaziland','Tanzania','Togo','Tunisia','Uganda','Zambia','Zimbabwe']

print(table[0])
# df_measles = pd.DataFrame([table])