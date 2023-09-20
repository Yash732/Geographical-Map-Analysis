
import numpy as np
import streamlit as st
import pandas as pd # read csv, df manipulation
# import time 
import plotly.express as px # interactive charts 
import matplotlib.pyplot as plt
# import geopandas as gpd
# import random



# read csv from a github repo
# df = pd.read_csv("D:/projects/dashboard_streamlit/bank.csv")
# df = pd.read_csv("bank.csv")
geo_df = pd.read_csv("D:/projects/dashboard_streamlit/dummyWasteData.csv")


# SHAPEFILE = "D:/codes/Python/keralaData/keralDsitrictdata/kerala/shapefiles/district.shp"
# Read shapefile using Geopandas
# geo_df = gpd.read_file(SHAPEFILE)[['DISTRICT','DT_CEN_CD','geometry']]


st.set_page_config(  
    page_title = 'Kerala Map',
    page_icon = '✅',
    layout = 'wide'
)

title = 'Daily waste produce in Kerala'
col = 'Resultant'
vmin = geo_df[col].min()
vmax = geo_df[col].max()
cmap = 'Reds'

# geo_df['label'] = geo_df['DISTRICT'].apply(lambda x: x.upper())
ax = geo_df.plot(figsize=(10, 10), column= col,alpha=0.7, edgecolor='0.8',cmap = cmap)
geo_df.apply(lambda x: ax.annotate(s=x['label'], xy=x.geometry.centroid.coords[0], ha='center'),axis=1)

#fig,ax = plt.subplots(1,figsize = (20,8))
ax.axis('off')

# geo_df.plot(column = col,ax = ax,edgecolor = '0.8',linewidth = 1,cmap = cmap)
ax.set_title(title,fontdict = {'fontsize' :'25','fontweight' :'3'})

# st.markdown("### First Chart")
# fig = px.density_heatmap(data_frame=geo_df, y = 'age_new', x = 'marital')
st.write(ax)





# dashboard title
st.title("Daily waste Produce")

# top-level filters 

