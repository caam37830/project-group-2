import sys
import os
import numpy as np
import math
sys.path.append("../")
from sir.improveagent import *
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from sklearn.neighbors import BallTree
from scipy.spatial import KDTree
from scipy.spatial import cKDTree
from scipy.spatial.distance import pdist
import networkx as nx

p = Person()

def run_Simulation2(k,N=100,T=10,start = 1,p=0.5,q=0.08,startcenter = False,startcorner=False):
    """
    run the simulation for the pop
    """
    recover = [0]
    infect  = [start]
    suspect = [N-start]
    pop = [Person() for i in range(N)]
    ##we need to change the code for the case start people infected
    for i in range(start):
        pop[i].get_infected();
    if(startcenter):
        resetcenter(start,pop)
    if(startcorner):
        resetcorner(start,pop)
    np.random.seed(10)
    for i in range(T):
        for j in range(N):
             pop[j].movepos(p)
        X = calculatedistance(pop)
        tree = cKDTree(X)
        for j in range(N):
             if pop[j].is_infected():
                addvalue = np.array([X[j]])
                inds = tree.query_ball_point(addvalue, q)
                inds = inds[0]
                #may have problem here
                for l in inds:
                    if pop[l].is_willinfected():
                        pop[l].get_infected()

        for j in range(N):
            if pop[j].is_infected():
                if np.random.rand()< k:
                    pop[j].get_recovered()

        recover.append(count_recover(pop))
        infect.append(count_infect(pop))
        suspect.append(count_suspectial(pop))
    newrecover = [i/N for i in recover]
    newsuspect = [s/N for s in suspect]
    newinfect = [i/N for i in infect]
    plt.plot(range(T+1),newrecover,label = "recoverpeople")
    plt.plot(range(T+1),newsuspect,label = "suspectpeople")
    plt.plot(range(T+1),newinfect,label = "infectpeople")
    plt.legend()
    plt.show()


#We run a simulation here,use the default value of p and q
run_Simulation2(0.6,N=20000,T = 30,start=10)

def checkinfectb(k,N,T,start=1,p=0.5,q=0.08,startcenter = False,startcorner=False):
    """
    we use this function for checking the total infected people
    """
    recover = [0]
    infect  = [start]
    suspect = [N-start]
    pop = [Person() for i in range(N)]
    np.random.seed(10)
    for i in range(start):
        pop[i].get_infected();
    if(startcenter):
        resetcenter(start,pop)
    if(startcorner):
        resetcorner(start,pop)
    np.random.seed(10)
    for i in range(T):
        for j in range(N):
            pop[j].movepos(p)
        X = calculatedistance(pop)
        tree = cKDTree(X)
        for j in range(N):
            if pop[j].is_infected():
                addvalue = np.array([X[j]])
                inds = tree.query_ball_point(addvalue, q)
                inds = inds[0]
                for l in inds:
                    if pop[l].is_willinfected():
                        pop[l].get_infected()
        for j in range(N):
            if pop[j].is_infected():
                if np.random.rand()<k:
                    pop[j].get_recovered()
    return np.array([(count_infect(pop)+count_recover(pop))/N,count_infect(pop)/N])



def plotcenterrange():
    """
    show how the total infected people i change with p start from center
    """
    plist1 = np.arange(0.02,0.1,0.02)
    plist = np.arange(0.1,1,0.1)
    infectlist = []
    for i in plist1:
        infectlist.append(checkinfectb(0.5,20000,30,200,p = i,q = np.sqrt(2/(20000*math.pi)),startcenter=True)[0])
    for i in plist:
        infectlist.append(checkinfectb(0.5,20000,30,200,p = i,q = np.sqrt(2/(20000*math.pi)),startcenter=True)[0])
    plt.plot(np.hstack((plist1,plist)),infectlist)
    plt.title("centerplot")
    plt.xlabel("change of p")
    plt.ylabel("change of total infected people")
    plt.show()

plotcenterrange()




def plotrandomcornerrange():
    """
    show how the i value change with p
    """
    plist1 = np.arange(0.02,0.1,0.02)
    plist = np.arange(0.1,1,0.1)
    infectlist = []
    infectlist2 = []
    infectlist3 = []
    for i in plist1:
        infectlist.append(checkinfectb(0.5,20000,30,200,p = i,q = np.sqrt(2/(20000*math.pi)),startcorner=True)[0])
        infectlist2.append(checkinfectb(0.5,20000,30,200,p = i,q = np.sqrt(2/(20000*math.pi)))[0])
        infectlist3.append(checkinfectb(0.5,20000,30,200,p = i,q = np.sqrt(2/(20000*math.pi)),startcenter = True)[0])
    for i in plist:
        infectlist.append(checkinfectb(0.5,20000,30,200,p = i,q = np.sqrt(2/(20000*math.pi)),startcorner=True)[0])
        infectlist2.append(checkinfectb(0.5,20000,30,200,p = i,q = np.sqrt(2/(20000*math.pi)))[0])
        infectlist3.append(checkinfectb(0.5,20000,30,200,p = i,q = np.sqrt(2/(20000*math.pi)),startcenter = True)[0])
    plt.plot(np.hstack((plist1,plist)),infectlist,label = "corner")
    plt.plot(np.hstack((plist1,plist)),infectlist2,label = "random")
    plt.plot(np.hstack((plist1,plist)),infectlist3,label = "center")
    plt.title("Change from random corner center")
    plt.xlabel("change of p")
    plt.ylabel("change of total infected people")
    plt.legend()
    plt.show()

plotrandomcornerrange()
