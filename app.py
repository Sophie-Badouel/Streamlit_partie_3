import streamlit as st
import pandas as pd

# Config de ma page
st.set_page_config(page_title="Mon Application", layout="wide")

#les données
def load_users():
    try:
        return pd.read_csv('users.csv')
    except FileNotFoundError:
        st.error("Le fichier users.csv est introuvable.")
        return pd.DataFrame()

#les variables
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = ''

#le login
def login_page():
    st.title("")  #espace
    
    with col2:
        #cadre pour formulaire
        with st.container(border=True):
            st.subheader("Login")
            
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            
            if st.button("Login"):
                df = load_users()
                
                if not df.empty:
                    #vérif simple (username et mdp)
                    user_match = df[(df['name'] == username) & (df['password'] == password)]
                    
                    if not username or not password:
                        st.warning("Les champs username et mot de passe doivent être remplis")
                    elif not user_match.empty:
                        st.session_state['logged_in'] = True
                        st.session_state['username'] = username
                        st.rerun() #refresh la page pour afficher le contenu
                    else:
                        st.error("Nom d'utilisateur ou mot de passe incorrect")

#logout
def logout():
    st.session_state['logged_in'] = False
    st.session_state['username'] = ''
    st.rerun()

#accueil
def home_page():
    st.title("haha c'est toi... ah oui... Bienvenue")
    #image d'arrivée
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTJ5eXpmZ2lsZmNwYXRvazd2OWk3ampnYWkzZHRycXNvdDRtMjkxZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gGFKnKYbgBVM4/giphy.gif", width=600)

#album
def album_page():
    st.title("Bienvenue dans l'album des pui pui 🐹")
    
    img1 = "https://i.pinimg.com/736x/ea/d9/51/ead9512ffefaf746ee2ea842d7f03264.jpg"
    img2 = "https://i.pinimg.com/1200x/ce/82/ba/ce82ba50636e1aea19855a88fca613dc.jpg"
    img3 = "https://i.pinimg.com/736x/b9/d9/b6/b9d9b635220e38b1488f59c87f9a3652.jpg"
    
    #une seule ligne (3 colonnes)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image(img1, caption="pui pui nerd ☝️🤓")
    with col2:
        st.image(img2, caption="pui pui dangereux 🔪")
    with col3:
        st.image(img3, caption="pui pui élégant 🎩")

#main
if not st.session_state['logged_in']:
    login_page()
else:
    #barre latérale
    with st.sidebar:
        #bouton déconnexion en haut
        if st.button("Déconnexion"):
            logout()
        
        st.markdown(f"### Bienvenue *{st.session_state['username']}*")
        st.write("---") #ligne de séparation
        
        #menu de navigation
        menu_choice = st.radio("Navigation", ["🌿 Accueil", "🐹 Les photos des pui pui"], label_visibility="collapsed")

    #affichage
    if menu_choice == "🌿 Accueil":
        home_page()
    elif menu_choice == "🐹 Les photos des pui pui":
        album_page()