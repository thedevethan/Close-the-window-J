
import customtkinter    # Module pour le GUI

import psutil    # Module pour relever des informations relatifs aux processus actifs

import json # Module pour interagir avec le fichier json

import shutil # Module pour le déplacemnt des fichiers

from functools import partial # Module pour la création de fonctions partielles

import sys    # Module permettant d'interagir avec l'interpréteur python

import ctypes # Module permmettant d'interagir avec des bibliothèques externes

"""if not ctypes.windll.shell32.IsUserAnAdmin():    # Vérification de la condition suivante: Si l'utilisateur a les droits administrateurs
    
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)    # Demande à l'utilisateur d'élever ses privilèges
    
    sys.exit()    # Arrêt du processus"""

def verify_shortcut():    # Fonction permmetant de vérifier si un raccourcis de l'exécutable est présent dans le dossier démarrer
    
    with open('applications.json', 'r') as data:    # Ouverture du fichier json en mode read
        
        database = json.load(data)
    
    if database.get("shortcut_startup") == False:    # Vérification de la condition suivante: Si la valeur de la clé shortcut_startup du dictionnaire database est false 
        
        shutil.move("short.c", "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\short.c")    # Déplacement du fichier dans le dossier démarrer
        
        with open('applications.json', 'w') as data:    # Ouverture du fichier json en mode write
            
            database["shortcut_startup"] = True    # Changement de la valeur de la clé shortcut_startup
            
            json.dump(database, data, indent=4)    # Conversion de l'objet python avec la nouvelle valeur de shortcut_startup en fichier json et modification du fichier json

verify_shortcut()    # Appel de la fonction

app = customtkinter.CTk()    # Instanciation de la classe

app.geometry('360x350')    # Définition de la taille de la fenêtre

app.resizable(False, False)    # Désactivation de la redimensionnement de la fenêtre

app.title('Close the window J')    # Nom de la fenêtre

app.iconbitmap("window-close-regular-24 (1).ico")    # Icône de la fenêtre

font_error = customtkinter.CTkFont(size= 11)    # Taille pour le message d'erreur 

label_error = customtkinter.CTkLabel(app, text='', width=40, height=28, fg_color='transparent', font= font_error, text_color= "red")    # Message d'erreur initialement vide
label_error.place(x=85, y=0)

entry = customtkinter.CTkEntry(app, placeholder_text='Exact App name', width=140, height=28, corner_radius= 1, border_width= 1)    # Entrée de l'utilisateur
entry.place(x = 85, y = 20,)

scrollable_frame_applications = customtkinter.CTkScrollableFrame(app, width=200, height=268, corner_radius= 0, fg_color= "transparent")    # Frame pour les applications
scrollable_frame_applications.pack(pady = (60,0), fill="both")


with open('applications.json', 'r') as data:    # Ouverture du fichier json en mode read
    
    applications = json.load(data)    # Chargement du fichier json en dictionnaire

def delete(index, appli):    # Fontion pour la suppression des applications initialements présentes
    
    list_child = scrollable_frame_applications.winfo_children()    # Obtention de la liste de tous les enfants de la frame scrollframe
    
    index_button_child = list_child.index(buttons[index])    # Obtention de l'index du bouton dans la liste des enfants de la frame scrollframe
    
    list_child[index_button_child-1].destroy()    # Destruction de l'enfant qui précède le bouton (le label)
    
    buttons[index].destroy()    # Destruction du bouton
    
    list_appli = applications.get("applications")    # Liste contenant les applications du json
    
    list_appli.remove(appli)    # Suppression de l'application de la liste des applications
    
    with open('applications.json', 'w') as data:    # Ouverture du fichier json en mode write
        
        json.dump(applications, data, indent=4)    # Conversion de l'objet python avec les nouvelles applications en fichier json et modification du fichier json

row = 0    # Variable repésentant les lignes de la grid

buttons = []    # Liste qui va contenir tous les boutons

