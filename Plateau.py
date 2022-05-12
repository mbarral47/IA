#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
import ProjetLabyrinthe as pl
import sys
import string
from termcolor import colored, cprint


path = "/home/user/Documents/IA&Jeux/ProjetIA/ProjetLabyrinthe.py"
sys.path.append(path)

def choixlignes(nbdir):
    possibles = [1,2,3,4,5,6,7,8]
    k=0
    n=len(possibles)
    while n>nbdir:
        a=possibles[k]
        b=0
        b=random.randint(0,1)
        if b==1:
            possibles.remove(a)
            k=0
            
        n=len(possibles)
        k=(k+1)%n
    return possibles

def choixcol(t):
    
    for i in range(len(t)):
        j=random.randint(1,8)
        a=t[i]
        t[i]=[a,j]    
    x=1
    b=False
    while not b:
        b=True
        while x < len(t)-3:
            if t[i][1]==t[i+1][1]:
                b=False
                t[i]=random.randint(1,8)
    return t


class Labyrinthe:
    def __init__(self):

        self.motrice = pl.MobileCase(1000, 1000,2)
        self.plateau = []
        self.tresor = [0, 0]
        self.joueurA = [0, 8]
        self.joueurB = [8, 0]

        t = choixlignes(4)
        t=choixcol(t)

        for i in range(9):
            self.plateau.append([])
            for j in range(9):
                contraintes = [0, 0, 0, 0]
                if ([i,j] in t):
                    dir =3
                else : 
                    dir = 2
                
                self.plateau[i].append(pl.MobileCase(i, j,dir))
                if(i % 2 == 0 and j % 2 == 0):
                    if (i == 0):
                        contraintes[1] = 1

                    if (i == 8):
                        contraintes[3] = 1

                    if (j == 0):
                        contraintes[2] = 1

                    if (j == 8):
                        contraintes[0] = 1

                    self.plateau[i][j] = pl.ImmobileCase(j, i, contraintes,dir)
        self.tresor[0] = random.randint(2, 4)
        self.tresor[1] = random.randint(2, 4)



