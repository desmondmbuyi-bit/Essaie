import streamlit as st
from supabase import create_client
from datetime import datetime, timedelta

URL = "https://icnlaumwdyrebbzmexiu.supabase.co"
KEY = "sb_publishable_5JQlhyKV7IO5gLjMDMRxfA_bs2FMTGd"
supabase = create_client(URL, KEY)

st.title("Admin Dashboard v2")

# 1. FORMULAIRE D'AJOUT (avec 30 jours par défaut)
with st.expander("Créer une licence (30 jours)"):
    email = st.text_input("Email client")
    key = st.text_input("Clé de licence")
    if st.button("Générer la licence"):
        # Calcul de la date d'expiration (+30 jours)
        expiration_date = (datetime.now() + timedelta(days=30)).isoformat()
        
        supabase.table("clients").insert({
            "email": email,
            "license_key": key,
            "is_active": True,
            "expires_at": expiration_date
        }).execute()
        st.success(f"Licence créée ! Expire le : {expiration_date}")

# 2. LISTE ET ACTIONS (Activer/Désactiver)
st.subheader("Gestion des accès")
res = supabase.table("clients").select("*").execute()
for client in res.data:
    col1, col2, col3, col4 = st.columns([3, 2, 2, 2])
    
    with col1:
        st.write(f"**{client['email']}** ({client['license_key']})")
    with col2:
        status = "✅ Actif" if client['is_active'] else "❌ Coupé"
        st.write(status)
    with col3:
        # Bouton pour Inverser le statut
        if st.button("Basculer", key=f"btn_{client['id']}"):
            new_status = not client['is_active']
            supabase.table("clients").update({"is_active": new_status}).eq("id", client['id']).execute()
            st.rerun()
    with col4:
        st.write(f"Expire le: {client['expires_at'][:10] if client['expires_at'] else 'Jamais'}")
