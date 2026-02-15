import streamlit as st
from supabase import create_client

# Configuration Supabase
URL = "https://icnlaumwdyrebbzmexiu.supabase.co"
KEY = "sb_publishable_5JQlhyKV7IO5gLjMDMRxfA_bs2FMTGd"
supabase = create_client(URL, KEY)

st.title("👨‍💻 Admin : Gestion des Clients")

# Récupérer les données
response = supabase.table("clients").select("*").execute()
clients = response.data

st.metric("Nombre de clients", len(clients))

# Affichage sous forme de tableau
st.subheader("Liste des accès")
st.table(clients)

# Formulaire pour ajouter un client
with st.expander("Ajouter un nouveau client"):
    new_email = st.text_input("Email")
    new_key = st.text_input("Clé de licence")
    if st.button("Valider"):
        supabase.table("clients").insert({"email": new_email, "license_key": new_key, "is_active": True}).execute()
        st.success("Client ajouté !")
        st.rerun()