#!/bin/bash

# Installation des dépendances
pip install -r requirements.txt

# Création des dossiers nécessaires
mkdir -p pages
mkdir -p assets

# Copie des pages existantes
cp *.py pages/ 2>/dev/null || true

# Message de succès
echo "✅ Installation terminée !"
echo "🎯 Pour démarrer l'application : streamlit run app.py"