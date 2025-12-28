import streamlit as st
import sys
import os
import base64
from pathlib import Path
def get_logo_base64():
    """Trouve et convertit le logo en base64"""
    try:
        # Chemins possibles
        possible_paths = [
            "assets/logo.png",
            "static/logo.png", 
            "logo.png",
            "./assets/logo.png",
            "./static/logo.png",
            "./logo.png"
        ]
        
        # Vérifier chaque chemin
        for path_str in possible_paths:
            path = Path(path_str)
            if path.exists() and path.is_file():
                with open(path, "rb") as f:
                    return base64.b64encode(f.read()).decode()
        
        # Si aucun fichier trouvé
        return None
        
    except Exception as e:
        print(f"Erreur dans get_logo_base64: {e}")
        return None
# Configuration de la page
st.set_page_config(
    page_title="📈 StatAnalytica",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/your-repo',
        'Report a bug': "https://github.com/your-repo/issues",
        'About': "### Master ROMARIN - Projet de Prévision des Séries Temporelles\n\n**Réalisé par :**\n- Dounia Belhocine\n- Hadil Bachir\n\n© 2024 - Tous droits réservés"
    }
)

# === Configuration des chemins ===
ROOT = Path(__file__).parent
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

# === CSS personnalisé ===
def load_css():
    st.markdown("""
    <style>
        /* ===========================================
           VARIABLES CSS - ADAPTATIVES POUR LES DEUX THÈMES
           =========================================== */
        
        /* Thème clair par défaut */
        :root {
            /* Couleurs principales */
            --primary: #4361ee;
            --primary-dark: #3a0ca3;
            --primary-light: #4cc9f0;
            --accent: #7209b7;
            --accent-light: #f72585;
            --success: #38b000;
            --warning: #ff9e00;
            --danger: #e63946;
            
            /* Couleurs d'interface */
            --dark: #1a1a2e;
            --light: #f8f9fa;
            --gray: #6c757d;
            
            /* Backgrounds */
            --bg-primary: white;
            --bg-secondary: #f8f9ff;
            
            /* Textes */
            --text-primary: #1a1a2e;
            --text-secondary: #6c757d;
            
            /* Bordures et cartes */
            --border-color: #e0e0e0;
            --card-bg: white;
            
            /* Ombres */
            --shadow-color: rgba(0,0,0,0.1);
            --shadow-light: rgba(0,0,0,0.05);
            
            /* Gradients spécifiques */
            --sidebar-bg: linear-gradient(180deg, #ffffff 0%, #f8f9ff 100%);
            --header-gradient: linear-gradient(135deg, #4361ee 0%, #3a0ca3 100%);
            --metric-gradient: linear-gradient(135deg, #4cc9f0 0%, #4361ee 100%);
        }
        
        /* ===========================================
           DÉTECTION AUTOMATIQUE DU MODE SOMBRE
           =========================================== */
        
        /* Détection système */
        @media (prefers-color-scheme: dark) {
            :root {
                /* Couleurs principales (plus claires pour contraste) */
                --primary: #5a7dff;
                --primary-dark: #4d12d1;
                --primary-light: #6bd4ff;
                --accent: #8a1fd9;
                --accent-light: #ff4da6;
                --success: #4cd500;
                --warning: #ffb347;
                --danger: #ff6b6b;
                
                /* Couleurs d'interface (inversées) */
                --dark: #e0e0e0;
                --light: #2d2d44;
                --gray: #a0a0a0;
                
                /* Backgrounds (fond sombre) */
                --bg-primary: #1a1a2e;
                --bg-secondary: #2d2d44;
                
                /* Textes (clair sur fond sombre) */
                --text-primary: #f0f0f0;
                --text-secondary: #b0b0b0;
                
                /* Bordures et cartes */
                --border-color: #444444;
                --card-bg: #2d2d44;
                
                /* Ombres (plus prononcées) */
                --shadow-color: rgba(0,0,0,0.3);
                --shadow-light: rgba(0,0,0,0.2);
                
                /* Gradients adaptés */
                --sidebar-bg: linear-gradient(180deg, #2d2d44 0%, #25253d 100%);
                --header-gradient: linear-gradient(135deg, #5a7dff 0%, #4d12d1 100%);
                --metric-gradient: linear-gradient(135deg, #6bd4ff 0%, #5a7dff 100%);
            }
        }
        
        /* Forçage par Streamlit (très important !) */
        [data-theme="dark"] {
            /* Couleurs principales */
            --primary: #5a7dff !important;
            --primary-dark: #4d12d1 !important;
            --primary-light: #6bd4ff !important;
            --accent: #8a1fd9 !important;
            --accent-light: #ff4da6 !important;
            --success: #4cd500 !important;
            --warning: #ffb347 !important;
            --danger: #ff6b6b !important;
            
            /* Couleurs d'interface */
            --dark: #e0e0e0 !important;
            --light: #2d2d44 !important;
            --gray: #a0a0a0 !important;
            
            /* Backgrounds */
            --bg-primary: #1a1a2e !important;
            --bg-secondary: #2d2d44 !important;
            
            /* Textes */
            --text-primary: #f0f0f0 !important;
            --text-secondary: #b0b0b0 !important;
            
            /* Bordures et cartes */
            --border-color: #444444 !important;
            --card-bg: #2d2d44 !important;
            
            /* Ombres */
            --shadow-color: rgba(0,0,0,0.3) !important;
            --shadow-light: rgba(0,0,0,0.2) !important;
            
            /* Gradients */
            --sidebar-bg: linear-gradient(180deg, #2d2d44 0%, #25253d 100%) !important;
            --header-gradient: linear-gradient(135deg, #5a7dff 0%, #4d12d1 100%) !important;
            --metric-gradient: linear-gradient(135deg, #6bd4ff 0%, #5a7dff 100%) !important;
        }
        
        /* ===========================================
           STYLE GÉNÉRAL - COMPLÈTEMENT ADAPTATIF
           =========================================== */
        
        /* Application principale */
        .main {
            padding: 2rem;
            background: var(--bg-secondary);
            min-height: 100vh;
            color: var(--text-primary);
            transition: all 0.3s ease;
        }
        
        /* Streamlit app container */
        .stApp {
            background: var(--bg-secondary) !important;
            color: var(--text-primary) !important;
        }
        
        /* ===========================================
           HEADER STATANALYTICA - Reste toujours visible
           =========================================== */
        
        .header-container {
            background: var(--header-gradient);
            padding: 2rem;
            border-radius: 20px;
            margin-bottom: 2rem;
            color: white !important; /* Force blanc même en mode sombre */
            box-shadow: 0 10px 30px var(--shadow-color);
            border: 3px solid rgba(255, 255, 255, 0.1);
            position: relative;
            overflow: hidden;
        }
        
        /* Effet brillant animé */
        .header-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, transparent 30%, rgba(255, 255, 255, 0.1) 50%, transparent 70%);
            animation: shine 3s infinite;
        }
        
        @keyframes shine {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }
        
        .authors {
            font-size: 1.2rem;
            margin-top: 0.5rem;
            opacity: 0.9;
            font-weight: 500;
            background: rgba(255, 255, 255, 0.15);
            padding: 8px 20px;
            border-radius: 50px;
            display: inline-block;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: white !important; /* Force blanc */
        }
        
        /* ===========================================
           CARDS - Adaptatives
           =========================================== */
        
        .card {
            background: var(--card-bg);
            padding: 1.8rem;
            border-radius: 15px;
            box-shadow: 0 5px 20px var(--shadow-color);
            margin-bottom: 1.5rem;
            border-left: 5px solid var(--primary);
            transition: all 0.3s ease;
            color: var(--text-primary);
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px var(--shadow-color);
            border-left: 5px solid var(--accent);
        }
        
        /* Texte dans les cartes (toujours visible) */
        .card h1, .card h2, .card h3, .card h4, 
        .card h5, .card h6, .card p, .card li, 
        .card span, .card div:not(.stButton) {
            color: var(--text-primary) !important;
        }
        
        /* ===========================================
           BOUTONS - Restent colorés
           =========================================== */
        
        .stButton > button {
            background: var(--header-gradient);
            color: white !important;
            border: none;
            padding: 0.7rem 2.2rem;
            border-radius: 50px;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(67, 97, 238, 0.3);
            position: relative;
            overflow: hidden;
        }
        
        .stButton > button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: 0.5s;
        }
        
        .stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(67, 97, 238, 0.4);
        }
        
        .stButton > button:hover::before {
            left: 100%;
        }
        
        /* ===========================================
           METRICS CARDS - Adaptatives
           =========================================== */
        
        .metric-card {
            background: var(--metric-gradient);
            color: white !important;
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 5px 15px var(--shadow-color);
            transition: transform 0.3s;
            border: 2px solid rgba(255, 255, 255, 0.3);
        }
        
        .metric-card:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 25px var(--shadow-color);
        }
        
        /* ===========================================
           SIDEBAR - Adaptative
           =========================================== */
        
        .sidebar .sidebar-content {
            background: var(--sidebar-bg) !important;
            border-right: 3px solid var(--primary-light);
            box-shadow: 5px 0 15px var(--shadow-light);
            color: var(--text-primary) !important;
        }
        
        /* Texte dans la sidebar */
        .sidebar .sidebar-content * {
            color: var(--text-primary) !important;
        }
        
        /* ===========================================
           PROGRESS BAR - Adaptative
           =========================================== */
        
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, var(--primary) 0%, var(--accent) 100%);
            border-radius: 10px;
        }
        
        /* ===========================================
           TABS - Adaptatives
           =========================================== */
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 0;
            background: var(--bg-secondary);
            padding: 5px;
            border-radius: 15px;
            box-shadow: inset 0 2px 10px var(--shadow-light);
        }
        
        .stTabs [data-baseweb="tab"] {
            background: transparent;
            border-radius: 10px;
            padding: 15px 25px;
            font-weight: 600;
            color: var(--text-primary) !important;
            transition: all 0.3s;
            border: 2px solid transparent;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background: rgba(67, 97, 238, 0.1);
            color: var(--primary) !important;
        }
        
        .stTabs [aria-selected="true"] {
            background: var(--header-gradient);
            color: white !important;
            box-shadow: 0 5px 15px var(--shadow-color);
            border: 2px solid rgba(255, 255, 255, 0.5);
        }
        
        /* ===========================================
           DATAFRAMES - Adaptatives
           =========================================== */
        
        .dataframe {
            border: none !important;
            border-radius: 10px !important;
            overflow: hidden !important;
            box-shadow: 0 5px 15px var(--shadow-light) !important;
            background: var(--card-bg) !important;
        }
        
        .dataframe thead {
            background: var(--header-gradient) !important;
            color: white !important;
        }
        
        .dataframe tbody tr:nth-child(even) {
            background-color: var(--bg-secondary) !important;
        }
        
        .dataframe tbody tr:hover {
            background-color: rgba(67, 97, 238, 0.1) !important;
        }
        
        .dataframe td, .dataframe th {
            color: var(--text-primary) !important;
            border-color: var(--border-color) !important;
        }
        
        /* ===========================================
           ALERTS - Adaptatives
           =========================================== */
        
        .stAlert {
            border-radius: 15px !important;
            border: none !important;
            box-shadow: 0 5px 15px var(--shadow-light) !important;
        }
        
        div[data-testid="stSuccess"] > div {
            background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%) !important;
            border-left: 5px solid var(--success) !important;
            color: #155724 !important;
        }
        
        div[data-testid="stWarning"] > div {
            background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%) !important;
            border-left: 5px solid var(--warning) !important;
            color: #856404 !important;
        }
        
        div[data-testid="stError"] > div {
            background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%) !important;
            border-left: 5px solid var(--danger) !important;
            color: #721c24 !important;
        }
        
        div[data-testid="stInfo"] > div {
            background: linear-gradient(135deg, #d1ecf1 0%, #bee5eb 100%) !important;
            border-left: 5px solid var(--primary-light) !important;
            color: #0c5460 !important;
        }
        
        /* ===========================================
           FOOTER - Adaptatif
           =========================================== */
        
        .footer {
            text-align: center;
            padding: 2.5rem;
            margin-top: 4rem;
            background: linear-gradient(135deg, rgba(255, 192, 203, 0.25) 0%, rgba(255, 182, 193, 0.25) 100%);
            color: var(--text-primary) !important;
            border-radius: 20px 20px 0 0;
            position: relative;
            overflow: hidden;
        }
        
        .footer::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--primary), var(--accent), var(--primary-light));
        }
        
        /* ===========================================
           BADGES - Adaptatifs
           =========================================== */
        
        .badge {
            display: inline-block;
            padding: 6px 14px;
            border-radius: 25px;
            font-size: 0.85rem;
            font-weight: 600;
            margin: 0 5px 10px 0;
            transition: all 0.3s;
            color: white !important;
        }
        
        .badge-primary {
            background: var(--header-gradient);
            box-shadow: 0 3px 10px var(--shadow-color);
        }
        
        .badge-success {
            background: linear-gradient(135deg, var(--success) 0%, #2b9348 100%);
            box-shadow: 0 3px 10px var(--shadow-color);
        }
        
        .badge-warning {
            background: linear-gradient(135deg, var(--warning) 0%, #ff8500 100%);
            box-shadow: 0 3px 10px var(--shadow-color);
        }
        
        .badge-danger {
            background: linear-gradient(135deg, var(--danger) 0%, #c1121f 100%);
            box-shadow: 0 3px 10px var(--shadow-color);
        }
        
        /* ===========================================
           INPUTS ET SÉLECTEURS - Adaptatifs
           =========================================== */
        
        .stSelectbox > div, .stTextInput > div, .stNumberInput > div, 
        .stDateInput > div, .stTextArea > div {
            border-radius: 10px !important;
            border: 2px solid var(--border-color) !important;
            transition: all 0.3s !important;
            background: var(--card-bg) !important;
            color: var(--text-primary) !important;
        }
        
        .stSelectbox > div:hover, .stTextInput > div:hover, 
        .stNumberInput > div:hover {
            border-color: var(--primary) !important;
            box-shadow: 0 0 0 3px rgba(67, 97, 238, 0.1) !important;
        }
        
        /* Labels des inputs */
        label, .stTextInput label, .stSelectbox label, 
        .stNumberInput label, .stDateInput label {
            color: var(--text-primary) !important;
        }
        
        /* Placeholder */
        input::placeholder, textarea::placeholder {
            color: var(--text-secondary) !important;
        }
        
        /* ===========================================
           SLIDERS - Adaptatifs
           =========================================== */
        
        .stSlider > div > div > div {
            background: linear-gradient(90deg, var(--primary) 0%, var(--primary-dark) 100%) !important;
        }
        
        .stSlider > div > div > div > div {
            background: var(--card-bg) !important;
            border: 3px solid var(--primary) !important;
            box-shadow: 0 2px 10px var(--shadow-color) !important;
        }
        
        /* ===========================================
           EXPANDERS - Adaptatifs
           =========================================== */
        
        .streamlit-expanderHeader {
            background: var(--bg-secondary) !important;
            border-radius: 10px !important;
            border: 2px solid var(--border-color) !important;
            font-weight: 600 !important;
            color: var(--text-primary) !important;
        }
        
        .streamlit-expanderHeader:hover {
            background: var(--card-bg) !important;
            border-color: var(--primary) !important;
        }
        
        /* ===========================================
           TABLEAUX DE DONNÉES - Adaptatifs
           =========================================== */
        
        [data-testid="stDataFrame"] {
            border-radius: 15px !important;
            overflow: hidden !important;
            box-shadow: 0 10px 30px var(--shadow-light) !important;
            background: var(--card-bg) !important;
        }
        
        /* ===========================================
           GRAPHIQUES - Adaptatifs
           =========================================== */
        
        .js-plotly-plot {
            border-radius: 15px !important;
            overflow: hidden !important;
            box-shadow: 0 5px 20px var(--shadow-light) !important;
            background: var(--card-bg) !important;
        }
        
        /* ===========================================
           RESPONSIVE DESIGN
           =========================================== */
        
        @media (max-width: 768px) {
            .main {
                padding: 1rem;
            }
            
            .header-container {
                padding: 1.5rem;
                border-radius: 15px;
            }
            
            .card {
                padding: 1.2rem;
            }
        }
        
        /* ===========================================
           ANIMATIONS
           =========================================== */
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .card, .metric-card {
            animation: fadeInUp 0.5s ease-out;
        }
        
        /* ===========================================
           SCROLLBAR PERSONNALISÉE
           =========================================== */
        
        ::-webkit-scrollbar {
            width: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background: var(--bg-secondary);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: var(--header-gradient);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, var(--primary-dark) 0%, var(--accent) 100%);
        }
        
        /* ===========================================
           TOOLTIPS - Adaptatifs
           =========================================== */
        
        .tooltip {
            position: relative;
            display: inline-block;
            border-bottom: 1px dotted var(--primary);
            cursor: help;
        }
        
        .tooltip .tooltiptext {
            visibility: hidden;
            width: 250px;
            background-color: var(--dark);
            color: var(--light) !important;
            text-align: center;
            border-radius: 10px;
            padding: 10px;
            position: absolute;
            z-index: 1;
            bottom: 125%;
            left: 50%;
            transform: translateX(-50%);
            opacity: 0;
            transition: opacity 0.3s;
            font-size: 0.9rem;
            box-shadow: 0 5px 15px var(--shadow-color);
        }
        
        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
        
        /* ===========================================
           SÉPARATEURS
           =========================================== */
        
        hr {
            border: none;
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--primary), transparent);
            margin: 2rem 0;
        }
        
        /* ===========================================
           CODE BLOCKS - Adaptatifs
           =========================================== */
        
        .stCodeBlock {
            border-radius: 10px !important;
            border: 2px solid var(--border-color) !important;
            background: var(--bg-secondary) !important;
            color: var(--text-primary) !important;
        }
        
        /* ===========================================
           IMAGES
           =========================================== */
        
        .stImage > img {
            border-radius: 15px !important;
            box-shadow: 0 10px 30px var(--shadow-light) !important;
            border: 3px solid var(--card-bg) !important;
        }
        
        /* ===========================================
           UTILISATION AVANCÉE (comme demandé)
           =========================================== */
        
        /* Effet de verre (glassmorphism) */
        .glass-card {
            background: rgba(255, 255, 255, 0.1) !important;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 8px 32px var(--shadow-color);
            color: var(--text-primary) !important;
        }
        
        [data-theme="dark"] .glass-card {
            background: rgba(45, 45, 68, 0.7) !important;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        /* Effet néon pour les titres */
        .neon-text {
            text-shadow: 
                0 0 5px var(--primary),
                0 0 10px var(--primary),
                0 0 20px var(--primary),
                0 0 40px var(--primary);
            color: white !important;
        }
        
        /* Animation de chargement */
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
        
        .pulse {
            animation: pulse 2s infinite;
        }
        
        /* Gradient animé */
        .gradient-bg {
            background: linear-gradient(-45deg, var(--primary), var(--primary-dark), var(--accent), var(--primary-light));
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* Effets de profondeur */
        .depth-1 { box-shadow: 0 1px 3px var(--shadow-color); }
        .depth-2 { box-shadow: 0 3px 6px var(--shadow-color); }
        .depth-3 { box-shadow: 0 10px 20px var(--shadow-color); }
        .depth-4 { box-shadow: 0 14px 28px var(--shadow-color); }
        .depth-5 { box-shadow: 0 19px 38px var(--shadow-color); }
        
        /* ===========================================
           GARANTIE DE VISIBILITÉ ABSOLUE
           =========================================== */
        
        /* S'assurer que TOUS les textes sont visibles */
        body, div, span, p, h1, h2, h3, h4, h5, h6, 
        li, td, th, a, small, strong, em, code, pre {
            color: var(--text-primary) !important;
        }
        
        /* Exceptions pour éléments spécifiques */
        .header-container *, 
        .stButton > button, 
        .metric-card *,
        .badge,
        .dataframe thead * {
            color: white !important;
        }
        
        /* Transition douce entre thèmes */
        * {
            transition: background-color 0.5s ease, 
                       color 0.5s ease, 
                       border-color 0.5s ease,
                       box-shadow 0.5s ease;
        }
        
        /* Override final pour Streamlit */
        .st-emotion-cache-1y4p8pa {
            background-color: var(--bg-secondary) !important;
            color: var(--text-primary) !important;
        }
        
        /* Tableaux générés par Streamlit */
        table {
            background-color: var(--card-bg) !important;
            color: var(--text-primary) !important;
        }
        
        table th {
            background-color: var(--primary) !important;
            color: white !important;
        }
        
        table td {
            color: var(--text-primary) !important;
            border-color: var(--border-color) !important;
        }
        
        /* Éléments de formulaire */
        input, select, textarea {
            background-color: var(--card-bg) !important;
            color: var(--text-primary) !important;
            border-color: var(--border-color) !important;
        }
        
        /* Désactiver la couleur bleue des liens en mode sombre */
        a {
            color: var(--primary) !important;
        }
        
        a:hover {
            color: var(--accent) !important;
        }
    </style>
    """, unsafe_allow_html=True)

