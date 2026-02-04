import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Analisi descriptiu")
st.sidebar.header("Analisi descriptiu")

st.title(":bar_chart: Analisi Descriptiu")

tab1, tab2 = st.tabs(["Videojocs Cat", "Vendes gènere"])

df= pd.read_csv("./dat/output/videojocsCat.csv", sep =";")

df["Pujada_Inversio_Absoluta"] = (
    df["Pujada_Inversio_Absoluta"]
    .str.replace(",", ".", regex=False)
    .astype(float)
)
with tab1:
    
    fig4 = px.bar(
    df,
    x="Any",
    y=["Facturacio_MEUR", "Treballadors", "Videojocs_Produits"],
    barmode="group",
    title="Comparació anual entre variables clau"
    )

    fig4.update_layout(
        xaxis_title="Any",
        yaxis_title="Valor",
        legend_title="Variable"
    )

    st.plotly_chart(fig4)

    st.write("Continuem veien que la tendencia es que a mes facturació, mes estudis i mes treballadors hi ha al sector i que aquesta tendencia es al alça.")
    
    

    fig5 = px.scatter(
        df,
        x="Inversio_Captada_Acumulada_MEUR",
        y="Facturacio_MEUR",
        size="Treballadors",
        color="Percentatge_Exportacio",
        color_continuous_scale=px.colors.diverging.RdBu,
        hover_name="Any",
        title="Relació entre inversió, facturació i estructura del sector"
    )

    fig5.update_layout(
        xaxis_title="Inversió acumulada (M€)",
        yaxis_title="Facturació (M€)"
    )

    st.plotly_chart(fig5)
        
    st.write("En aquest gràfic veiem que a mesura que la inversio acumulada i la facturació augmenten, el percentatge d'exportacions creix.")
    
    # Reorganitzar a format llarg per apilar
    df_long = df.melt(
        id_vars="Any",
        value_vars=["Inversio_Captada_Acumulada_MEUR", "Pujada_Inversio_Absoluta"],
        var_name="Tipus_Inversio",
        value_name="Inversio"
    )

    # Gràfic de barres apilades
    fig8 = px.bar(
        df_long,
        x="Any",
        y="Inversio",
        color="Tipus_Inversio",
        barmode="stack",
        title="Creixement de la inversió: barres apilades + línia"
    )

    # Afegir línia de la inversió acumulada
    fig8.add_scatter( x=df["Any"],
                      y=df["Pujada_Inversio_Absoluta"],
                      mode="lines+markers",
                      name="Pujada anual d'inversió", 
                      line=dict(color="black", width=3) 
     )


    fig8.update_layout(
        xaxis_title="Any",
        yaxis_title="Inversió (M€)",
        legend_title="Tipus d'inversió"
    )
    st.plotly_chart(fig8)
    st.write("En aquest gràfic veiem que la tendencia anual en la inversió captada en el sector fluctua, tot i que segueix pujant, amb una pujada 10 punts menor l'any 2024 respecte a l'any anterior.")
    

      
with tab2:
    
    df2= pd.read_csv("./dat/output/sales_genre.csv", sep =";")
    
    fig6 = px.box(
    df2,
    x="Genre",
    y="Global_Sales",   
    color="Genre",
    title="Distribució de vendes globals per gènere",
    )

    fig6.update_layout(xaxis_title="Gènere", yaxis_title="Vendes globals (M€)")
    
    st.plotly_chart(fig6)
    
    st.write("Les vendes globals per gènere deixen constancia que, globalment, el gènere de videojoc més venut es el d'acció, seguit del shooter i dels videojocs d'esports.")
    
    df_long = df2.melt(
    id_vars=["Genre", "Year"],
    value_vars=["Global_Sales", "US_Sales", "EU_Sales"],
    var_name="Sales_Type",
    value_name="Sales"
    )

    fig9 = px.bar(
        df_long,
        x="Genre",
        y="Sales",
        color="Sales_Type",
        title="Vendes per gènere i mercat",
        barmode="stack"
    )

    fig9.update_layout(
        xaxis_title="Gènere",
        yaxis_title="Vendes (M€)",
        legend_title="Tipus de vendes",
        xaxis_tickangle=45,
        legend=dict( orientation="h", x=0.5, xanchor="center", y=-0.4, yanchor="top" ), 
        margin=dict(b=120)
    )
    st.plotly_chart(fig9)
    
    st.write("""Amb aquest gràfic queda clar que el gènere per excelència en el sector dels videojocs es el d'acció, tant globalment com a Europa i als Estat Units, i que el mercat segueix els mateixos patrons sigui als Estat Units, a Europa o globalment.
                Aquest fet no ha cambiat en els últims 8 anys.
                En conclusió el gènere que pot reportar més beneficis a un estudi de videojocs es el d'acció.""")    





