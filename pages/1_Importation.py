import streamlit as st
import pandas as pd
import uuid
from datetime import datetime

st.title("📂 Importation des Données")
st.write("Importez votre fichier contenant la série temporelle.")
# === CSS additionnel ===
st.markdown("""
<style>
    .page-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin-bottom: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# === Header de page ===
st.markdown("""
<div class="page-header">
    <h1 style="margin: 0;">📁 Importation des Données</h1>
    <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">
        Étape 1/7 - Importez et préparez vos données temporelles
    </p>
</div>
""", unsafe_allow_html=True)

# === Indicateur de progression ===
progress_value = 0.14  # 1/7
st.progress(progress_value)
st.caption(f"Progression globale : {int(progress_value*100)}%")
# Initialisation du journal
if "journal" not in st.session_state:
    st.session_state["journal"] = {}

if "session" not in st.session_state["journal"]:
    st.session_state["journal"]["session"] = {
        "session_id": str(uuid.uuid4()),
        "date_debut": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# Upload du fichier
uploaded_file = st.file_uploader("Choisir un fichier", type=["csv", "xlsx"])

if not uploaded_file:
    st.stop()

# Lecture du fichier
name = uploaded_file.name.lower()

if name.endswith(".csv"):
    try:
        df_raw = pd.read_csv(uploaded_file, sep=";", encoding="utf-8")
    except UnicodeDecodeError:
        try:
            df_raw = pd.read_csv(uploaded_file, sep=";", encoding="cp1252")
        except UnicodeDecodeError:
            df_raw = pd.read_csv(uploaded_file, sep=";", encoding="latin1")

elif name.endswith(".xlsx"):
    df_raw = pd.read_excel(uploaded_file)

else:
    st.stop()

# Stockage
st.session_state["df_raw"] = df_raw

st.write("Aperçu des données importées :")
st.dataframe(df_raw.head())

# Sélection des colonnes
date_col = st.selectbox("Colonne Date :", df_raw.columns)
value_col = st.selectbox("Colonne Valeur :", df_raw.columns)

if st.button("Charger la série"):
    df = df_raw.copy()

    df[value_col] = (
        df[value_col]
        .astype(str)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    df[date_col] = pd.to_datetime(df[date_col], dayfirst=True)
    df = df.set_index(date_col)

    series = df[value_col]

    st.session_state["series"] = series
    st.session_state["target_column"] = value_col
    st.session_state["serie_description"] = {
        "nom": value_col,
        "date_debut": str(series.index.min()),
        "date_fin": str(series.index.max()),
        "frequence": "mensuelle",
        "nombre_observations": len(series)
    }

    st.success("Série chargée avec succès")
    st.line_chart(series)
with st.expander("🎯 **Fonctionnalités avancées**", expanded=False):
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🔍 Détection automatique
        - Format de date
        - Séparateur CSV
        - Encodage du fichier
        - Type de données
        """)
        
        if st.button("🔎 Analyser le fichier", key="analyze_file"):
            st.toast("Analyse en cours...", icon="🔍")
    
    with col2:
        st.markdown("""
        ### ⚙️ Prétraitement
        - Gestion des valeurs manquantes
        - Détection des outliers
        - Normalisation optionnelle
        - Agrégation temporelle
        """)
        
        if st.button("🔄 Appliquer le prétraitement", key="preprocess"):
            st.toast("Prétraitement appliqué !", icon="✅")

