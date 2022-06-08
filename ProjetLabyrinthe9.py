#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
    def __init__(self,i,j,tab_contraintes):
        
        super(ImmobileCase,self).__init__(i,j)
        possibles = []
        
        for i in range(4) :
            if tab_contraintes[i]==0  :
                possibles.append(i)
        
        nb_direct= min(random.randint(2,3),len(possibles))

        #while(nb_direct>0) :
        sommet = random.sample(possibles,nb_direct)
        for i in sommet:
            self.directions[i]=True 
            #nb_direct = nb_direct-1
            
        self.mobile = False



class MobileCase (CaseGen):
    
    def __init__(self,i,j):
        super(MobileCase,self).__init__(i,j)
        
        
        nb_direct = random.randint(2,3)
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

        
    
            
        

            