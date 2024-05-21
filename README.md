Si tu veux par exemple fermer automatiquement les applications qui se lancent dès le démarrage de ton ordinnateur, voici une proposition de démarche: 

1. Créer un exécutable du script avec le module pyinstaller (faire pyinstaller --onefile --noconsole /chemin_vers_le_script/ pour créer l'exécutable),
  
2. Créer un raccourci de l'exécutable,

3. Le copier et le coller dans le dossier "Démarrage" de ton ordinateur en suivant ce chemin "C:\ProgramData\Microsoft\Windows\Menu Démarrer\Programmes\Démarrage"
