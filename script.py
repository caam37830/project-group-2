import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from sir.agent import *
import numpy as np
import matplotlib.pyplot as plt


# Agent-based simulations and plots

def run_Simulation2(b, k, N=100, T=10, start = 1):
    """
    run the simulation for the population
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
                contacts = np.random.randint(N, size=b)
                for l in contacts:
                    if pop[l].is_willinfected():
                        pop[l].get_infected()

        for j in range(N):
            if pop[j].is_infected():
                if np.random.rand() < k:
                    pop[j].get_recovered()

        recover.append(count_recover(pop))
        infect.append(count_infect(pop))
        suspect.append(count_suspectial(pop))

    plt.plot(range(T+1), recover, label = "recoverpeople")
    plt.plot(range(T+1), suspect, label = "suspectpeople")
    plt.plot(range(T+1), infect, label = "infectpeople")
    plt.legend()
    plt.show()


def checktotalinfect(b, k, N, T, start = 1):
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
                contacts = np.random.randint(N, size=b)
                for l in contacts:
                    if pop[l].is_willinfected():
                        pop[l].get_infected()

        for j in range(N):
            if pop[j].is_infected():
                if np.random.rand() < k:
                    pop[j].get_recovered()

    return [count_infect(pop)/N, (count_infect(pop)+count_recover(pop))/N]


def plotphasediagram(blist, klist, N, T, start):
    cts = np.zeros((len(blist), len(klist)))
    for j,b in enumerate(blist):
        for i,k in enumerate(klist):
            cts[j,i] = checktotalinfect(b, k, N, T, start)[1]

   # plt.figure(figsize=(8,10))
    plt.imshow(cts,extent=[np.min(klist), np.max(klist), np.min(blist), np.max(blist)], interpolation="nearest", aspect="auto")
    plt.colorbar()
    plt.title("Percentage of Population Infected and Removed \n T = "+str(T)+", Discrete")
    plt.xlabel("k")
    plt.ylabel("b")
    plt.show()
    

def plotphasediagraminfect(blist, klist, N, T, start):
    cts = np.zeros((len(blist), len(klist)))
    for j,b in enumerate(blist):
        for i,k in enumerate(klist):
            cts[j,i] = checktotalinfect(b, k, N, T, start)[0]

   # plt.figure(figsize=(8,10))
    plt.imshow(cts,extent=[np.min(klist), np.max(klist), np.min(blist), np.max(blist)], interpolation="nearest", aspect="auto")
    plt.title("Percentage of Population Infected \n T= " + str(T) + ", Discrete")
    plt.colorbar()
    plt.xlabel("k")
    plt.ylabel("b")
    plt.show()
    

run_Simulation2(2, 0.3, N=10000, T=50, start=100)
run_Simulation2(5, 0.5, N=10000, T=100, start=100)

#Now firstly, we try to discover the total percentage of
#infected at T = 10,50, 100, 200 days
blist = np.arange(10, 0, -1)
klist = np.arange(0, 1, 0.1)
plotphasediagram(blist, klist, N = 20000, T = 10, start = 100)
plotphasediagram(blist, klist, N = 20000, T = 20, start = 100)
plotphasediagram(blist, klist, N = 20000, T = 30, start = 100)
#Coclusion: The percentage of infected at time >10 days mainly depend on the b.If b > 5(5 Susceptible people
#infected once contact a suspectible person, then all of them will be infected), then all the person will be infected very early no matter what i is
#if b<=5, then if the recoverrate is very high there will be small amount of people being infected

#Secondly, we try to discover the part of regimes that i will quickly go to 0
#We also observe the diagram we have already observed,

plotphasediagraminfect(blist, klist, N=20000, T = 10, start = 100)
plotphasediagraminfect(blist, klist, N=20000, T = 20, start = 100)
plotphasediagraminfect(blist, klist, N=20000, T = 30, start = 100)
#Conclusion:
#The percentage of infected people will quickly goes to 0, if the recovered rate R is large.A small amount of b will
#accelerate the process of decreasing percentage of infected people but the main factor is the recover rate R.
#

#Finally we will try to discover in which case no people recovered
#We can check that through the phasediagram. If the b is very large(b>5), even if the recovered rate is high, All the people will be infected





# ODE simulations and plots

def odesimulation(t, x, b, k):
    s = x[0]
    i = x[1]
    r = x[2]
    ds = -b*s*i
    di = b*s*i-k*i
    dr = k*i
    return np.array([ds, di, dr])


def convertvector(x):
    s = x[0]
    i = x[1]
    r = x[2]
    return np.array([s/(s+i+r), i/(s+i+r), r/(s+i+r)])


def runodesimulation(tspan, xstart, b, k, teval):
    xstart = convertvector(xstart)
    sol = solve_ivp(odesimulation, tspan, xstart, args = (b,k), t_eval = teval)
    plt.plot(sol.t, sol.y[0], label ="suspectial people")
    plt.plot(sol.t, sol.y[1], label ="infected people")
    plt.plot(sol.t, sol.y[2], label ="recovered people")
    plt.title("odesimulation with s = " + str(xstart[0]) + "i = "+str(xstart[1]))
    plt.xlabel("days")
    plt.ylabel("percentage")
    plt.legend()
    plt.show()

    
def checktotalinfectpeople(x, b, k, T):
    x = convertvector(x)
    tspan = (0, T)
    xstart = x
    teval = np.linspace(0, T, 200);
    sol = solve_ivp(odesimulation, tspan, xstart, args=(b,k), t_eval = teval)
    totalinfect = sol.y[2][-1] + sol.y[1][-1]
    infect = sol.y[1][-1]
    return np.array([totalinfect, infect])


def plotodephasediagram(x, blist, xlist, T):
    cts = np.zeros((len(blist), len(xlist)))
    for j,b in enumerate(blist):
        for i,k in enumerate(klist):
            cts[j, i] = checktotalinfectpeople(x, b, k, T)[0]
    plt.imshow(cts,extent=[np.min(klist), np.max(klist), np.min(blist), np.max(blist)], 
               interpolation="nearest", aspect='auto')
    plt.colorbar()
    plt.title("Percentage of Population Removed and Infected \n T = " + str(T) + ", Continuous")
    plt.xlabel("k")
    plt.ylabel("b")
    plt.show()


def plotodeinfectphasediagram(x, blist, xlist, T):
    cts = np.zeros((len(blist), len(xlist)))
    for j,b in enumerate(blist):
        for i,k in enumerate(klist):
            cts[j, i] = checktotalinfectpeople(x, b, k, T)[1]
    plt.imshow(cts,extent=[np.min(klist), np.max(klist), np.min(blist), np.max(blist)], 
               interpolation="nearest", aspect='auto')
    plt.colorbar()
    plt.title("Percentage of Population Infected \n T = " + str(T) + ", Continuous")
    plt.xlabel("k")
    plt.ylabel("b")
    plt.show()

tspan = (0, 20)
xstart = np.array([4500, 500, 0])
teval = np.linspace(0, 20, 200);
runodesimulation(tspan, xstart, 8, 0.4, teval)
tspan2 = (0, 30)
xstart2 = np.array([9800, 200, 0])
teval2 = np.linspace(0, 30, 300);
runodesimulation(tspan2, xstart2, 4, 0.95, teval2);
blist = np.arange(10, 0, -1)
klist = np.arange(0, 1, 0.1)
plotodephasediagram(np.array([790000, 10, 0]), blist,klist, 10)
plotodephasediagram(np.array([790000, 10, 0]), blist,klist, 20)
plotodephasediagram(np.array([790000, 10, 0]), blist,klist, 30)
plotodeinfectphasediagram(np.array([790000, 10, 0]), blist,klist, 10)
plotodeinfectphasediagram(np.array([790000, 10, 0]), blist,klist, 20)
plotodeinfectphasediagram(np.array([790000, 10, 0]), blist,klist, 30)



