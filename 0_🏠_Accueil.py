import streamlit as st
import sys
import os
from pathlib import Path

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
        /* Style général */
        .main {
            padding: 2rem;
        }
        
        /* Header personnalisé */
        .header-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            color: white;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }
        
        .authors {
            font-size: 1.2rem;
            margin-top: 0.5rem;
            opacity: 0.9;
            font-weight: 500;
        }
        
        /* Cards */
        .card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
            border-left: 4px solid #667eea;
        }
        
        /* Boutons */
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 0.5rem 2rem;
            border-radius: 25px;
            font-weight: 600;
            transition: all 0.3s;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        
        /* Metrics */
        .metric-card {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
        }
        
        /* Sidebar */
        .sidebar .sidebar-content {
            background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
        }
        
        /* Progress bar */
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 2rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            background-color: #f0f2f6;
            border-radius: 5px 5px 0px 0px;
            padding: 10px 20px;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: #667eea;
            color: white;
        }
        
        /* Dataframes */
        .dataframe {
            border: none !important;
        }
        
        /* Success/Warning/Error boxes */
        .stAlert {
            border-radius: 10px;
            border: none;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
            color: #666;
            border-top: 1px solid #eee;
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
            <p>Étudiantes en Master ROMARIN, En se basant sur ce qu'on a appris en Méthodes de prévision. Ce projet représente notre travail 
            approfondi sur les méthodes de prévision temporelle.</p>
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
        st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <div style="
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                width: 60px;
                height: 60px;
                border-radius: 50%;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                font-size: 24px;
                color: white;
                margin-bottom: 10px;
            ">
                📊
            </div>
            <h3 style="margin: 0;">Navigation</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Menu de navigation stylisé
        st.markdown("### 🗂️ Étapes du projet")
        
        # Indicateur de progression (simulé)
        st.progress(0)
        
        st.markdown("""
        <div style="margin: 1.5rem 0;">
            <a href="/?page=1" style="text-decoration: none; color: inherit;">
                <div style="
                    padding: 0.8rem;
                    border-radius: 10px;
                    margin: 0.3rem 0;
                    background: #f0f2f6;
                    transition: all 0.3s;
                    border-left: 4px solid #667eea;
                ">
                    <strong>1. 📁 Importation</strong>
                </div>
            </a>
            
            <a href="/?page=2" style="text-decoration: none; color: inherit;">
                <div style="
                    padding: 0.8rem;
                    border-radius: 10px;
                    margin: 0.3rem 0;
                    background: #f0f2f6;
                    transition: all 0.3s;
                    border-left: 4px solid #667eea;
                ">
                    <strong>2. 📊 Analyse Exploratoire</strong>
                </div>
            </a>
            
            <a href="/?page=3" style="text-decoration: none; color: inherit;">
                <div style="
                    padding: 0.8rem;
                    border-radius: 10px;
                    margin: 0.3rem 0;
                    background: #f0f2f6;
                    transition: all 0.3s;
                    border-left: 4px solid #667eea;
                ">
                    <strong>3. 📈 Tests de Stationnarité</strong>
                </div>
            </a>
            
            <a href="/?page=4" style="text-decoration: none; color: inherit;">
                <div style="
                    padding: 0.8rem;
                    border-radius: 10px;
                    margin: 0.3rem 0;
                    background: #f0f2f6;
                    transition: all 0.3s;
                    border-left: 4px solid #667eea;
                ">
                    <strong>4. 🧮 Modèles Classiques</strong>
                </div>
            </a>
            
            <a href="/?page=5" style="text-decoration: none; color: inherit;">
                <div style="
                    padding: 0.8rem;
                    border-radius: 10px;
                    margin: 0.3rem 0;
                    background: #f0f2f6;
                    transition: all 0.3s;
                    border-left: 4px solid #667eea;
                ">
                    <strong>5. 🤖 Modèles & Prévisions</strong>
                </div>
            </a>
            
            <a href="/?page=6" style="text-decoration: none; color: inherit;">
                <div style="
                    padding: 0.8rem;
                    border-radius: 10px;
                    margin: 0.3rem 0;
                    background: #f0f2f6;
                    transition: all 0.3s;
                    border-left: 4px solid #667eea;
                ">
                    <strong>6. 🧪 Tests & Validation</strong>
                </div>
            </a>
            
            <a href="/?page=7" style="text-decoration: none; color: inherit;">
                <div style="
                    padding: 0.8rem;
                    border-radius: 10px;
                    margin: 0.3rem 0;
                    background: #f0f2f6;
                    transition: all 0.3s;
                    border-left: 4px solid #667eea;
                ">
                    <strong>7. 📤 Export & Logs</strong>
                </div>
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # Informations de session
        st.markdown("---")
        st.markdown("### 📊 Session actuelle")
        
        if "journal" in st.session_state and "session" in st.session_state["journal"]:
            session_info = st.session_state["journal"]["session"]
            st.markdown(f"**ID Session :** `{session_info['session_id'][:8]}...`")
            st.markdown(f"**Débutée le :** {session_info['date_debut']}")
        
        # Bouton de réinitialisation
        if st.button("🔄 Nouvelle session", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

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