# Charger le CSS
load_css()

# === Header avec logo et auteurs ===
def create_header():
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col1:
        # Vous pouvez ajouter votre logo ici
        st.markdown("""
        <div style="text-align: center;">
            <div style="
                width: 80px;
                height: 80px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 50%;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                font-size: 30px;
                color: white;
                margin-bottom: 10px;
            ">
                📈
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="header-container">
            <h1 style="margin: 0; font-size: 2.5rem; text-align: center;">
                StatAnalytica
            </h1>
            <p style="text-align: center; font-size: 1.2rem; margin-top: 0.5rem;">
                Plateforme avancée de prévision des séries temporelles
            </p>
            <div class="authors" style="text-align: center;">
                Par <strong>Dounia Belhocine</strong> & <strong>Hadil Bachir</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: right; padding-top: 1rem;">
            <div style="
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                padding: 8px 16px;
                border-radius: 20px;
                color: white;
                display: inline-block;
                font-weight: bold;
            ">
                Master ROMARIN
            </div>
        </div>
        """, unsafe_allow_html=True)

# === Page d'accueil ===
def main_page():
    create_header()
    
    st.markdown("---")
    
    # Introduction
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>🎯 Objectif du Projet</h3>
            <p>Cette application permet d'analyser et prévoir des séries temporelles 
            avec des méthodes classiques et avancées, en suivant une méthodologie complète.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3>📊 Méthodologie</h3>
            <ol>
                <li>Importation et nettoyage des données</li>
                <li>Analyse exploratoire (EDA)</li>
                <li>Tests de stationnarité</li>
                <li>Modélisation classique</li>
                <li>Modèles avancés (Holt-Winters)</li>
                <li>Validation et tests statistiques</li>
                <li>Export des résultats</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>🚀 Fonctionnalités Avancées</h3>
            <ul>
                <li><strong>Grid Search Automatique</strong> - Optimisation des paramètres</li>
                <li><strong>Intervalles de confiance</strong> - Bootstrap et méthodes analytiques</li>
                <li><strong>Optimisation bayésienne</strong> - Pour recherche efficace</li>
                <li><strong>Validation croisée</strong> - 70/30, 80/20, Rolling-Origin</li>
                <li><strong>Tests statistiques complets</strong> - Shapiro-Wilk, Ljung-Box</li>
                <li><strong>Journal d'exécution</strong> - Traçabilité complète</li>
                <li><strong>Export multi-format</strong> - CSV, JSON, ZIP</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Guide de démarrage
    with st.expander("📖 Guide de démarrage rapide", expanded=True):
        st.markdown("""
        1. **Importez vos données** dans l'onglet 📁 Importation
        2. **Explorez vos données** dans 📊 Analyse Exploratoire
        3. **Testez la stationnarité** dans 📈 Tests de Stationnarité
        4. **Appliquez les modèles classiques** dans 🧮 Modèles Classiques
        5. **Utilisez les modèles avancés** dans 🤖 Modèles & Prévisions
        6. **Validez vos modèles** dans 🧪 Tests & Validation
        7. **Exportez les résultats** dans 📤 Export & Logs
        """)
    
    # Métriques de progression
    st.markdown("### 📈 Progression du projet")
    
    # Simulation de progression (vous pouvez la remplacer par des vraies métriques)
    progress_cols = st.columns(4)
    
    with progress_cols[0]:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem;">7</div>
            <div>Étapes</div>
        </div>
        """, unsafe_allow_html=True)
    
    with progress_cols[1]:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem;">10+</div>
            <div>Modèles</div>
        </div>
        """, unsafe_allow_html=True)
    
    with progress_cols[2]:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem;">15+</div>
            <div>Métriques</div>
        </div>
        """, unsafe_allow_html=True)
    
    with progress_cols[3]:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem;">5+</div>
            <div>Tests statistiques</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Dernière section avec informations complémentaires
    col_info1, col_info2 = st.columns(2)
    
    with col_info1:
        st.markdown("""
        <div class="card">
            <h3>👥 À propos des auteurs</h3>
            <p><strong>Dounia Belhocine & Hadil Bachir</strong></p>
            <p>Étudiantes en Master 2 specialisées en Recherches Operationnelles Management 
            Risques et Négociations, avec un intérêt particulier pour l’analyse quantitative et la modélisation .</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_info2:
        st.markdown("""
        <div class="card">
            <h3>🔧 Technologies utilisées</h3>
            <p>• <strong>Streamlit</strong> - Interface utilisateur</p>
            <p>• <strong>Statsmodels</strong> - Modèles statistiques</p>
            <p>• <strong>Scikit-learn</strong> - Machine Learning</p>
            <p>• <strong>Scikit-optimize</strong> - Optimisation bayésienne</p>
            <p>• <strong>Pandas/Numpy</strong> - Manipulation de données</p>
            <p>• <strong>Matplotlib/Plotly</strong> - Visualisation</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>© 2025 - Projet académique - Master ROMARIN</p>
        <p>Développé avec ❤️ par Dounia Belhocine & Hadil Bachir pour Monsieur Chaabane </p>
        <p style="font-size: 0.9rem; color: #888;">
            Cette application est optimisée pour Streamlit Cloud
        </p>
    </div>
    """, unsafe_allow_html=True)

