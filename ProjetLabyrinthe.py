#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 09:26:11 2022

@author: user
"""
""" 
A faire : methode sur Labyrinthe qui prend la case motrice, 
effecture les changements et retrourne une nouvelle case motrice

représentation graphique du jeu (symbolique)
representation 1 : une un caractère sur une ligne pour une case
2 : plusieurs lignes pour une case




"""

import random

class CaseGen :
    
    def __init__(self,i,j): 
        self.colonne=j
        self.ligne=i
        self.directions=[False,False,False,False]
        self.sommet={0 : "droite",1 :"haut",2:"gauche",3: "bas"}
        
      
    def get_dir(self,a):
        return self.directions[a]
    
     
    def toString(self):
        
        
        if self.directions ==[True,True,False,False]: 
            return "[ L ]"
            
        elif self.directions ==[False,True,True,False]: 
            return "[_| ]"
        
        elif self.directions ==[True,False,True,False]: 
            return "[___]"
        
        elif self.directions ==[False,False,True,True]: 
            return "[ 7 ]"
        
        elif self.directions ==[False,True,False,True]: 
            return "[ | ]"
        
        elif self.directions ==[True,False,False,True]:
            return "[ Γ ]"
            
        
        #C(4,3)=4
        elif self.directions==[True ,True,True,False]: 
            return "[_|_]"
        
        elif self.directions == [True,True,False,True]:  
            return "[|- ]"
        
        
        elif self.directions == [True,False,True,True]:  
            return "[ T ]"
        
        else :
            #false,true,true,true
            return "[ -|]"
        
    def coder (self): 
        """code une case en une matrice de taille 3 x 3 pour
        afficher graphiquement les directions possibles"""
        if self.directions ==[True,True,False,False]: 
            return [[0,1,0],[0,1,1],[0,0,0]] 
            
        elif self.directions ==[False,True,True,False]: 
            return [[0,1,0],[1,1,0],[0,0,0]] 
        
        elif self.directions ==[True,False,True,False]: 
            return [[0,0,0],[1,1,1],[0,0,0]]
        
        elif self.directions ==[False,False,True,True]: 
            return [[0,0,0],[1,1,0],[0,1,0]]
        
        elif self.directions ==[False,True,False,True]: 
            return [[0,1,0],[0,1,0],[0,1,0]]
        
        elif self.directions ==[True,False,False,True]:
            return [[0,0,0],[0,1,1],[0,1,0]]
            
        
        
        elif self.directions==[True ,True,True,False]: 
            return [[0,1,0],[1,1,1],[0,0,0]]
        
        elif self.directions == [True,True,False,True]:  
            return [[0,1,0],[0,1,1],[0,1,0]]
        
        
        elif self.directions == [True,False,True,True]:  
            return [[0,0,0],[1,1,1],[0,1,0]]
        
        else :
            #false,true,true,true
            return [[0,1,0],[1,1,0],[0,1,0]]
    
    def toMobileCase(self):
        A=MobileCase(self.ligne,self.colonne)
        A.colonne=self.colonne
        A.ligne=self.ligne
        for i in range(4):
            A.directions[i] = self.directions[i]

        return A
        
        

class ImmobileCase (CaseGen):
    def __init__(self,i,j,tab_contraintes,dir):
        
        super(ImmobileCase,self).__init__(i,j)
        possibles = []
        p = random.randint(1,3)

        for i in range(dir) :
            if tab_contraintes[i]== 0  :
                possibles.append(i)
        
        nb_direct= min(len(possibles),dir)

        #while(nb_direct>0) :
        sommet = random.sample(possibles,nb_direct)
        n = len(sommet)
        for i in range(n):
    
            a=sommet[(i+p)%n]
            print(a)
            if i < nb_direct : 
                self.directions[a]=True 
            #nb_direct = nb_direct-1
            
        self.mobile = False

"""

"""

class MobileCase (CaseGen):
    
    def __init__(self,i,j,nbdir):
        super(MobileCase,self).__init__(i,j)
        
        
        nb_direct = nbdir
        deja_tire = []
        while(nb_direct>0) :
            sommet = random.randint(0,3)
            if sommet not in deja_tire  : 
                deja_tire.append(sommet)
                self.directions[sommet]=True  
                nb_direct = nb_direct-1
        
        
    def rotation(self,teta):
        """sens trigonométrique"""
        teta = teta%4
        tab = []
        for i in range(4):
            tab.append(self.directions[i])

        for i in range(4) : 
            indice = (i+teta)%4
            self.directions[indice]= tab[i]
