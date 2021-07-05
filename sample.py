import geopandas as gdp

worlddata=gdp.read_file(gdp.datasets.get_path("naturalearth_lowres"))

import pandas as pd

url="http://wdi.worldbank.org/table/2.15"
mydata=pd.read_html(url)[2]
mydata.drop(mydata.columns[[5,6,7,8,9,10,11,12]], axis = 1, inplace = True)
mydata = mydata.rename(columns={mydata.columns[0]: 'name'})
newdf=pd.merge(worlddata,mydata,how="left",on="name")

newdf=newdf[(newdf["iso_a3"]=="BRN") | (newdf["iso_a3"]=="KHM") |(newdf["iso_a3"]=="TLS")|(newdf["iso_a3"]=="IDN")|(newdf["iso_a3"]=="MMR")|(newdf["iso_a3"]=="LAO")|(newdf["iso_a3"]=="MYS")|(newdf["iso_a3"]=="PHL")|(newdf["iso_a3"]=="SGP")|(newdf["iso_a3"]=="THA")|(newdf["iso_a3"]=="VNM")]
newdf[["2012", "2016","2018","2020"]] = newdf[[1, 2,3,4]].apply(pd.to_numeric,errors="coerce").fillna(0).astype(int)
newdf.drop(newdf.columns[[1,2,3,4]], axis = 1, inplace = True)

import matplotlib.pyplot as plt

figure,axes =plt.subplots(2,2,figsize=(50,50))

axis=axes[0,0]
axis.axis('off')
axis.set_title("PREVALENCE OF WASTING IN SOUTH EAST ASIA \nFOR THE YEAR 2012",fontsize=10)
axis.annotate("ONDUSO LABAN OMBONGI", xy=(.01, .01), xycoords='axes fraction',fontsize=8)
axis.annotate("ENC221-0308/2018", xy=(.6, .01), xycoords='axes fraction',fontsize=8)
axis=axes[0,1]
axis.axis('off')
axis.set_title("PREVALENCE OF WASTING IN SOUTH EAST ASIA \nFOR THE YEAR 2016",fontsize=10)
axis.annotate("ONDUSO LABAN OMBONGI", xy=(.01, .01), xycoords='axes fraction',fontsize=8)
axis.annotate("ENC221-0308/2018", xy=(.6, .01), xycoords='axes fraction',fontsize=8)
axis=axes[1,0]
axis.axis('off')
axis.set_title("PREVALENCE OF WASTING IN SOUTH EAST ASIA \nFOR THE YEAR 2018",fontsize=10)
axis.annotate("ONDUSO LABAN OMBONGI", xy=(.01, .01), xycoords='axes fraction',fontsize=8)
axis.annotate("ENC221-0308/2018", xy=(.6, .01), xycoords='axes fraction',fontsize=8)
axis=axes[1,1]
axis.axis('off')
axis.set_title("PREVALENCE OF WASTING IN SOUTH EAST ASIA \nFOR THE YEAR 2020",fontsize=10)
axis.annotate("ONDUSO LABAN OMBONGI", xy=(.01, .01), xycoords='axes fraction',fontsize=8)
axis.annotate("ENC221-0308/2018", xy=(.6, .01), xycoords='axes fraction',fontsize=8)

# import mapclassify

newdf.plot("2012", cmap="Blues",ax=axes[0,0],scheme='EqualInterval',legend=True,figsize=(25,25),edgecolor="blue",linewidth=0.5,legend_kwds=dict(loc='upper left',title="Weight for height\n(% of children under 5)", bbox_to_anchor=(1, 1)))
newdf.plot("2016", cmap="Blues",ax=axes[0,1],scheme='EqualInterval',legend=True,figsize=(25,25),edgecolor="blue",linewidth=0.5,legend_kwds=dict(loc='upper left',title="Weight for height\n(% of children under 5)", bbox_to_anchor=(1, 1)))
newdf.plot("2018", cmap="Blues",ax=axes[1,0],scheme='EqualInterval',legend=True,figsize=(25,25),edgecolor="blue",linewidth=0.5,legend_kwds=dict(loc='upper left',title="Weight for height\n(% of children under 5)", bbox_to_anchor=(1, 1)))
newdf.plot("2020", cmap="Blues",ax=axes[1,1],scheme='EqualInterval',legend=True,figsize=(25,25),edgecolor="blue",linewidth=0.5,legend_kwds=dict(loc='upper left',title="Weight for height\n(% of children under 5)", bbox_to_anchor=(1, 1)))
plt.show()
