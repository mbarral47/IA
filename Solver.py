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
            i.setPere(self)
        self.val=v

        

    def makeFeuille(self):
        v =self.getVal()
        self=Feuille(v)

    def addfils(self,f):
        self.fils.append(f)

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
        fils = self.courant.getFils()
        fils = fils.append(t)
        self.courant.setFils(fils)



    


class Solver: 

    
    def __init__(self,lab):
        self.Base = lab
        self.arbre = Arbreknaire()
        
    def choix (self, joueur):
       
        p = self.lab.avanceBis(joueur)
        print("direction(s) possible(s) pour votre joueur: \n", p)
        t = ["oui","non"]
        if (t=="oui"):
            
            o = [True,False]
            c = ["droite","haut","gauche","bas"]
            n = range(1,10)
            self.lab.une_translation(o, c, n)
            p = self.lab.avanceBis(joueur)
            print("Nouvelles direction(s) possible(s) pour votre joueurA: \n", p)
            dir = input("indiquez une direction: ")
        elif p!=[]:
            dir = input("indiquez une direction: ")
        else:
            print("impossible de bouger une translation aurait été plus judicieux")

        

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
    n=Noeud("c",t)
    print(type(n)==type(Noeud(None,None)))
    print(f1.getVal())
    print(n.count())









