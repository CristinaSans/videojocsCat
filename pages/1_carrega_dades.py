import streamlit as st
import pandas as pd

st.set_page_config(page_title="Carrega dades")

st.sidebar.header("Carrega dades")

st.title(":floppy_disk: Carrega de dades")

# Carregar primer dataframe
uploaded_file = st.file_uploader("Carrega el fitxer CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Guardar el dataframe a session_state
    st.session_state["df_videojocs_cat"] = df

    st.success("Dades carregades correctament!")
    
        
    st.write('DataFrame videojocs Catalunya')

    st.write(df.head())

else:
    st.warning("Carrega fitxer videojocs-cat")

# Carregar segon dataframe
uploaded_file2 = st.file_uploader("Carrega el 2on fitxer CSV", type=["csv"])

if uploaded_file2 is not None:
    
    df2 = pd.read_csv(uploaded_file2)
    st.session_state["df_sales_genre"] = df2
    st.success("Dades carregades correctament!")
    
        
    st.write('DataFrame Vendes videojocs per gènere')

    st.write(df2.head())

    
    
    
else:
    st.warning("Carrega fitxer vendes-gènere")



st.subheader("Descripció dels datasets:")

st.write("""El primer dataset detalla la facturació, els treballadors, el estudis actius, els videojocs produits, el percentatge d'exportacio i la inversió captada acumulada.
El segon dataset conté les ventes (globals, EUA i Europa) i el tant percent global per gènere i any.
""")

st.subheader("Fonts:")

st.write(""" Les fonts dels datasets son:

dataset 1 :

- Llibre blanc del videojoc a Catalunya -->(link:https://culturadigital.blog.gencat.cat/estudis/  )
- ICEC(Institut Català de les Empreses Culturals)--> (link:https://icec.gencat.cat/ca/observatori/dades/)
- ACCIÓ(Generalitat de Catalunya)-->(link:https://www.accio.gencat.cat/ca/serveis/banc-coneixement/cercador/BancConeixement/eic-els-videojocs-a-catalunya)
- DEV (Associació Espanyola de Videojocs)-->(link: https://www.dev.org.es/)

dataset 2:

- NPD Group/ Circana (EUA)-->(link:https://vgsales.fandom.com/wiki/NPD_sales_figures)
- GSD/ISFE(Europa)-->(https://www.videogameseurope.eu/data-key-facts/)
- VGChart(Global)-->(https://www.vgchartz.com/)
- Steam (ingressos per gènere)-->(link:https://steamdb.info/)""")