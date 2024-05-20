# Si tu ne t'appelles pas Ethan et que tu n'as pas installé le module psutil je te conseille de le faire


import psutil


class processus:
    
    def __init__(self):
        
        pass
    
    def list_process(self):
        
        list_sorted = []
        
        for proc in psutil.process_iter():
            
            list_sorted.append(proc.name())
        
        for proc in sorted(list_sorted):
            
            print(proc)
    
    def kill_process(self,name):
        
        for proc in psutil.process_iter():
            
            if proc.name() == name:
                
                proc.kill()



def main():
    
    obj = processus()
    
    "obj.list_process()"   # Si tu veux voir la liste des processus en cours tu peux utiliser la méthode list_process()
    
    List_of_applications_to_close = ["steam.exe", "opera.exe", "Discord.exe"]    # Si tu veux ajouter une autre application tu dois mettre le nom exact du processus
    
    for name in List_of_applications_to_close:
        
        obj.kill_process(name)

main()