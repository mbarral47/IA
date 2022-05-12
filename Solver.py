
from re import A


class NoeudGen : 
    
    def __init__(self,v):
        self.val=v

    def getVal(self):
        return val

    def toString(self):
        s=""
        if type(self)==type(Noeud(None,None)) : 
            s= s+"( "
            s=s+str(self.val)
            for i in range(len(self.fils)):
                a = self.t[i]
                s = s+a.toString()
            s=s+" )"
            return s
        else: 
            s=s+" ("
            s = s+self.val
            s=s+" )"
            return s
            
            
            


class Feuille (NoeudGen):
    def __init__(self,v):
        self.val =v

class Noeud(NoeudGen):
    def __init__(self,t,v):
        self.fils=t
        self.val=v

    def makeFeuille(self):
        v =self.getVal()
        self=Feuille(v)

    def addfils(self,f):
        self.fils.append(f)
        

class Arbreknaire():
    pass


class Solver: 


    def __init__(self):
        pass

    def UCB1(self):
        pass

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
    print(n.toString())




