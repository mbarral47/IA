Jeu : Le Labyrinthe

Règles du jeu
Sur un plateau de 81 cases (9 par 9), certaines cases sont mobiles et d'autres non, un trésor est placé au centre et 2 joueurs placés aux extrémités opposées.
But du jeu : Pour gagner, il faut arriver le premier au trésor, pour ce faire le joueur peut se dépalcer directement si un chemin se dessine ou
faire glisser les cases en insérant une énième case et se déplacer ensuite. Les joueurs jouent à tour de rôle.

Dossier
Notre dossier se compose de trois fichiers:
plateau.py - labyrinthe.py - partie.py


labyrinthe.py
comprend la mise en place du plateau et particulièrement les définitions des cases

plateau.py
comprend toutes les fonctions nécessaires au jeu c'est-à-dire:
	-déplacement d'un joueur
	-translations d'une carte 
	-affichage du plateau

partie.py
décrit le déroulé d'une partie c'est ce fichier qu'il faut exécuter

Remarque:
Nous avons choisi un plateau de 9 par 9 lignes, à l'origine le plateau fait 7 par 7 mais le jeu est trop simple. On peut gagner du premier coup. En effet nous avons simplifié les règles du jeu de société d'origine, initialement les joueurs doivent passer par certaines cases pour collecter des objets
