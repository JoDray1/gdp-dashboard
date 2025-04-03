import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Analyse d'un Fonds ESG - Critères Extra-Financiers")

# Informations générales sur le fonds
st.header("Informations du Fonds")
st.write("""
Nom du Fonds : Fonds Durable XYZ
Type : ETF
Secteurs ciblés : Énergies renouvelables, technologies propres, santé publique.
""")

# Données fictives du portefeuille
data = {
    "Secteur": ["Énergies renouvelables", "Technologies propres", "Santé publique", "Éducation"],
    "Allocation (%)": [40, 25, 20, 15],
    "Impact Environnemental (E)": [90, 80, 70, 60],
    "Impact Social (S)": [75, 85, 95, 90],
    "Impact Gouvernance (G)": [88, 85, 92, 80]
}
df = pd.DataFrame(data)

# Afficher les données sous forme de tableau
st.subheader("Composition et Impact du Portefeuille")
st.dataframe(df)

# Graphique : Allocation par secteur
st.subheader("Répartition des Secteurs")
fig, ax = plt.subplots()
ax.pie(df["Allocation (%)"], labels=df["Secteur"], autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Assure que le graphique est circulaire
st.pyplot(fig)

# Graphique : Score ESG par secteur
st.subheader("Scores ESG par Secteur")
fig, ax = plt.subplots()
ax.bar(df["Secteur"], df["Impact Environnemental (E)"], label="Environnemental (E)", color='green')
ax.bar(df["Secteur"], df["Impact Social (S)"], label="Social (S)", color='blue')
ax.bar(df["Secteur"], df["Impact Gouvernance (G)"], label="Gouvernance (G)", color='orange')
ax.set_ylabel("Score ESG")
ax.legend()
st.pyplot(fig)

# Message final
st.success("Voici un aperçu complet du Fonds Durable XYZ basé sur des critères ESG.")