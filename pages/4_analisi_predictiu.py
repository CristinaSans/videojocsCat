import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go

st.set_page_config(page_title="Analisi Predictiu")
st.sidebar.header("Analisi Predictiu")

st.title("🔮 Anàlisi Predictiu — Regressió Múltiple")

# -----------------------------
# 1. CARREGAR DATAFRAME
# -----------------------------

df= pd.read_csv("./dat/output/videojocsCat.csv", sep =";")
df= df.set_index("Any")
df["Pujada_Inversio_Absoluta"] = (
    df["Pujada_Inversio_Absoluta"]
    .str.replace(",", ".", regex=False)
    .astype(float)
)


# -----------------------------
# 2. SELECCIÓ DE VARIABLE OBJECTIU
# -----------------------------
st.subheader("1️⃣ Selecciona la variable objectiu")

target = st.selectbox(
    "Variable a predir:",
    df.columns,
)

# Variables explicatives = totes menys la objectiu
features = [col for col in df.columns if col != target]

st.write("Variables explicatives utilitzades:", features)

# -----------------------------
# 3. ENTRENAR MODEL
# -----------------------------
X = df[features]
y = df[target]

model = LinearRegression()
model.fit(X, y)

# -----------------------------
# 4. PREDICCIÓ FUTURA (2025–2030)
# -----------------------------
st.subheader("Predicció futura (2025–2030)")

anys_futurs = np.arange(2025, 2031)

# Projecció simple basada en tendències lineals
df_futur = pd.DataFrame(index=anys_futurs)

for col in features:
    df_futur[col] = np.linspace(df[col].iloc[-1], df[col].iloc[-1] * 1.25, len(anys_futurs))

prediccions = model.predict(df_futur)
st.dataframe(df_futur)
# -----------------------------
# 5. GRÀFIC
# -----------------------------
st.subheader("Gràfic de predicció")

colors = px.colors.sequential.Viridis

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df.index,
    y=df[target],
    mode="lines+markers",
    name="Dades reals",
    line=dict(color=colors[3])
))

fig.add_trace(go.Scatter(
    x=anys_futurs,
    y=prediccions,
    mode="lines+markers",
    name="Predicció",
    line=dict(color=colors[-2], dash="dash")
))

fig.update_layout(
    title=f"Predicció de {target} (Regressió múltiple)",
    xaxis_title="Any",
    yaxis_title=target
)

st.plotly_chart(fig, use_container_width=True)


# -----------------------------
# 6. COEFICIENTS DEL MODEL
# -----------------------------
st.subheader("Coeficients del model")

coef_df = pd.DataFrame({
    "Variable": features,
    "Coeficient": model.coef_
})

st.dataframe(coef_df)




