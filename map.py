
import pandas as pd
import streamlit as st
import leafmap
#filepath = 'C:\Users\colep\OneDrive - Massey University\Data Wrangling and Machine Learning\Assignment 3 Group Project Personal'

Area_Coords = pd.read_csv(r"C:\Users\colep\OneDrive - Massey University\Data Wrangling and Machine Learning\Assignment 3 Group Project Personal\Geo_info.csv")
Area_Coords['info'] = 'hello'

import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.info(
    """
    - Web App URL: <https://streamlit.geemap.org>
    - GitHub repository: <https://github.com/giswqs/streamlit-geospatial>
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Qiusheng Wu: <https://wetlands.io>
    [GitHub](https://github.com/giswqs) | [Twitter](https://twitter.com/giswqs) | [YouTube](https://www.youtube.com/c/QiushengWu) | [LinkedIn](https://www.linkedin.com/in/qiushengwu)
    """
)

st.title("Marker Cluster")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[-36.8, 175], zoom=8.5)
        cities = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
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
