import customtkinter    # Module pour le GUI

import psutil    # Module pour relever des informations relatifs aux processus actifs

import json # Module pour interagir avec le fichier json

app = customtkinter.CTk()    # Instanciation de la classe

app.geometry('360x350')    # Définition de la taille de la fenêtre

app.resizable(False, False)    # Désactivation de la redimensionnement de la fenêtre

app.title('CTW-J')    # Nom de la fenêtre

app.iconbitmap("window-close-regular-24.ico")    # Icône de la fenêtre

font_error = customtkinter.CTkFont(size= 11)    # Taille pour le message d'erreur 

label_error = customtkinter.CTkLabel(app, text='', width=40, height=28, fg_color='transparent', font= font_error, text_color= "red")    # Message d'erreur initialement vide
label_error.place(x=85, y=0)

entry = customtkinter.CTkEntry(app, placeholder_text='Exact App name', width=140, height=28, corner_radius= 1, border_width= 1)    # Entrée de l'utilisateur
entry.place(x = 85, y = 20,)

scrollable_frame_applications = customtkinter.CTkScrollableFrame(app, width=200, height=268, corner_radius= 0, fg_color= "transparent")    # Frame pour les applications
scrollable_frame_applications.pack(pady = (0,15), side = "bottom", fill="both")

with open('applications.json', 'r') as data:    # Ouverture du fichier json en mode read
    
    applications = json.load(data)    # Chargement du fichier json en dictionnaire

row = 0    # Variable repésentant les lignes de la grid

for appli in applications.get("applications"):    # Affichage des applications
    
    label = customtkinter.CTkLabel(scrollable_frame_applications, text=f'{appli}', width=40, height=28, fg_color='transparent')    # Label des applications du json
    label.grid(padx = (10,0), pady = (10,0), column = 1, row = row)
    
    button_delete = customtkinter.CTkButton(scrollable_frame_applications, text='Delete', width=40, height=28, corner_radius=1)    # Bouton pour supprimer les apps
    button_delete.grid(padx = (5,0), column = 2, pady = (10,0), row = row)
    
    row += 1    # Incrémentation de la variable des lignes de 1



def add():    # Fonction rattachée au bouton add
    
    new_app = entry.get()    # Récupération de l'entrée de l'utilisateur
    
    if new_app + ".exe" in applications.get("applications"):    # Vérification de la présence de l'application dans le fichier json
        
        label_error.configure(text = "This app is already registered")    # Message d'erreur
    
    elif new_app == "":
        
        label_error.configure(text = "Please enter an app name")    # Message d'erreur en cas de champs non rempli
    
    else:
        
        label_error.configure(text = "")    # Pas d'erreur
        
        list_appli = applications.get("applications")    # Initialisation de la list_appli avec les applications contenues dans le json
        
        
        list_appli.append(new_app + ".exe")    # Ajout de l'application entrée par l'utilisateur à la liste des applications
        
        applications["applications"] = [    # Modification de l'objet python avec les nouvelles applications
            
            *list_appli    # Dépaquétage de la liste pour intégrer ces éléments au dictionnaire
            
        ]
        
        global row    # Variable pour les lignes définie plus haut
        
        label = customtkinter.CTkLabel(scrollable_frame_applications, text=f'{new_app}', width=40, height=28, fg_color='transparent')    # Label des applications du json
        label.grid(padx = (10,0), pady = (10,0), column = 1, row = row)
        
        
        def delete():    # Fonction pour supprimer les applications
            pass
        
        button_delete = customtkinter.CTkButton(scrollable_frame_applications, text='Delete', width=40, height=28, corner_radius=1)    # Bouton pour la suppression des applications
        button_delete.grid(padx = (5,0), column = 2, pady = (10,0), row = row)
        
        row += 1    # Incrémentation de la variable des lignes de 1
    
    with open('applications.json', 'w') as data:    # Ouverture du fichier json en mode write
        
        json.dump(applications, data, indent=4)    # Conversion de l'objet python avec les nouvelles applications en fichier json et modification du fichier json 




add_button = customtkinter.CTkButton(app, text='Add', width=40, height=28, corner_radius= 1, command = add)    # Bouton ajouter
add_button.place(x = 235, y = 20)

font_app_name = customtkinter.CTkFont(size = 9)

def button_event():
    
    frame_app_names = customtkinter.CTkToplevel(app)

    frame_app_names.geometry('360x350')    # Définition de la taille de la fenêtre

    frame_app_names.resizable(False, False)    # Désactivation de la redimensionnement de la fenêtre

    frame_app_names.title('CTW-J')    # Nom de la fenêtre


button_app_name = customtkinter.CTkButton(app, text='App\nnames', width=20, height=28, font = font_app_name, corner_radius = 1, command = button_event)
button_app_name.place(x=284, y=20)

app.mainloop()    # Méthode pour l'exécution de l'interface