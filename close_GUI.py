import customtkinter    # Module pour le GUI

import json # Module pour interagir avec le fichier json

app = customtkinter.CTk()    # Instanciation de la classe

app.geometry('360x350')    # Définition de la taille de la fenêtre

app.resizable(False, False)    # Désactivation de la redimensionnement de la fenêtre

app.title('CTW-J')    # Nom de la fenêtre

app.iconbitmap("window-close-regular-24.ico")    # Icône de la fenêtre

font_error = customtkinter.CTkFont(size= 11)    # Taille pour le message d'erreur 

label_error = customtkinter.CTkLabel(app, text='', width=40, height=28, fg_color='transparent', font= font_error, text_color= "red")    # Message d'erreur initialement vide
label_error.place(x=85, y=0)

entry = customtkinter.CTkEntry(app, placeholder_text='App name', width=140, height=28, corner_radius= 1, border_width= 1)    # Entrée de l'utilisateur
entry.place(x = 85, y = 20,)

def add():    # Fonction rattachée au bouton add
    
    with open(r'C:\Users\pc\Desktop\coding\Projet_python\fermetture de fenetre\applications.json', 'r') as data:    # Ouverture du fichier json en mode read
        
        applications = json.load(data)    # Chargement du fichier json en dictionnaire
    
    new_app = entry.get()    # Récupération de l'entrée de l'utilisateur
    
    if new_app in applications.get("applications"):    # Vérification de la présence de l'application dans le fichier json
        
        label_error.configure(text = "This app is already registered")    # Message d'erreur
    
    else:
        
        label_error.configure(text = "")    # Message d'erreur vide 


add = customtkinter.CTkButton(app, text='Add', width=40, height=28, corner_radius= 1, command = add)    # Bouton ajouter
add.place(x = 235, y = 20)

app.mainloop()    # Méthode pour l'exécution de l'interface