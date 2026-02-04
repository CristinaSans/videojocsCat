import streamlit as st

st.set_page_config(
    page_title="Analisi sector videojocs a catalunya",
)

st.markdown(
    "<h1 style='text-align:center; color:#e63946; font-size:60px; font-weight:bold;'>"
    "Anàlisi del sector dels videojocs a Catalunya"
    "</h1>",
    unsafe_allow_html=True
)

st.space(size="large")
st.image("./dat/GRIS-Portada.jpg", caption="portada del videojoc Gris de Nomada Studio,", use_container_width=True)
st.space(size="large")

st.header("**Realitzat per:**")
st.subheader("_Cristina Sans, el 4 de Febrer de 2026_")

