
import pandas as pd
import streamlit as st
import leafmap
#filepath = 'C:\Users\colep\OneDrive - Massey University\Data Wrangling and Machine Learning\Assignment 3 Group Project Personal'

Area_Coords = pd.read_csv(r"Geo_info.csv")
print(Area_Coords.columns)
#Area_Coords['info'] = 'hello'
Area_Coords[['Respondents','Area','Latitude', 'Longitude', '15-29 years',
       '30-64 years', '65 years and over', 'No qualification',
       'Level 3 certificate', 'Level 4 certificate', 'Level 5 diploma', 'Level 6 diploma',
       'Bachelor degree and level 7 qualification',
       'Post-graduate and honours degrees', 'Masters degree',
       'Doctorate degree',
       'European', 'Maori',
       'Pacific Peoples', 'Asian', 'Middle Eastern/Latin American/African',
       'Other ethnicity', 'Regular smoker', 'Ex-smoker',
       'Never smoked regularly', 'No dependent children',
       'One dependent child', 'Two dependent children',
       'Three dependent children', 'Four or more dependent children',
       'Total people - with at least one religious affiliation', 'No religion']]
import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.title("Marker Cluster")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[-36.8, 175], zoom=8.5)
        regions = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson'

       	#m.add_geojson(regions, layer_name='NZ Electorates')
        m.add_points_from_xy(
            Area_Coords,
            x="Longitude",
            y="Latitude",
            icon_names=['gear', 'map', 'leaf', 'globe'],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=650)
