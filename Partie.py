
import sys
import random
import ProjetLabyrinthe as pl
import string
from termcolor import colored, cprint
import Plateau as plat

path = "/home/barral/Documents/IA/Plateau"
sys.path.append(path)


class jeu :

    def __init__(self):
        #générer un plateau
        self.lab = plat.Labyrinthe()
        self.lab.DispJeu()
    
    def tour(self, joueur):
        p = self.lab.avanceBis(joueur)
        print("direction(s) possible(s) pour votre joueur: \n", p)
        t = input("suite à la réponse souhaitez-vous faire une translation (true/false): ")
        if (t=="true"):
            o = input("true : ligne - false : colonne: ")
            c = input("par la gauche ou droite ou haut ou bas : ")
            n = int(input("et un numéro de ligne ou colonne: "))
            self.lab.une_translation(o, c, n)
            self.lab.DispJeu()
            p = self.lab.avanceBis(joueur)
            
            print("Nouvelles direction(s) possible(s) pour votre joueurA: \n", p)
            dir = input("indiquez une direction: ")
        elif p!=[]:
            dir = input("indiquez une direction: ")
        else:
            print("impossible de bouger une translation aurait été plus judicieux")

        while dir not in p and p!=[]:
            dir = input("indiquez une direction: ")
        else:
            self.lab.deplaceBis(dir, joueur)
            self.lab.DispJeu()
        
        p = self.lab.avanceBis(joueur)
        dir="dir"
        while p!=[] and dir!="stop":
            print("direction(s) possible(s) pour votre joueurA: \n", p)
            dir = input("vous pouvez toujours avancer, indiquez une direction ou stop pour s'arreter: ")
            if dir!="stop":
                self.lab.deplaceBis(dir, joueur)
                self.lab.DispJeu()
                p = self.lab.avanceBis(joueur)
            else:
                print("au joueur suivant")
    
    def deroulement(self):
        while(True):
            self.tour(self.lab.joueurA)
            if self.lab.joueurA==self.lab.tresor :
                print("VICTOIRE JOUEUR A")
                break
            self.tour(self.lab.joueurB)
            if self.lab.joueurB==self.lab.tresor:
                print("VICTOIRE JOUEUR B")
                break

if __name__=="__main__" :
    j=jeu()
    j.deroulement()