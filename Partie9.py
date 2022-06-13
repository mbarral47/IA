
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
            dir=""
            while dir!="stop":
                print("\n")
                print("Direction(s) possible(s) pour votre joueur: \n", p)
                dir = input("Vous pouvez avancer, indiquez une direction ou stop pour s'arreter: ")
                if (dir!="stop"):
                    self.lab.deplace(dir, joueur)
                    self.lab.DispJeu()
                    p = self.lab.avance(joueur)

        else:
            print("Impossible de bouger une autre stratégie aurait été meilleure")

            
    def tourOrdi (self, tab):
        #ex, tab = ["oui",3,"ligne", "gauche", 1, "haut"]
        d = 1

        if tab[0] == "oui":
            r = tab[1]
            self.lab.motrice.rotation(r)
            o = tab[2]
            c = tab[3]
            n = tab[4]
            self.lab.une_translation(o, c, n)

            d = 5
            
        for dir in range(d, len(tab)):
            p = self.lab.avance(self.lab.joueurB)
            if tab[dir] not in p:
                print("impossible")
                break
            self.lab.deplace(tab[dir], self.lab.joueurB)

        self.lab.DispJeu()
        

    def deroulement(self):
        while(True):
            self.tour(self.lab.joueurA)
            if self.lab.joueurA==self.lab.tresor :
                print("Vous avez gagné")
                break
            print("")
            print("A l'ordi")
            print("")
            #self.tour(self.lab.joueurB)
            #tab = ["oui", 3, "ligne", "gauche", 1, "haut"]
            tab = ["non", "haut", "droite"]
            self.tourOrdi(tab)
            if self.lab.joueurB==self.lab.tresor:
                print("Vous avez perdu")
                break
            print("")
            print("A vous de jouer")
            print("")

if __name__=="__main__" :
    j=jeu()
    j.deroulement()
