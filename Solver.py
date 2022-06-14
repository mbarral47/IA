
from json.encoder import HAS_UTF8

from re import A, S
import Plateau9 as plat
import Partie9 as game
import random 
import itertools
from copy import copy

from math import sqrt
from math import log
from math import exp

def heuristique(a,b):
        """distance euclidienne"""
        return 1000 * exp (   -((a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]))   )


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
        
        c = 1
        if type(self)==type(Noeud(None,None)):
    
            for i in range(len(self.fils)):
                a = self.getFils(i)
                c =c + a.count()
        return c



class Feuille(NoeudGen):
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

    def gotoRoot(self):
        self.courant = self.root

    def addBranch(self,t):
    
        if type(self.courant) == type(Feuille(0)):
            g = self.getCurrent()
            p= g.getPere()
            v= g.getVal()
            g = Noeud(v,[])
            g.setPere(p)
            
            if self.courant == self.root:
                self.root=g
            self.courant = g
            
    
        
        if type(t[0]) != type(NoeudGen(0)):
            for i in t :
                i = Feuille(i)

        self.courant.addfils(t)
        g = self.getCurrent()
        for j in self.courant.getAllFils() :
            j.setPere(g)

    def getCurVal(self):
        return self.courant.getVal()

    def setCurVal(self,v):
        self.courant.val = v  


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
                
class SNode :
    """ Type de valeurs contenue dans les noeuds du solver"""
    
    def __init__(self):
        self.nbex=0
        """nombre d'exploration du noeud"""
        self.total =0
        """total des valeurs moyennes des noeuds fils"""
        self.vi = 0
        """valeur moyenne sur le nombre des fils"""
        self.act = []
        """chaque case du tableau correspond au coups à jouer pour arriver à un état fils"""

    def setVi(self,v):
        self.vi=v
    
    def setTotal(self,v):
        self.total=v

    def setNbex(self,v):
        self.nbex=v
    
    def addaction(self,a):
        self.act.append(a)

    def getNbex(self):
        return self.nbex

    def getTotal(self):
        return self.total
    
    
