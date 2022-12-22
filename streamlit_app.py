from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    import os
    import xml.etree.ElementTree as ET 
    import pandas as pd
    planilla = pd.read_excel('Formulario equivalencias.xlsx')
    planilla.drop(0,axis=0,inplace=True)
    planilla=planilla.rename(columns={'Información sobre Dispositivo Médico':'Nombre Español','Unnamed: 1':'Nombre Ingles','Códigos identificación':'UMDNS','Unnamed: 3':'GMDN','NO COMPLETAR':'Término EMDN','NO COMPLETAR.1':'Código EMDN'})
    Base = pd.read_excel("GMDN_EMDN_VF.xlsx")
    Base_GMDN_EMDN =Base[['codigo1_1','termino1_1','codigo2_1','termino2_1']]
    Base_GMDN_EMDN=Base_GMDN_EMDN.rename(columns={'codigo1_1':'Codigo GMDN','termino1_1':'Termino GMDN','codigo2_1':'Codigo EMDN','termino2_1':'Termino EMDN'})
    Base_GMDN_EMDN=Base_GMDN_EMDN.rename(columns={'codigo1_1':'Codigo GMDN','termino1_1':'Termino GMDN','codigo2_1':'Codigo EMDN','termino2_1':'Termino EMDN'})
    planilla = planilla.rename(columns={'GMDN':'Codigo GMDN'})
    planilla['Codigo GMDN'] = planilla['Codigo GMDN'].astype(int)
    df_merged = Base_GMDN_EMDN.merge(planilla)
    df_merged.to_excel("formulario equivalencias respuesta.xlsx",index=False)


    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
