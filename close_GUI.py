import customtkinter    # Module pour le GUI

app = customtkinter.CTk()    # Instanciation de la classe

app.geometry('360x350')    # Définition de la taille de la fenêtre

app.resizable(False, False)    # Désactivation de la redimensionnement de la fenêtre

app.title('CTW-J')    # Nom de la fenêtre

customtkinter.set_default_color_theme("dark-blue")    # Thème par défaut

app.iconbitmap("window-close-regular-24.ico")    # Icône de la fenêtre

app.mainloop()    # Méthode pour l'exécution de l'interface