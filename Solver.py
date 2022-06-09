
from json.encoder import HAS_UTF8
from re import A, S
import Plateau as plat
import Partie as game
import random 
import itertools
import copy 

def dirToDigit(t):
       
        tab = [0,0,0,0]
        if t==[]:
            return tab
        
        for i in t:
            if i =="droite":
                t[0]=1
            elif i=="haut":
                t[1]=1
            
            elif i =="gauche":
                t[2]=1

            elif i=="bas":
                t[3]=1

        return t

def digitToDir(t):
        
        conv =["droite","gauche","haut","bas"]
        res = []
        for i in range(len(t)):
            if t[i]==1:
                res.append(t[i])
        return res
            
               

class NoeudGen : 
    
    def __init__(self,v):
        self.val=v
        self.pere = None

    def getVal(self):
        return self.val

    def getPere(self):
        return self.pere

    def setPere(self,father):
        self.pere=father

    def toString(self):
        s=""
        if type(self)==type(Noeud(None,None)) : 
            s= s+"( "
            s=s+str(self.getVal())
            for i in range(len(self.fils)):
                a = self.getFils(i)
                s = s+ a.toString()
                
            s=s+" )"
            
        else: 
            s=s+" ( "
            s = s+self.getVal()
            s=s+" )"
        return s
            
    def count(self):
        print(type(self))
        c = 1
        if type(self)==type(Noeud(None,None)):
    
            for i in range(len(self.fils)):
                a = self.getFils(i)
                c =c + a.count()
        return c



class Feuille (NoeudGen):
    def __init__(self,v):
        self.pere = None
        self.val =v

    def toNoeud(self):
        p = self.getPere()
        self = Noeud(self.getVal,[])
        self.setPere(p)

class Noeud(NoeudGen):
    
    def __init__(self,v,t):
        self.fils=t
        for i in range(len(t)) :
            if type(t[i])!=type(NoeudGen(0)):
                t[i]==Noeud(0,[])
            t[i].setPere(self)
        self.val=v

        

    def makeFeuille(self):
        v =self.getVal()
        p = self.getPere
        self=Feuille(v)
        self.setPere(p)

    def addfils(self,f):

        self.fils = self.fils +f

        for i in range(len(self.fils)): 
            self.fils[i].setPere(self)

    

    def getFils(self,i):
        return self.fils[i]
    
    def getAllFils(self):
        return self.fils
        

class informations : 
    
    def __init__(self):
        #moyenne des valeurs heuristiques des feuilles du noeuds
        self.V=0
        #sommme des valeurs heuristiques du noeud. 
        self.t=0
        #nombre de visites
        self.n=0

class Arbreknaire:
    
    def __init__(self):
        self.root = Feuille(0)
        self.root.setPere(self.root)
        self.courant = self.root


    def gotoFils(self,i):
        self.courant = self.courant.getFils(i)

    def getCurrent(self) : 
        return self.courant

    def gotoFather(self):
        self.courant = self.courant.getPere()

    def addBranch(self,t):
    
        if type(self.courant) == type(Feuille(0)):
            
            p = self.courant.getPere()
            v= self.getCurVal()
            g = self.getCurrent()
            self.courant = Noeud(v,[])
            self.courant.setPere(p)

        
        if type(t[0]) != type(NoeudGen(0)):
            for i in t :
                i = Feuille(i)

        self.courant.addfils(t)

        for j in self.courant.getAllFils() :
            j.setPere(g)


        

    def getCurVal(self):
        return self.courant.getVal()

    def setCurVal(self,v):
        self.courant.val = v

    def listify(self,tab): 
        
        
        ptrf = self.getCurrent()
        if type(self.courant)!=type(Feuille(0)):
            
            t = []
            #ptrf sert de pointeur de référence pour repositionner l'element cournat après la remontée de l'arbre
            
            while self.courant != self.root :
                a= self.getCurVal()
                t.append(a)
                self.gotoFather()
            t.append(self.root.getVal())
            t = list(reversed(t))
            return [t]

        elif type(self.courant)==type(Noeud(0,[])):
            for i in range(len(self.courant.fils)) : 
                self.gotoFils(i)
                tab = tab + self.listify(tab)
                self.courant = ptrf
                self.gotoFather
            
            return tab
                
            

    def dispArbre(self):
        
        if type(self.courant)==type(Feuille(0)):
            s = "( "
            s = s + str(self.courant.getVal())
            s = s + " )"
            return s

        elif type(self.courant)==type(Noeud(0,[])):
            s = " ("
            for i in range(len(self.courant.getAllFils())):
                
                self.gotoFils(i)
                s = s + self.dispArbre()
                self.gotoFather()
            s = s + " )"
            return s
                
            


class Solver: 


    def __init__(self,labyrinthe):
        self.inv ={"droite":"gauche","haut":"bas","gauche":"droite","bas":"haut"}
        self.lab = labyrinthe
        self.arbre = Arbreknaire()

#méthode qui calcule récursivement les déplacements possibles sans retour en arrière
    
    def getLab(self):
        return self.lab

    def setLab(self, lb):
        self.lab = lb
    
    def movlist(self,visite,l,tab):
        
        """fonction récursive qui ajoute le chemin l à tab"""
        
        p = self.lab.avanceBis(self.lab.joueurB)
        l1 = l.copy()
        print(p)
        for i in p : 
            l = l1
            self.lab.deplace(i,self.lab.joueurB)
            if self.lab.joueurB not in visite :
                print("ici")
                l = l+ [i]
                visite.append(self.lab.joueurB)
                tab.append(l)
                self.movlist(visite,l,tab)

            self.lab.deplace(self.inv[i],self.lab.joueurB)





 #calcule la liste de toutes les séquences de choix possibles pour un joueur et un tour donné.       
    
    def choix (self,joueur):
        chx = []
        #differentes possibilités de translations ou aucune
        p = self.lab.avanceBis(joueur)
        o = [True,False]
        c = ["droite","haut","gauche","bas"]
        n = [1,2,3,4,5,6,7,8,9]
    
        chx = list(itertools.product(["oui"],o,c,n))
        chx.append("non")
        copielab = self.lab

        #ajouter aux coups possibles tous les déplacements possibles
        
        
        for ch in chx :
            visites = []
            a = Arbreknaire()

            self.lab = copielab
            if ch[0]=="oui":
                self.lab.une_translation(ch[1],ch[2],ch[3])
            if self.lab.joueurB not in visites :
                visites.append(self.lab.joueurB)
            
            self.deplacements(a,visites)
            l = [ch]
            a.listify(l)
            chx.append(ch)
           

        return chx
            
        

        

    def UCB1(self,node):
        
        return 100000000

    def backPropagation(self):
        pass

    def expansion(self):
        pass

    def simulation(self):
        pass


"""
if __name__=="__main__":
    
    
   
    
    
    lb = plat.Labyrinthe()
    lb.DispJeu()
    solver = Solver(lb)
    tableau = []
    solver.movlist([],[],tableau)
    print(tableau)
"""   