class Solver: 


    def __init__(self,labyrinthe):
        self.inv ={"droite":"gauche","haut":"bas","gauche":"droite","bas":"haut"}
        self.lab = labyrinthe
        self.arbre = Arbreknaire()
        self.arbre.root.val = SNode()


    
    def getLab(self):
        return self.lab

    def setLab(self, lb):
        self.lab = lb
    
    def movlist(self,visite,l,tab,pred):
        

        l = list(l)
        visite = list(visite)
        p = self.lab.avance(self.lab.joueurB)
        l1 = l.copy()
        v1 = visite.copy()

        """filtrer p pour empêcher de rebrousser chemin"""
        
        if pred in p : 
            a = p.index(pred)
            a= int(a)
            p[a:a+1]=[]
        
        for i in p : 
            """nb les copy() sont necessaires pour pouvoir utiliser la récursivité. Sinon les paramètres d'entrée seraient
            modifiés d'un noeud frère à l'autre"""
            l = l1.copy()
            visite = v1.copy()
            n = len(visite)
            
            self.lab.deplace(i,self.lab.joueurB)
            """filter le deplacement pour empecher un cycle """
            if self.lab.joueurB not in visite:
                
                l.append(i)
                visite.append(self.lab.joueurB.copy())
                tab.append(l)
                self.movlist(visite,l,tab,self.inv[i])

            self.lab.deplace(self.inv[i],self.lab.joueurB)

 

      
    
    def choix (self):
        """calcule la liste de toutes les séquences de choix possibles pour un joueur et un tour donné."""      
        chx = []
        o = ["ligne","colonne"]
        c = ["droite","haut","gauche","bas"]
        n = [1,3,5,7]
        rot = [0,1,2,3]

        """rot correspond aux rotations possibles de la case motrice.
        On remarque qu'avant même d'avoir fait les déplacements, la liste des possibilités est grande: 64"""

        ch1 = list(itertools.product(["oui"],rot,["ligne"],["droite","gauche"],n))
        ch2 = list(itertools.product(["oui"],rot,["colonne"],["haut","bas"],n))
        chx = ch1 + ch2
        chx.append(["non"])
        cplab = self.lab.copieLab()
    
        for i in range(len(chx)) :
            t =[]
            chx[i]=list(chx[i])
            self.lab = cplab.copieLab()
            if chx[i][0]=="oui":
                self.lab.motrice.rotation(chx[i][1])
                self.lab.une_translation(chx[i][2],chx[i][3],chx[i][4])
            self.movlist([],[],t,"bonjour")
            for j in t :

                tab = j.copy()
                chx.append(chx[i].copy() + tab)

            if i>288:
                return chx
        choix2 = chx[:65]
        chx[:65]=[]
        chx = choix2 + chx
        return chx
            
        

        

    def UCB1(self):
        """UCB1 s'effectue sur le noeud sur lequel on veut calculer la valeur ucb1"""
        ucb = 1000
        if self.arbre.courant.getVal().nbex !=0:
            
            ni =self.arbre.courant.getVal().nbex
            npere = self.arbre.courant.getPere().getVal().nbex
            v = self.arbre.courant.getVal().vi

            ucb = v + 2*sqrt(log(ni)/npere)

            """si  le nombre d'exploration n'est pas nul, appliquer la formule"""
        return ucb

    def backPropagation(self):
        """Permet de changer toutes les valeur moyenne des parents d'une feuille."""
        
        while self.arbre.courant != self.arbre.root :
            self.arbre.gotoFather()
            n = len(self.arbre.courant.getAllFils())
            m=0
            for i in range(n):
    
                m = m+int(self.arbre.courant.getFils(i).getVal().total)
            self.arbre.courant.val.setTotal(m)
            self.arbre.courant.val.setVi(m/n)


    def effectMov(self,ch):
        """permet d'effectuer les mouvements contenus dans une liste de mouvements (au bon format)"""
        p=1
        c = ch.copy()
        if c[0]=="oui":

            self.lab.motrice.rotation(c[1])
            self.lab.une_translation(c[2],c[3],c[4])
            c[0:5]=[]
        else :
            c[0:1]=[]
        for d in c:
            self.lab.deplace(d,self.lab.joueurB)


    def simulation(self,n,k):
        """il n'est pas certain que la simulation converge vers un état terminal, c'est pourquoi n limite le nombre
        de tour."""
        for i in range(n):
            a = random.randint(0,1)
            if a==1:
                rot = random.randint(0,3)
                opt = random.choice(["ligne","colonne"])
                if opt =="ligne":
                    cote = random.choice(["droite","gauche"])
                else:
                    cote = random.choice(["haut","bas"])
                num = random.choice([1,3,5,7])
                self.lab.motrice.rotation(rot)
                self.lab.une_translation(opt,cote,num)
            
            dep = "rien"
            for i in range(k):
                """empêche le solver de tourner en rond en cas de cycle dans le labyrinthe"""
                p = self.lab.avance(self.lab.joueurB)
                if len(p)==0 :
                    """ si le seul déplacement que l'on peut faire est de rebrousser chemin"""
                    break
                else : 
                    if (dep in self.inv.keys() )and (self.inv[dep] in p) :
                        a = p.index(self.inv[dep])
                        p[a:a+1]=[]
                    e = random.randint(1,1+len(p))
                    """ a une chance sur len(p)+1 de s'arrêter avant"""
                    if e==1 or p==[]:    
                        break
        
                dep = random.choice(p)
                self.lab.deplace(dep,self.lab.joueurB)
                
            
            self.arbre.courant.val.setTotal(heuristique(self.lab.joueurB , self.lab.tresor))
            self.arbre.courant.val.setVi(heuristique(self.lab.joueurB, self.lab.tresor))

    def mcts(self):
        
        if type(self.arbre.courant) == type(Feuille(0)):
            
            ni = self.arbre.courant.val.getNbex()
            if ni ==0:

                self.arbre.courant.val.setNbex(ni +1)
                ptr = self.arbre.getCurrent()
                

                lb = self.lab.copieLab()
                self.simulation(10,10)
                self.backPropagation()
                self.lab=lb.copieLab()

                self.arbre.courant = ptr
                
            choices = self.choix()
            for i in range(len(choices)):
                """ajouter chaque choix possible au fils et ajouter l'action nécessaire."""
                sn = SNode()
                self.arbre.addBranch([Feuille(sn)])
                self.arbre.courant.val.addaction(choices[i])


            
            
            if len(self.arbre.courant.getAllFils())!=0:
                self.effectMov(self.arbre.courant.val.act[0])
                self.arbre.gotoFils(0)
                self.arbre.courant.val.setNbex(1)
                self.simulation(10,10)
        else :
            
            """ si ce n'est pas un noeud feuille continuer l'exploration"""
            t = self.arbre.courant.getAllFils()
            k=0
            max =-100000000
            """obtenir argmax(i, UCB1(fils(i))"""
            for i in range(len(t)):
                self.arbre.gotoFils(i)
                cmp = int(self.UCB1())

                if max <= cmp:
                    k=i
                    max = cmp
                self.arbre.gotoFather()
                """effectuer l'action du fils k pour chaner la configuration du jeu"""
            self.effectMov(self.arbre.courant.val.act[k])
            self.arbre.gotoFils(k)
            self.mcts()
            
                

                


    def monteCarloTreeSearch(self,n):
        """fonction finale du Solver. n est le nombre d'itérations souhaité retourne un tableau d'instruction"""
        cplb = self.lab.copieLab()
        for i in range(n):
            self.lab = cplb.copieLab()
            self.arbre.courant = self.arbre.root
            self.mcts()
            self.arbre.gotoRoot()
        """retourner l'action qui maximise vi"""
        self.lab=cplb.copieLab()
        t = self.arbre.root.getAllFils()
        k=0
        max = -100000000
        for i in t:
            if max < i.val.vi: 
                max = i.val.vi
                k=t.index(i)

        return self.arbre.root.val.act[k]



"""
if __name__=="__main__":
    

    lb = plat.Labyrinthe()
    lb1 = lb.copieLab()
    solver = Solver(lb)
    lbd2 = solver.lab.copieLab()
    t = solver.monteCarloTreeSearch(10)

    print(t)
    
   
"""
