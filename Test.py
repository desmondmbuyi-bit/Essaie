import requests

API_URL = "https://ton-api-fastapi.onrender.com" # L'URL après déploiement

def lancer_logiciel():
    print("--- BIENVENUE DANS LE LOGICIEL ---")
    license_key = input("Veuillez entrer votre clé de licence : ")

    # Requête vers ton API FastAPI
    try:
        response = requests.get(f"{API_URL}/verify/{license_key}")
        result = response.json()

        if response.status_code == 200 and result["status"] == "success":
            print(f"✅ Accès accordé ! Bonjour {license_key}")
            print(f"Données récupérées : {result['user_data']}")
            # Ici, ton logiciel continue son exécution...
        else:
            print(f"❌ Accès refusé : {result.get('detail', 'Clé inconnue')}")
            
    except Exception as e:
        print(f"Erreur de connexion au serveur : {e}")

if __name__ == "__main__":
    lancer_logiciel()