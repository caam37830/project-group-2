###We have the simulation for several cases
#b = 2,k = 0.3,N=10000,T=50,startnumber = 100
#b = 2,k=0.5,N=10000,T = 100,startnumber = 100

from agent import *
import numpy as np
import matplotlib.pyplot as plt
def run_Simulation2(b,k,N=100,T=10,start = 1):
    """
    run the simulation for the pop
    """
    recover = [0]
    infect  = [start]
    suspect = [N-start]
    pop = [Person() for i in range(N)]
    ##we need to change the code for the case start people infected
    pop[0].get_infected();
    np.random.seed(10)
    for i in range(T):
        for j in range(N):
             if pop[j].is_infected():
                contacts = np.random.randint(N,size=b)
                for l in contacts:
                    if pop[l].is_willinfected():
                        pop[l].get_infected()

        for j in range(N):
            if pop[j].is_infected():
                if np.random.rand()< k:
                    pop[j].get_recovered()

        recover.append(count_recover(pop))
        infect.append(count_infect(pop))
        suspect.append(count_suspectial(pop))

    plt.plot(range(T+1),recover,label = "recoverpeople")
    plt.plot(range(T+1),suspect,label = "suspectpeople")
    plt.plot(range(T+1),infect,label = "infectpeople")
    plt.legend()
    plt.show()


def checktotalinfect(b,k,N,T,start=1):
    """
    check the total infected people and infected people respectively in a simulation
    """
    recover = [0]
    infect  = [start]
    suspect = [N-start]
    pop = [Person() for i in range(N)]
    for i in range(start):
        pop[i].get_infected();
    np.random.seed(10)
    for i in range(T):
        for j in range(N):
             if pop[j].is_infected():
                contacts = np.random.randint(N,size=b)
                for l in contacts:
                    if pop[l].is_willinfected():
                        pop[l].get_infected()

        for j in range(N):
            if pop[j].is_infected():
                if np.random.rand()< k:
                    pop[j].get_recovered()

    return [count_infect(pop)/N,(count_infect(pop)+count_recover(pop))/N]


def plotphasediagram(blist,klist,N,T,start):
    """
    plot the phase diagram for the total infected people including the recovered
    """
    cts = np.zeros((len(blist), len(klist)))
    for j,b in enumerate(blist):
        for i,k in enumerate(klist):
            cts[j,i] = checktotalinfect(b,k,N,T,start)[1]
    print("The percentage of infection for different k,b")
    print(cts)

    plt.imshow(cts,extent=[np.min(klist),np.max(klist),np.min(blist),np.max(blist)])
    plt.colorbar()
    plt.xlabel("k")
    plt.ylabel("b")


def plotphasediagraminfect(blist,klist,N,T,start):
    """
    plot the change of i with different behaviour of k ,b
    """
    cts = np.zeros((len(blist), len(klist)))
    for j,b in enumerate(blist):
        for i,k in enumerate(klist):
            cts[j,i] = checktotalinfect(b,k,N,T,start)[0]
    print("The percentage of i for different k,b")
    print(cts)

    plt.imshow(cts,extent=[np.min(klist),np.max(klist),np.min(blist),np.max(blist)])
    plt.colorbar()
    plt.xlabel("k")
    plt.ylabel("b")

#We do the simulation here
run_Simulation2(2,0.3,N=10000,T=50,start=100)
run_Simulation2(5,0.5,N=10000,T=100,start=100)

#Now firstly, we try to discover the total percentage of
#infected(including recovered people) at T = 10,20, 30days
blist = np.arange(10,0,-1)
klist = np.arange(0,1,0.2)

fig = plt.figure()
plt.subplot(1,3,1)
plotphasediagram(blist,klist,N=2000,T=10,start = 100)
plt.subplot(1,3,2)
plotphasediagram(blist,klist,N=2000,T=20,start = 100)
plt.subplot(1,3,3)
plotphasediagram(blist,klist,N=2000,T=30,start = 100)
plt.show()
#Coclusion: The percentage of infected at time >10 days mainly depend on the b.If b > 5(5 Susceptible people
#infected once contact a suspectible person, then all of them will be infected), then all people will be infected very early no matter what recovered rate is
#if b<=5, then if the recoverrate is very high there will be small amount of people being infected finally

#Secondly, we try to discover the part of regimes that i will quickly go to 0
#We also observe the diagram we have already observed,

fig = plt.figure()
plt.subplot(1,3,1)
plotphasediagraminfect(blist,klist,N=2000,T=10,start = 100)
plt.subplot(1,3,2)
plotphasediagraminfect(blist,klist,N=2000,T=20,start = 100)
plt.subplot(1,3,3)
plotphasediagraminfect(blist,klist,N=2000,T=30,start = 100)
plt.show()
#Conclusion:
#The percentage of infected people will quickly goes to 0, if the recovered rate R is large.A small amount of b will
#accelerate the process of decreasing percentage of infected people but the main factor is the recover rate R.
#

#Finally we will try to discover in which case no people susceptible.
#We can check that through the phasediagram. If b is very large(b>5), even if the recovered rate is high unless extremely close to 1, All the people will be infected
#if b is not large, a recover rate that is greater than 0.5 will lead to the consequence that there will always be remained susceptible people and not all people will be infected
