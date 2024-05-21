# Si tu ne t'appelles pas Ethan et que tu n'as pas installé le module psutil je te conseille de le faire !


import psutil    # Module permettant la gestion des processus


class processus:    # Classe Processus contenant des méthodes pour gérer les processus
    
    def __init__(self):    # Constructeur initial
        
        pass
    
    def list_process(self):    # Méthode servant à lister les processus en cours
        
        list_sorted = []    # Initialisation de la liste qui va contenir les noms des processus en cours
        
        for proc in psutil.process_iter():   # psutil.process_iter sert à obtenir des informations brutes sur les processus en cours, obtention des diverses informations relatives aux processus en cours
            
            list_sorted.append(proc.name())    # L'application de la méthode name à l'objet représentant le processus renvoie son nom exacte, ajout du nom du processus à la liste list_sorted
        
        for proc in sorted(list_sorted):    # Itération sur la liste liste list_sorted triée
            
            print(proc)    # Affichage du processus en cours
    
    def kill_process(self,name):    # Méthode servant à arrêter un processus en cours, avec pour paramètre le nom du processus que l'on veut arrêter
        
        for proc in psutil.process_iter():    # Itération sur la liste contenant les informations brutes sur les différents processus en cours
            
            if proc.name() == name:    # Vérification de la condition suivante: si le nom de processus entré en paramètre correspond à un processus en cours
                
                proc.kill()    # Arrêt du processus en cours une fois identifié



def main():    # Fonction principale
    
    obj = processus()    # Création d'une instance de la classe Processus
    
    "obj.list_process()"   # Si tu veux voir la liste des processus en cours tu peux utiliser la méthode list_process()
    
    List_of_applications_to_close = ["steam.exe", "opera.exe", "Discord.exe"]    # Si tu veux ajouter une autre application tu dois mettre le nom exact du processus
    
    for name in List_of_applications_to_close:    # Itération sur les éléments de la liste des applicqtions à fermer pour pouvoir les fermer
        
        obj.kill_process(name)    # Application de la méthode kill_process à l'instance de la classe pour arrêter le processus en cours 

main()