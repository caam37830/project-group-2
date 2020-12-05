import numpy as np
import numpy.linalg as la
#from sklearn.neighbors import BallTree
from scipy.spatial.distance import pdist
import networkx as nx
class Person():
    """
    An agent representing a person.

    """

    def __init__(self):
        self.infected = False # if enlightened = True, the person has heard idea
        self.willinfect = True
        self.pos = np.random.rand(2)

    def allocpos(self,x,y):
        self.pos = np.array([x,y])

    def movepos(self,p):
        dpos = np.random.randn(2)
        dpos = dpos / la.norm(dpos)
        dpos = p*dpos

        pos2 = self.pos+dpos
        if pos2[0]>=0 and pos2[0]<=1 and pos2[1]>=0 and pos2[1]<=1:
            self.pos = pos2



    def is_infected(self):
        """
        returns true if the person has  been infected
        """
        return self.infected

    def is_willinfected(self):
        """
        return true if the person is Susceptible
        """
        return self.willinfect


    def get_infected(self):
        """
        once the person get infected
        """
        self.infected = True
        self.willinfect = False

    def get_recovered(self):
        """
        once the person get recovered
        """
        self.infected = False

    def is_recovered(self):
        """
        if the person is recovered
        """
        return self.infected==False and self.willinfect == False



def count_infect(pop):
    """
    the total infected people
    """
    total = 0
    for i in pop:
        if i.is_infected():
            total = total + 1
    return total

def count_recover(pop):
    """
    the total recovered people
    """
    total = 0
    for i in pop:
        if i.is_recovered():
            total = total + 1
    return total

def count_suspectial(pop):
    """
    the total suspectial people
    """
    total = 0
    for i in pop:
        if i.is_willinfected():
            total = total + 1
    return total


def resetcenter(start,pop):
    for i in range(start):
        pop[i].allocpos(0.5,0.5)

def resetcorner(start,pop):
    k = np.random.choice(4,start)
    for i in range(start):
        """
        if k[i]==0:
            pop[i].allocpos(0,0)
        if k[i]==1:
            pop[i].allocpos(0,1)
        if k[i]==2:
            pop[i].allocpos(1,0)
        if k[i]==3:
            pop[i].allocpos(1,1)
        """
        pop[i].allocpos(0,0)

def calculatedistance(pop):
    length = len(pop)
    X = pop[0].pos
    for i in np.arange(1,len(pop),1):
        X = np.vstack((X,pop[i].pos))
    return X
