
from json.encoder import HAS_UTF8

from re import A, S
import Plateau9 as plat
import Partie9 as game
import random 
import itertools
from copy import copy

from math import sqrt
from math import log

def dist(a,b):
        """distance euclidienne"""
        return (a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1])


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
        self.root = Noeud(0,[])
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
        o = [True,False]
        c = ["droite","haut","gauche","bas"]
        n = [1,2,3,4,5,6,7,8,9]
        rot = [0,1,2,3]

        """rot correspond aux rotations possibles de la case motrice.
        On remarque qu'avant même d'avoir fait les déplacements, la liste des possibilités est grande: 288 coups """

        chx = list(itertools.product(["oui"],rot,o,c,n))
        chx.append(["non"])
        cplab = self.lab.copieLab()
        print(chx)
        
        for i in range(len(chx)) :
            t =[]
            chx[i]=list(chx[i])
            self.lab = cplab.copieLab()
            if chx[i][0]=="oui":
                self.lab.motrice.rotation(chx[i][1])
                self.lab.une_translation(chx[i][2],chx[i][3],chx[i][4])
            self.movlist([],[],t,"bonjour")
            for j in t :
                
                chx.append(chx[i] + j)

            if i>288:
                return chx
        
        
        return chx
            
        

        

    def UCB1(self):
        """UCB1 s'effectue sur le noeud sur lequel on veut calculer la valeur ucb1"""
        ucb = 100000000
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


    def effectMov(self,l):
        """permet d'effectuer les mouvements contenus dans une liste de mouvements (au bon format)"""
        p=1
        if ch[0]=="oui":

            self.lab.motrice.rotation(ch[1])
            self.lab.une_translation(ch[2],ch[3],ch[4])
            l[0:5]=[]
        else :
            l[0:1]=[]
        for d in l:
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
            for i in range(20):
                """empêche le solver de tourner en rond en cas de cycle dans le labyrinthe"""
                p = self.lab.avance(self.lab.joueurB)
                if len(p)==1 :
                    """ si le seul déplacement que l'on peut faire est de rebrousser chemin"""
                    break
                elif  dep in self.inv.keys(): 
                    a = p.index(self.inv[dep])
                    p[a:a+1]=[]
                    a = random.randint(1,len(p))
                    """ a une chance sur len(p) de s'arrêter avant"""
                    if a==1:
                        break
                    else:
                        dep = random.choice(p)
                        self.lab.deplacement(dep,self.lab.joueurB)

            self.arbre.courant.val.setTotal(dist(self.lab.joueurB , self.lab.tresor))
            self.arbre.courant.val.setVi(dist(self.lab.joueurB, self.lab.tresor))

    def mcts(self):
        if type(self.arbre.courant) == type(Feuille(0)):
            
            ni = self.arbre.courant.val.nbex
            if ni ==0:
                self.arbre.courant.val.setNbex(ni +1)
                ptr = self.arbre.getCurrent()
                """la fonction backpropagation nous ramène à la racine. ptr pointe vers l'ancienne feuille courante"""
                self.simulation()
                """simulation d'une partie depuis la configuration courante"""
                self.backPropagation()
                """mise à jour des valeurs pour tous les noeuds courants"""
                self.arbre.courant = ptr
            choices = self.choix()
            for c in range(len(choices)):
                """ajouter chaque choix possible au fils et ajouter l'action nécessaire."""
                self.arbre.addBranch([Feuille(c[i])])
                self.arbre.courant.getFils(i).val.addaction(c[i])

            if len(self.arbre.courant.getAllFils)!=0:
                self.arbre.gotoFils(0)
                self.arbre.courant.val.setNbex(1)
                self.simulation()
        else :
            t = self.arbre.courant.getAllFils()
            k=0
            min =-100000000
            """obtenir argmax(i, UCB1(fils(i))"""
            for i in range(len(t)):
                self.arbre.gotoFils(i)
                if min < self.UCB1():
                    k=i
                    min = self.UCB1
                self.arbre.gotoFather()
                """effectuer l'action du fils k pour chaner la configuration du jeu"""
                self.effectMov(self.courant.val.act[k])
            self.arbre.gotoFils(k)
            self.mtcs()
                    
                

                


    def monteCarloTreeSearch(self,n):
        """fonction finale du Solver. n est le nombre d'itérations souhaité retourne un tableau d'instruction"""
        cplb = self.lab.copieLab()
        for i in range(n):
            self.lab = cplb.copieLab()
            self.arbre.courant = self.arbre.root
            self.mcts()
        """retourner l'action qui maximise vi"""
        t = self.arbre.root.getAllFils()
        k=0
        max = -100000000
        for i in t:
            if max < i.val.vi: 
                max = i.val.vi
                k=t.index(i)
        return self.arbre.root.val.act[k]





if __name__=="__main__":
    
    lb = plat.Labyrinthe()
    solver = Solver(lb)
    a = Arbreknaire()
    solver.mcts()

    
    