for index, appli in enumerate(applications.get("applications")):    # Affichage des applications dans la framescroll, utilisation de la fonction enumerate pour l'itérationn sur l'index de l'élément de la liste et sur l'élément lui même
    
    label = customtkinter.CTkLabel(scrollable_frame_applications, text=f'{appli.replace(".exe","")}', width=40, height=28, fg_color='transparent')    # Label des applications du json
    label.grid(padx = (10,0), pady = (10,0), column = 1, row = row)
    
    buttons.append(customtkinter.CTkButton(scrollable_frame_applications, text='Delete', width=40, height=28, corner_radius=1, command = partial(delete, index, appli)))    # Bouton pour la suppression des applications
    buttons[index].grid(padx = (5,0), column = 2, pady = (10,0), row = row)
    
    row += 1    # Incrémentation de la variable des lignes de 1

def add(event):    # Fonction rattachée au bouton add, event pour faire référence à l'évennement définie ppour cette fonction
    
    new_app = entry.get()    # Récupération de l'entrée de l'utilisateur
    
    if new_app + ".exe" in applications.get("applications"):    # Vérification de la présence de l'application dans le fichier json
        
        label_error.configure(text = "This app is already registered")    # Message d'erreur
    
    elif new_app == "":
        
        label_error.configure(text = "Please enter an app name")    # Message d'erreur en cas de champs non rempli
    
    elif len(new_app) >= 50:
        
        label_error.configure(text = "Invalid entry")    # Message d'erreur en cas d'application trop longue
    
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
        
        index = len(buttons)    # Index des boutons delete qui vont s'ajouter au fur et à mesure
        
        buttons.append(customtkinter.CTkButton(scrollable_frame_applications, text='Delete', width=40, height=28, corner_radius=1, command = partial(delete,index, new_app + ".exe")))    # Ajout du bouton créé dans la liste boutons qui contient tous les autres boutons
        buttons[index].grid(padx = (5,0), column = 2, pady = (10,0), row = row)
        
        row += 1    # Incrémentation de la variable des lignes de 1

    with open('applications.json', 'w') as data:    # Ouverture du fichier json en mode write
        
        json.dump(applications, data, indent=4)    # Conversion de l'objet python avec les nouvelles applications en fichier json et modification du fichier json 


entry.bind("<Return>", add)    # Ajout d'une application suite à l'appui de  la touche Entrée de l'ordinateur


add_button = customtkinter.CTkButton(app, text='Add', width=40, height=28, corner_radius= 1)    # Bouton ajouter
add_button.place(x = 235, y = 20)

add_button.bind("<ButtonRelease-1>", add)    # Ajout d'une application suite à l'appui de la touche add définie dans l'application

font_app_name = customtkinter.CTkFont(size = 9)    # Taille du bouton App names

def process_information():    # Fonction pour l'affichage de la deuxième fenêtre
    
    frame_app_names = customtkinter.CTkToplevel(app)
    
    frame_app_names.geometry('360x350')    # Définition de la taille de la fenêtre
    
    frame_app_names.resizable(False, False)    # Désactivation de la redimensionnement de la fenêtre
    
    frame_app_names.title('Close the window J')    # Nom de la fenêtre
    
    scrollable_frame = customtkinter.CTkScrollableFrame(frame_app_names, width=200, height=200)    # Frame scrollante à l'intérieur de la frame
    
    scrollable_frame.pack(expand = "True", fill = "both")
    
    for proc in psutil.process_iter():    # Itération sur informations brutes du processus
        
        label = customtkinter.CTkLabel(scrollable_frame, text= f'{proc.name()}', width=40, height=28, fg_color='transparent')    # Affichage des processus actifs
        
        label.pack()


button_app_name = customtkinter.CTkButton(app, text='App\nnames', width=40, height=28, font = font_app_name, corner_radius = 1, command = process_information)    # Bouton app name
button_app_name.place(x=284, y=20)


def save():    # Fonction permettant la sauvegarde
    
    bouton_save.after(500)    # Temps de latence de 500 millisecondes
    
    bouton_save.configure(text = "Saved!")    # Changement du texte du bouton

font_save = customtkinter.CTkFont(weight = "bold")    # Police du bouton save

bouton_save = customtkinter.CTkButton(app, text='Save Changes', width=140, height=15, corner_radius= 0, font = font_save, command = save)    # Bouton de sauvegarde

bouton_save.pack(side = "bottom", fill = "x")    # Fill = "x" pour que le bouton occupe toute la largeur disponible 

app.mainloop()    # Méthode pour l'exécution de l'interface