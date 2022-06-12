
import sys
import Plateau9 as plat

path = "/Plateau9"
sys.path.append(path)

class jeu :

    def __init__(self):
        self.lab = plat.Labyrinthe()
        self.lab.DispJeu()
    
    def tour(self, joueur):
        print("\nPièce motrice")
        self.lab.printMotrice()
        print("\n")
        p = self.lab.avance(joueur)
        print("Direction(s) possible(s) pour votre joueur : \n", p)
        t = input("Suite à la réponse souhaitez-vous faire une translation? : ")

        if (t=="oui"):
            #optimiser rotation pièce avec touche clavier
            r = int(input("Rotation pièce, indiquez le(s) quart(s) de tour dans le sens trigonométrique : "))
            self.lab.motrice.rotation(r)
            self.lab.printMotrice()
            print("\nLa translation doit se faire ")

            o = input("  par une ligne ou une colonne : ")
            while(o not in ["ligne", "colonne"]):
                o = input("  par une ligne ou une colonne : ")
            c = input("  par la gauche ou droite ou haut ou bas : ")
            while(c not in ["droite", "gauche", "haut", "bas"]):
                c = input("  par la gauche ou droite ou haut ou bas : ")
            n = int(input("  et un numéro pair de ligne ou colonne : "))
            while (n%2!=0):
                n = int(input("  et un numéro pair de ligne ou colonne : "))
            
            self.lab.une_translation(o, c, n-1)
            self.lab.DispJeu()
            p = self.lab.avance(joueur)
            
            
        if p!=[]:
            print("\n")
            print("Direction(s) possible(s) pour votre joueur: \n", p)
            dir = input("Indiquez une direction: ")

            while dir not in p:
                dir = input("Indiquez une direction: ")
            else:
                self.lab.deplace(dir, joueur)
                self.lab.DispJeu()
        
            p = self.lab.avance(joueur)
            dir="dir"

        else:
            print("Impossible de bouger une translation aurait été plus judicieux")
            dir="stop"
            

       
        while dir!="stop":
            print("\n")
            print("Direction(s) possible(s) pour votre joueur: \n", p)
            dir = input("Vous pouvez toujours avancer, indiquez une direction ou stop pour s'arreter: ")
            if (dir!="stop"):
                self.lab.deplace(dir, joueur)
                self.lab.DispJeu()
                p = self.lab.avance(joueur)


    
    def deroulement(self):
        while(True):
            self.tour(self.lab.joueurA)
            if self.lab.joueurA==self.lab.tresor :
                print("VICTOIRE JOUEUR A")
                break
            print("")
            print("au joueur suivant")
            print("")
            self.tour(self.lab.joueurB)
            if self.lab.joueurB==self.lab.tresor:
                print("VICTOIRE JOUEUR B")
                break
            print("")
            print("au joueur suivant")
            print("")

if __name__=="__main__" :
    j=jeu()
    j.deroulement()
