import streamlit as st

st.set_page_config(page_title="Conclusions")
st.sidebar.header("Conclusions")

st.title("📋 Conclusions")

st.space('small')

st.write("""Després de realitzar l'estudi de les dades dels últims anys i veient els resultats dels analisis descriptiu i predictiu, podem arrribar a les següents conclusions:
""")

st.space('small')
st.markdown(
    """
    <div style="
        background-color:#f1faee;
        padding:15px;
        border-radius:10px;
        border:2px solid #a8dadc;
        margin-top:10px;
    ">
        <div style="
            font-size:18px;
            font-weight:bold;
            color:#1d3557;
            margin-bottom:8px;
            text-decoration: underline;
        ">
            Facturació
        </div>
        <p style="font-size:16px; color:#1d3557; margin:0;">
            La facturació en el sector del videojoc a Catalunya continuarà pujant, com ho ha anat fent en els anys anteriors.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


st.space('small')

st.markdown(
    """
    <div style="
        background-color:#EFBAEF;
        padding:15px;
        border-radius:10px;
        border:2px solid #a8dadc;
        margin-top:10px;
        font-size:16px;
    ">
        <div style="
                font-size:18px;
                font-weight:bold;
                color:#1d3557;
                margin-bottom:8px;
                text-decoration: underline;
            ">
                Treballadors i estudis
        </div>
        <p style="font-size:16px; color:#1d3557; margin:0;">
            El nombre de treballadors i estudis s'estancarà el 2025 i continuarà augmentant al llarg dels pròxims anys.
        </p>
    </div>
    """,
    unsafe_allow_html=True)

st.space('small')

st.markdown(
    """
    <div style="
        background-color:#afebf0;
        padding:15px;
        border-radius:10px;
        border:2px solid #a8dadc;
        margin-top:10px;
        font-size:16px;
    ">
        <div style="
                font-size:18px;
                font-weight:bold;
                color:#1d3557;
                margin-bottom:8px;
                text-decoration: underline;
            ">
            Producció de Videojocs
        </div>
        <p style="font-size:16px; color:#1d3557; margin:0;">
            El nombre de videojocs produits a Catalunya pujarà progresivament en els propers anys
        </p>
    </div>
    """,
    unsafe_allow_html=True)


st.space('small')

st.markdown(
    """
    <div style="
        background-color:#efb9b9;
        padding:15px;
        border-radius:10px;
        border:2px solid #a8dadc;
        margin-top:10px;
        font-size:16px;
    ">
        <div style="
                font-size:18px;
                font-weight:bold;
                color:#1d3557;
                margin-bottom:8px;
                text-decoration: underline;
            ">
            Inversió
        </div>
        <p style="font-size:16px; color:#1d3557; margin:0;">
            L'inversió captada de l'extranger continuarà pujant, tot i que en un percentatge menor
        </p>
    </div>
    """,
    unsafe_allow_html=True)

st.space('small')

st.markdown(
    """
    <div style="
        background-color:#ffffe5;
        padding:15px;
        border-radius:10px;
        border:2px solid #a8dadc;
        margin-top:10px;
        font-size:16px;
    ">
         <div style="
                font-size:18px;
                font-weight:bold;
                color:#1d3557;
                margin-bottom:8px;
                text-decoration: underline;
            ">
                Gènere més factible
         </div>
         <p style="font-size:16px; color:#1d3557; margin:0;">
         El gènere de videojoc més demandat al llarg de tots els anys estudiats i que, per tant, resulta més factible económicament es el d'acció, seguit per el shooter i els jocs d'esports.</strong>
        </p>
     </div>
    """,
    unsafe_allow_html=True)

st.space('small')

st.write("Aquestes conclusions son extretes del estudi realitzat, però la part predictiva necesita comprobació per confirmar que els resultats s'ajusten a la realitat. No he aconseguit trobar dades reals del 2025 per contrastar.")
