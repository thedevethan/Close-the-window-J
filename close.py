# Si tu ne t'appelles pas Ethan et que tu n'as pas installé le module psutil je te conseille de le faire !


import psutil    # Module permettant la gestion des processus

import json    # Module permettant d'interagir avec le fichier json


class Processus:    # Classe Processus contenant des méthodes pour gérer les processus
    
    def __init__(self):    # Constructeur initial
        
        pass
    
    def list_process(self):    # Méthode retournant une liste contenant tous les processus en cours
        
        list_sorted = []    # Initialisation de la liste qui va contenir les noms des processus en cours
        
        for proc in psutil.process_iter():   # psutil.process_iter sert à obtenir des informations brutes sur les processus en cours, obtention des diverses informations relatives aux processus en cours
            
            list_sorted.append(proc.name())    # L'application de la méthode name à l'objet représentant le processus renvoie son nom exacte, ajout du nom du processus à la liste list_sorted
        
        return sorted(list_sorted)    # Retour au programme d'une liste triée contenant tous les noms des processus en cours
    
    def kill_process(self,name):    # Méthode servant à arrêter un processus en cours, avec pour paramètre le nom du processus que l'on veut arrêter
        
        for proc in psutil.process_iter():    # Itération sur la liste contenant les informations brutes sur les différents processus en cours
            
            if proc.name() == name:    # Vérification de la condition suivante: si le nom de processus entré en paramètre correspond à un processus en cours
                
                proc.kill()    # Arrêt du processus en cours une fois identifié



def main():    # Fonction principale
    
    with open("applications.json", 'r') as data:    # with pour manipuler le flux des fichiers, ouvrir le fichier json en mode read, data contient le fichier json
        
        applications = json.load(data)    # Chargement du fichier json dans un objet python
    
    obj = Processus()    # Création d'une instance de la classe Processus
    
    "print(obj.list_process())"   # Si tu veux voir la liste des processus en cours tu peux utiliser la méthode list_process()
    
    List_of_applications_to_close = applications.get("applications")    # Si tu veux ajouter une autre application tu dois mettre le nom exact du processus
    
    for name in List_of_applications_to_close:    # Itération sur les éléments de la liste des applicqtions à fermer pour pouvoir les fermer
        
        if name in obj.list_process():    # Vérification de la condition suivante: Si le nom de l'application se trouve dans la liste des processus en cours
            
            obj.kill_process(name)    # Application de la méthode kill_process à l'instance de la classe pour arrêter le processus en cours 

main()