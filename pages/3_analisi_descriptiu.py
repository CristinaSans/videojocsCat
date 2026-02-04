import streamlit as st
import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

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
        
    fig4_sub = make_subplots(rows=1, cols=1)

    for col in ["Facturacio_MEUR", "Treballadors", "Videojocs_Produits"]:
        fig4_sub.add_trace(
            go.Bar(
                x=df["Any"],
                y=df[col],
                name=col,
                showlegend=True
            )
        )

    fig4_sub.update_layout(
        title="Comparació anual entre variables clau",
        xaxis_title="Any",
        yaxis_title="Valor",
        legend=dict(orientation="h", x=0.5, xanchor="center", y=-0.2)
    )

    st.plotly_chart(fig4_sub, use_container_width=True)

    st.write("Continuem veien que la tendencia es que a mes facturació, mes estudis i mes treballadors hi ha al sector i que aquesta tendencia es al alça.")
    
    
    fig5_sub = make_subplots(rows=1, cols=1)

    fig5_sub.add_trace(
        go.Scatter(
            x=df["Inversio_Captada_Acumulada_MEUR"],
            y=df["Facturacio_MEUR"],
            mode="markers",
            marker=dict(
                size=df["Treballadors"],
                sizemode="area",
                sizeref=max(df["Treballadors"]) / 40,   # fa visibles les bombolles
                color=df["Percentatge_Exportacio"],
                colorscale="RdBu",
                line=dict(width=1, color="black"),       # contorn per fer-les destacar
                showscale=True
            ),
            text=df["Any"],
            hovertemplate="<b>Any:</b> %{text}<br>"
                          "Inversió: %{x} M€<br>"
                          "Facturació: %{y} M€<br>"
                          "<extra></extra>"
        )
    )

    fig5_sub.update_layout(
        title="Relació entre inversió, facturació i estructura del sector",
        xaxis_title="Inversió acumulada (M€)",
        yaxis_title="Facturació (M€)",
        legend=dict(
            orientation="h",
            x=0.5,
            xanchor="center",
            y=-0.2
        )
    )

    st.plotly_chart(fig5_sub, use_container_width=True)
        
    st.write("En aquest gràfic veiem que a mesura que la inversio acumulada i la facturació augmenten, el percentatge d'exportacions creix.")
    
   
    # Reorganitzar a format llarg per apilar
   
    df_long = df.melt(
    id_vars="Any",
    value_vars=["Inversio_Captada_Acumulada_MEUR", "Pujada_Inversio_Absoluta"],
    var_name="Tipus_Inversio",
    value_name="Inversio"
    )

    fig8_sub = make_subplots(rows=1, cols=1)

    for tipus in df_long["Tipus_Inversio"].unique():
        subset = df_long[df_long["Tipus_Inversio"] == tipus]
        fig8_sub.add_trace(
            go.Bar(
                x=subset["Any"],
                y=subset["Inversio"],
                name=tipus,
                showlegend=True
            )
        )

    fig8_sub.add_trace(
        go.Scatter(
            x=df["Any"],
            y=df["Pujada_Inversio_Absoluta"],
            mode="lines+markers",
            name="Pujada anual d'inversió",
            line=dict(color="black", width=3),
            showlegend=True
        )
    )

    fig8_sub.update_layout(
        title="Creixement de la inversió: barres apilades + línia",
        xaxis_title="Any",
        yaxis_title="Inversió (M€)",
        legend=dict(orientation="h", x=0.5, xanchor="center", y=-0.2)
    )

    st.plotly_chart(fig8_sub, use_container_width=True)

    
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
    )

    st.plotly_chart(fig9, use_container_width=True)

    
    st.write("""Amb aquest gràfic queda clar que el gènere per excelència en el sector dels videojocs es el d'acció, tant globalment com a Europa i als Estat Units, i que el mercat segueix els mateixos patrons sigui als Estat Units, a Europa o globalment.
                Aquest fet no ha cambiat en els últims 8 anys.
                En conclusió el gènere que pot reportar més beneficis a un estudi de videojocs es el d'acció.""")    