# === Page sidebar ===
def create_sidebar():
  with st.sidebar:
        # DÉFINIR logo_b64 AVANT de l'utiliser
        logo_b64 = get_logo_base64()
        
        # Afficher le logo
        if logo_b64 is not None and logo_b64 != "":
            # Avec logo
            st.markdown(f"""
            <!-- Logo avec image -->
            <div style="text-align: center; margin-bottom: 2rem;">
                <img src="data:image/png;base64,{logo_b64}" 
                     alt="StatAnalytica"
                     style="width: 80px; height: 80px; border-radius: 15px; margin-bottom: 10px;">
                <h3 style="margin: 0; color: #4361ee;">StatAnalytica</h3>
                <p style="margin: 5px 0 0 0; color: #6b7280; font-size: 0.9rem;">
                    Belhocine & Bachir
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Fallback sans logo
            st.markdown("""
            <!-- Logo fallback -->
            <div style="text-align: center; margin-bottom: 2rem;">
                <div style="
                    width: 80px; height: 80px; 
                    background: linear-gradient(135deg, #4361ee 0%, #3a0ca3 100%);
                    border-radius: 15px; 
                    display: inline-flex; 
                    align-items: center; 
                    justify-content: center;
                    margin-bottom: 10px;
                    font-size: 32px;
                    color: white;
                ">
                    📊
                </div>
                <h3 style="margin: 0; color: #4361ee;">StatAnalytica</h3>
                <p style="margin: 5px 0 0 0; color: #6b7280; font-size: 0.9rem;">
                    Advanced Statistical Analysis
                </p>
            </div>
            """, unsafe_allow_html=True)

# === Fonction principale ===
def main():
    create_sidebar()
    
    # Si nous sommes sur la page d'accueil
    if len(st.query_params) == 0:
        main_page()
    else:
        # Les autres pages seront gérées automatiquement par Streamlit
        st.markdown("## " + st.query_params.get("page", ""))

if __name__ == "__main__":

    main()












