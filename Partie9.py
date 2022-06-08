
import sys
import Plateau9 as plat

path = "/Plateau9"
sys.path.append(path)

class jeu :

    def __init__(self):
        #générer un plateau
        self.lab = plat.Labyrinthe()
        self.lab.DispJeu()
    
    def tour(self, joueur):
        print(self.lab.motrice.toString())
        p = self.lab.avance(joueur)
        print("direction(s) possible(s) pour votre joueur: \n", p)
        t = input("suite à la réponse souhaitez-vous faire une translation: ")
        if (t=="oui"):
            #optimiser rotation pièce avec touche clavier
            r = int(input("rotation pièce indiquer quart de tour sens trigo: "))
            self.lab.motrice.rotation(r)
            print(self.lab.motrice.toString())

            o = input("ligne - colonne: ")
            c = input("par la gauche ou droite ou haut ou bas : ")
            n = int(input("et un numéro pair de ligne ou colonne: "))
            while (n%2!=0):
                n = int(input("et un numéro pair de ligne ou colonne: "))
            self.lab.une_translation(o, c, n-1)
            self.lab.DispJeu()
            p = self.lab.avance(joueur)
            
            
        if p!=[]:
            print("direction(s) possible(s) pour votre joueur: \n", p)
            dir = input("indiquez une direction: ")

            while dir not in p:
                dir = input("indiquez une direction: ")
            else:
                self.lab.deplace(dir, joueur)
                self.lab.DispJeu()
        
            p = self.lab.avance(joueur)
            dir="dir"

        else:
            print("impossible de bouger une translation aurait été plus judicieux")
            dir="stop"
            

       
        while dir!="stop":
            print("direction(s) possible(s) pour votre joueur: \n", p)
            dir = input("vous pouvez toujours avancer, indiquez une direction ou stop pour s'arreter: ")
            if (dir!="stop"):
                self.lab.deplace(dir, joueur)
                self.lab.DispJeu()
                p = self.lab.avance(joueur)

        print("")
        print("au joueur suivant")
        print("")
    
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