""" ATTENTION 
Si le joueur est sur une des cases qui bougent à cause d'une translation le joueur doit bouger également"""

    def modif_joueurs(self,num,opt,mvt):
        """ permet de modifier les position des joueurs et du trésor lors d'une translation
        opt est dit si l'on va placer la motrice sur l"""
        ind=0
        if opt=="true":
            ind=0
        else:
            ind=1
        
        if(self.joueurA[ind]==num):
            self.joueurA[1-ind]=self.joueurA[1-ind]+mvt
            """ gere si le joueur est ejecté du plateau"""
            if self.joueurA[1-ind] >8 or self.joueurA[1-ind] <0:
                self.joueurA=[0,8]
        
        if(self.joueurB[ind]==num):    
            self.joueurB[1-ind]=self.joueurB[1-ind]+mvt
            if self.joueurB[1-ind] >8 or self.joueurB[1-ind] <0:
                self.joueurB=[0,8]
        
        if(self.tresor[ind]==num):
            self.tresor[1-ind]=self.tresor[1-ind]+mvt
            if self.tresor[1-ind] >8 or self.tresor[1-ind] <0:
                a=random.randint(2,4)
                b=random.randint(2,4)
                self.tresor=[a,b]

    def une_translation(self, opt, cote, num):
        """ une translation sur une colonne se fait par les i
        une ligne par les j
        opt = oui si ligne
        cote = droit|haut|gauche|bas
        num = numéro de la ligne ou colonne
        """

        if (opt=="oui" and cote == "gauche"):
            tmp = []
            for j in range(9):

                print(self.plateau[num][j].toString())
                tmp.append(self.plateau[num][j].toMobileCase())

            self.plateau[num][0] = self.motrice
            self.motrice = tmp[8]
            self.modif_joueurs(num,opt,1)

            for j in range(1,9):
                self.plateau[num][j] = tmp[j-1]

        elif (opt=="oui" and cote == "droite"):
            tmp = []
            for j in range(9):

                print(self.plateau[num][j].toString())
                tmp.append(self.plateau[num][j].toMobileCase())

            self.plateau[num][8] = self.motrice
            self.motrice = tmp[0]
            self.modif_joueurs(num,opt,-1)
            for j in [1, 2, 3, 4, 5, 6,7,8]:
                self.plateau[num][j-1] = tmp[j]

        elif(opt=="non" and cote == "haut"):
            tmp = []
            for i in range(9):

                print(self.plateau[i][num].toString())
                tmp.append(self.plateau[i][num].toMobileCase())

            self.plateau[0][num] = self.motrice
            self.motrice = tmp[8]
            self.modif_joueurs(num,opt,1)
            for i in [1, 2, 3, 4, 5, 6,7,8]:
                self.plateau[i][num] = tmp[i-1]

        elif (opt=="non" and cote == "bas"):

            tmp = []
            for i in range(8):

                print(self.plateau[i][num].toString())
                tmp.append(self.plateau[i][num].toMobileCase())

            self.modif_joueurs(num,opt,1)
            self.plateau[8][num] = self.motrice
            self.motrice = tmp[0]


            for i in [1, 2, 3, 4, 5, 6,7,8]:
                self.plateau[i-1][num] = tmp[i]


            
    def printGame(self):
        coul = 'white'
        s = ""
        for i in range(9):
            s = "".join([s, "\n"])
            for j in range(9):
                    coul = 'yellow'
        print(s)
        print("\n ", self.motrice.toString())



    def avance(self, direc, joueur):
        a = joueur[0]
        b = joueur[1]
        if (direc == "gauche" and self.plateau[a][b].directions[2] == True
                and self.plateau[a][b-1].directions[0] == True and b > 0):
            return True

        elif (direc == "droite" and self.plateau[a][b].directions[0] == True
              and self.plateau[a][b+1].directions[2] == True and b < 8):
            return True

        elif (direc == "haut" and self.plateau[a][b].directions[1] == True
              and self.plateau[a-1][b].directions[3] == True and a > 0):
            return True
        elif (direc == "bas" and self.plateau[a][b].directions[3] == True
              and self.plateau[a+1][b].directions[1] == True and a < 8):
            return True

        elif(direc == "rester"):
            return True
        else:

            return False
    
    def avanceBis(self, joueur):
        a = joueur[0]
        b = joueur[1]
        res = []
                
        if (self.plateau[a][b].sommet[2] and b > 0):
            if( self.plateau[a][b].directions[2] == True
                and self.plateau[a][b-1].directions[0] == True ):
                res.append("gauche")

        if (self.plateau[a][b].sommet[0] and b < 8):
            if (self.plateau[a][b].directions[0] == True
            and self.plateau[a][b+1].directions[2] == True ):
                res.append("droite")

        if (self.plateau[a][b].sommet[1] and a > 0):
            if(self.plateau[a][b].directions[1] == True
            and self.plateau[a-1][b].directions[3] == True ):
                res.append("haut")
        
        if (self.plateau[a][b].sommet[3] and a < 8):
            if(self.plateau[a][b].directions[3] == True
            and self.plateau[a+1][b].directions[1] == True ):
                res.append("bas")

        return res

    
    
    def deplace(self, direc, joueur):
        if self.avance(direc, joueur):
            if direc == "gauche":
                joueur[1] = joueur[1]-1
            elif direc == "droite":
                joueur[1] = joueur[1]+1
            elif direc == "haut":
                joueur[0] = joueur[0]-1
            else:
                joueur[0] = joueur[0]+1

    def deplaceBis(self, direc, joueur):
        if direc == "gauche":
            joueur[1] = joueur[1]-1
        elif direc == "droite":
            joueur[1] = joueur[1]+1
        elif direc == "haut":
            joueur[0] = joueur[0]-1
        else:
            joueur[0] = joueur[0]+1




    """def printGame(self):
        coul = 'white'
        s=""
        for i in range(7):
            s="".join([s,"\n"])
            for j in range(7):
                coul='white'
                if i==self.tresor[0] and j == self.tresor[1]: 
                    coul='yellow'
                    
                elif i==self.joueurA[0] and j==self.joueurA[1]:
                    coul = 'red'
                elif i==self.joueurB[0] and j==self.joueurB[1]:
                     coul = 'blue'
                string = colored(self.plateau[i][j].toString(),coul,attrs=['bold'])
                s = "".join([s,string])
        print(s)
        print("\n ",self.motrice.toString())"""



    def CodeJeu(self):
        tab = []
        
        for i in range(27):
            tmp = []
            for j in range(27):
                tmp.append(0)
            tab.append(tmp)

        for ci in range(9) :
            for cj in range(9):
                
                
                tmp2 = self.plateau[ci][cj].coder()
                for i in range(3):
                    for j in range(3):
                        tab[ci*3+i][cj*3+j] = tmp2[i][j]
                    
                
        return tab
    
    
    def DispJeu(self):
        tab=self.CodeJeu()
        s="\n       1        2       3        4        5        6        7         8        9\n"
        for i in range(27):
            for j in range(27):
                tab[i][j]=int(tab[i][j])
            
        for i in range(27):
            if i%3==0:
                s=s+"\n     ------   ------   ------   ------   ------   ------   ------   ------   ------"
                s=s+"\n   "
            elif ((i-1)%3==0):
                st = str((i-1)/3)[0]
                s = s+"\n"
                s="".join([s,st])
                s = s+"  "  
            else : 
                s  = s+"\n   "

            for j in range(27):
                char = "o"
                sep=""
                coul='white'
                
                """  definition du caractère a afficher"""
                if (self.joueurA[0]*3+1==i and self.joueurA[1]*3 +1==j):
                    char = "J "
                    coul="red"
                elif(self.joueurB[0]*3+1==i and self.joueurB[1]*3 +1==j):
                    char = "J "
                    coul="blue"
                elif(self.tresor[0]*3+1==i and self.tresor[1]*3 +1==j):
                    char = "T "
                    coul="yellow"
                elif(tab[i][j]==1)  :
                    char = "  "
                elif(int(tab[i][j])==0):
                    char = "▓ "
                
                """ definition du caractère de séparation"""
                if(j%3==0):
                    sep=" | "
                string = colored(char, coul, attrs=['bold'])
                s = sep.join([s, string])
                
        print(s)
        print("\n",self.motrice.toString())


"""

if __name__ == "__main__":


    Lab = Labyrinthe()
    tab = Lab.CodeJeu()
    Lab.DispJeu()
    #print(int(tab[0][2]))

"""


     
   
