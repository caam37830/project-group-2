import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from sir.agent import *
import numpy as np
import matplotlib.pyplot as plt


# Agent-based simulations and plots

def run_Simulation2(b, k, N=100, T=10, start = 1):
    """
    Run the discrete simulation and plot s, i, r 
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
    newrecover = [i/N for i in recover]
    newsuspect = [s/N for s in suspect]
    newinfect = [i/N for i in infect]
    plt.plot(range(T+1), recover, label = "r: percentage of removed")
    plt.plot(range(T+1), suspect, label = "s: percentage of susceptible")
    plt.plot(range(T+1), infect, label = "i: percentage of infected")
    plt.legend()
    plt.show()

    
def checktotalinfect(b, k, N, T, start = 1):
    """
    Compute the total percentage of the population infected (i+r) and 
    percentage of the population infected (i)
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
                contacts = np.random.randint(N, size = b)
                for l in contacts:
                    if pop[l].is_willinfected():
                        pop[l].get_infected()

        for j in range(N):
            if pop[j].is_infected():
                if np.random.rand() < k:
                    pop[j].get_recovered()

    return [count_infect(pop)/N, (count_infect(pop)+count_recover(pop))/N]



def plotphasediagram(blist, klist, N, T, start):
    """
    Generate phase diagram of total percentage of the population infected (i+r)
    """
    cts = np.zeros((len(blist), len(klist)))
    for j,b in enumerate(blist):
        for i,k in enumerate(klist):
            cts[j,i] = checktotalinfect(b, k, N, T, start)[1]

    plt.imshow(cts,extent=[np.min(klist), np.max(klist), np.min(blist), np.max(blist)], interpolation="nearest", aspect="auto")
    plt.colorbar()
    plt.title("Percentage of Population Infected and Removed \n T = " + str(T) + ", Discrete")
    plt.xlabel("k")
    plt.ylabel("b")
    plt.show()
    

def plotphasediagraminfect(blist, klist, N, T, start):
    """
    Generate phase diagram of percentage of the population infected (i)
    """
    cts = np.zeros((len(blist), len(klist)))
    for j,b in enumerate(blist):
        for i,k in enumerate(klist):
            cts[j,i] = checktotalinfect(b, k, N, T, start)[0]

    plt.imshow(cts,extent=[np.min(klist), np.max(klist), np.min(blist), np.max(blist)], interpolation="nearest", aspect="auto")
    plt.title("Percentage of Population Infected \n T= " + str(T) + ", Discrete")
    plt.colorbar()
    plt.xlabel("k")
    plt.ylabel("b")
    plt.show()
    

# Produce some plots of how s, i, and r change over the length of the simulation 
# Fix b = 2
run_Simulation2(b = 2, k = 0.3, N=20000, T=35, start=100) 
run_Simulation2(b = 2, k = 0.5, N=20000, T=35, start=100)
run_Simulation2(b = 2, k = 0.8, N=20000, T=35, start=100)

# Fix b = 5
run_Simulation2(b = 5, k = 0.3, N=20000, T=35, start=100)
run_Simulation2(b = 5, k = 0.5, N=20000, T=35, start=100)
run_Simulation2(b = 5, k = 0.8, N=20000, T=35, start=100)



# Generate phase diagrams at T = 10, 20, 30 days
# For total percentage of the population infected
blist = np.arange(10, 0, -1)
klist = np.arange(0, 1.1, 0.1)
plotphasediagram(blist, klist, N = 20000, T = 10, start = 100)
plotphasediagram(blist, klist, N = 20000, T = 20, start = 100)
plotphasediagram(blist, klist, N = 20000, T = 30, start = 100)


# For percentage of the population infected
plotphasediagraminfect(blist, klist, N=20000, T = 10, start = 100)
plotphasediagraminfect(blist, klist, N=20000, T = 20, start = 100)
plotphasediagraminfect(blist, klist, N=20000, T = 30, start = 100)











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
    sol = solve_ivp(odesimulation, tspan, xstart, args = (b, k), t_eval = teval)
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
    sol = solve_ivp(odesimulation, tspan, xstart, args = (b, k), t_eval = teval)
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



