import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Analisi exploratori")
st.sidebar.header("Analisi exploratori")

st.title(":mag_right: Analisi exploratori")

if "df_videojocs_cat" not in st.session_state:
    st.error("Carrega les dades primer a la pàgina 1.")
else:
    df = st.session_state["df_videojocs_cat"]


st.subheader("Canvis realitzats als Dataframes:")
tab1, tab2 = st.tabs(["Videojocs Cat", "Vendes gènere"])

#Creació columna target:
with tab1:
   
    df["Pujada_Inversio_Absoluta"] = df["Inversio_Captada_Acumulada_MEUR"].diff().fillna(0) 
    df["Pujada_Inversio_Absoluta"] = df["Pujada_Inversio_Absoluta"].round(2)


    df.to_csv("./dat/output/videojocsCat.csv",  index=False, sep =";", decimal=",")
    
    df= df.set_index("Any")
    st.write(df.head())


    st. write("""Hem cambiat l'index a any i hem afegit una columna en el primer dataframe, que es la següent:

     - Pujada_Inversio_Absoluta --> percentatge de pujada respecte a l'any anterior
     """)


    st.subheader("Gràfics exploratoris:")


    # Selector de gràfic
    opcio = st.selectbox(
        "Selecciona el tipus de gràfic",
        ["Mapa de correlació", "Histogrames"]
    )

    # --- MAPA DE CORRELACIÓ ---
    if opcio == "Mapa de correlació":
        st.subheader("Mapa de correlació")

        corr = df.corr(numeric_only=True)

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5, ax=ax)
        ax.set_title("Mapa de correlació – Indústria del videojoc a Catalunya (2016–2024)")

        st.pyplot(fig)

    # --- HISTOGRAMES ---

    elif opcio == "Histogrames":
        st.subheader("Histogrames de variables numèriques")

        # Seleccionar columnes numèriques excepte 'Any'
        numeric_cols = df.select_dtypes(include="number").columns
        numeric_cols = [col for col in numeric_cols if col]

        # Selector de variable numèrica
        variable = st.selectbox("Selecciona una variable numèrica", numeric_cols)

        # Crear histograma de la variable seleccionada
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(df[variable], bins=10, edgecolor="black")
        ax.set_title(f"Histograma de {variable}")
        ax.set_xlabel(variable)
        ax.set_ylabel("Freqüència")

        st.pyplot(fig)
        
        st.write("Els  tots histogrames son de distribució multimodal, excepte el de percentatge_exportació que es bimodal")
     



with tab2:
        
    if "df_sales_genre" not in st.session_state:
        st.error("Carrega les dades primer a la pàgina 1.")
    else:
        df2 = st.session_state["df_sales_genre"]
    
    st.write(df2.head())
    st. write("Aquest dataset es manté com era")

    df2.to_csv("./dat/output/sales_genre.csv",  index=False, sep =";", decimal=",")
    
    st.subheader("Gràfics exploratoris:")


    # Reorganitzar el dataframe a format llarg
    df_long = df2.melt(
        id_vars=["Genre", "Year"],
        value_vars=["Global_Sales", "US_Sales", "EU_Sales"],
        var_name="Sales_Type",
        value_name="Sales"
    )

    # Selector d'any
    years = sorted(df_long["Year"].unique())

    selected_year = st.selectbox("Selecciona l'any", years)

    # Filtrar dades per l'any seleccionat
    data_year = df_long[df_long["Year"] == selected_year]

    # Ordenar gèneres per vendes globals
    order_genres = (
        df2[df2["Year"] == selected_year]
        .sort_values("Global_Sales", ascending=False)["Genre"]
        .unique()
    )

    # Crear figura
    fig, ax = plt.subplots(figsize=(12, 6))

    sns.barplot(
        data=data_year,
        x="Sales_Type",
        y="Sales",
        hue="Genre",
        hue_order=order_genres,
        ax=ax
    )

    ax.set_title(f"Vendes per tipus i gènere — Any {selected_year}")
    ax.set_xlabel("Tipus de vendes")
    ax.set_ylabel("Vendes (M€)")
    ax.legend(title="Gènere", bbox_to_anchor=(1.05, 1), loc='upper left')

    st.pyplot(fig)
    st.write("En els gràfics podem comprobar que el gènere més venut, any rere any, es el d'acció")

