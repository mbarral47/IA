
from re import A
import Plateau as plat
import Partie as game
import random 
import itertools


    

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
                print(type(a))
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


class Noeud(NoeudGen):
    def __init__(self,v,t):
        self.fils=t
        for i in t :
            if type(t[i])!=type(NoeudGen(0)):
                t[i]==Noeud(0,None,None)
            i.setPere(self)
        self.val=v

        

    def makeFeuille(self):
        v =self.getVal()
        p = self.getPere
        self=Feuille(v)
        self.setPere(p)

    def addfils(self,f):
        for i in f : 
            if type(i)!=type(NoeudGen(0)):
                i==Noeud(0,[])
        self.fils = self.fils +f
        for i in range(len(self.fils)): 
            self.fils[i].setPere(self)

    def getFils(self,i):
        return self.fils[i]
        

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
        self.root = Noeud(0,[])
        self.root.setPere(self.root)
        self.courant = self.root


    def gotoFils(self,i):
        self.courant = self.courant.getFils(i)

    def gotoFather(self):
        self.courant = self.courant.getPere()

    def addBranch(self,t):
        fils = self.courant.addfils(t)
        

    def getCurVal(self):
        return self.courant.getVal()

    


class Solver: 

    
    def __init__(self,lab):
        self.Base = lab
        self.arbre = Arbreknaire()

    def deplacements(self, n, pred,t):
        p = self.Base.avanceBis(self.Base.joueurB)
        for deplacement in p :
            if p[n] != pred[(n+2)%2]:

                tabi = t
                tabi.append(p[n])
                self.deplacement(self,pred,tabi)
                


        
    def choix (self, joueur):
        chx = []
        p = self.lab.avanceBis(joueur)
        
        o = [True,False]
        c = ["droite","haut","gauche","bas"]
        n = [1,2,3,4,5,6,7,8,9]
        self.lab.une_translation(o, c, n)
        p = self.lab.avanceBis(joueur)

        chx = list(itertools.product(["oui"],o,c,n))
        chx.append("non")


        return chx
            
        

        

    def UCB1(self,node):
        
        return 100000000

    def backPropagation(self):
        pass

    def expansion(self):
        pass

    def simulation(self):
        pass



if __name__=="__main__":
    f1= Feuille("a")
    f2 = Feuille("b")
    t = [f1,f2]
    a = Arbreknaire()
    a.addBranch(t)
    print(a.getCurVal())
    a.gotoFils(0)
    print(a.getCurVal())



