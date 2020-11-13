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
    plt.plot(range(T+1), newrecover, label = "r: percentage of removed")
    plt.plot(range(T+1), newsuspect, label = "s: percentage of susceptible")
    plt.plot(range(T+1), newinfect, label = "i: percentage of infected")
    plt.xlabel("T")
    plt.ylabel("Percentage")
    plt.title("Percentage of Population, Discrete \n b = "+str(b)+", k = "+str(k))
    plt.legend()
    plt.show()



def checktotalinfect(b, k, N, T, start = 1):
    """
    Compute the total percentage of the population infected (i+r) and
    percentage of the population infected (i) for b >= 1
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
    for b >= 1
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
    for b >= 1
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



# For b < 1, re-define the functions as below

def checkinfectbsmall(b,k,N,T,start=1):
    """
    Compute the total percentage of the population infected (i+r) and
    percentage of the population infected (i) for b < 1
    """
    recover = [0]
    infect  = [start]
    suspect = [N-start]
    pop = [Person() for i in range(N)]
    np.random.seed(10)
    for i in range(start):
        pop[i].get_infected();
    for i in range(T):
        for j in range(N):
            if pop[j].is_infected():
                contact = np.random.randint(N, size= 1)
                if np.random.rand()< b:
                    pop[contact[0]].get_infected()
        for j in range(N):
            if pop[j].is_infected():
                if np.random.rand()<k:
                    pop[j].get_recovered()
    return np.array([(count_infect(pop)+count_recover(pop))/N,count_infect(pop)/N])


def plotphasediagramsmall(blist,klist,N,T,start):
    """
    Generate phase diagram of total percentage of the population infected (i+r)
    for b < 1
    """
    cts = np.zeros((len(blist), len(klist)))
    for j,b in enumerate(blist):
        for i,k in enumerate(klist):
            cts[j,i] = checkinfectbsmall(b,k,N,T,start)[0]
    plt.imshow(cts,extent=[np.min(klist),np.max(klist),np.min(blist),np.max(blist)], aspect="auto")
    plt.colorbar()
    plt.xlabel("k")
    plt.ylabel("b")
    plt.title("Percentage of Population Infected and Removed \n T = "+str(T)+", Discrete")
    plt.show()



def plotphasediagraminfectsmall(blist,klist,N,T,start):
    """
    Generate phase diagram of percentage of the population infected (i)
    for b < 1
    """
    cts = np.zeros((len(blist), len(klist)))
    for j,b in enumerate(blist):
        for i,k in enumerate(klist):
            cts[j,i] = checkinfectbsmall(b,k,N,T,start)[1]
    plt.imshow(cts,extent=[np.min(klist),np.max(klist),np.min(blist),np.max(blist)], aspect="auto")
    plt.colorbar()
    plt.xlabel("k")
    plt.ylabel("b")
    plt.title("Percentage of Population Infected \n T = "+str(T)+", Discrete")
    plt.show()


# Phase diagrams for b < 1
blist = np.arange(1, 0, -0.1)
klist = np.arange(0, 1, 0.1)
plotphasediagramsmall(blist, klist, 20000, 10, 100)
plotphasediagramsmall(blist, klist, 20000, 20, 100)
plotphasediagramsmall(blist, klist, 20000, 30, 100)
plotphasediagraminfectsmall(blist, klist, 20000, 10, 100)
plotphasediagraminfectsmall(blist, klist, 20000, 20, 100)
plotphasediagraminfectsmall(blist, klist, 20000, 30, 100)








# ODE continuous simulations and plots

def odesimulation(t, x, b, k):
    """
    Generate ODE simulation
    """
    s = x[0]
    i = x[1]
    r = x[2]
    ds = -b*s*i
    di = b*s*i-k*i
    dr = k*i
    return np.array([ds, di, dr])


def convertvector(x):
    """
    Convert s, i, r into vector of percentage
    """
    s = x[0]
    i = x[1]
    r = x[2]
    return np.array([s/(s+i+r), i/(s+i+r), r/(s+i+r)])


def runodesimulation(tspan, xstart, b, k, teval):
    """
    Run ODE simulation with plot
    """
    xstart = convertvector(xstart)
    sol = solve_ivp(odesimulation, tspan, xstart, args = (b, k), t_eval = teval)
    plt.plot(sol.t, sol.y[0], label = "s: percentage of susceptible")
    plt.plot(sol.t, sol.y[1], label = "i: percentage of infected")
    plt.plot(sol.t, sol.y[2], label = "r: percentage of removed")
    plt.title("Percentage of Population, Continuous \n b = "+str(b)+", k = "+str(k))
    plt.xlabel("T")
    plt.ylabel("percentage")
    plt.legend()
    plt.show()


def checktotalinfectpeople(x, b, k, T):
    """
    Compute the total percentage of the population infected (i+r) and
    percentage of the population infected (i)
    """
    x = convertvector(x)
    tspan = (0, T)
    xstart = x
    teval = np.linspace(0, T, 200);
    sol = solve_ivp(odesimulation, tspan, xstart, args = (b, k), t_eval = teval)
    totalinfect = sol.y[2][-1] + sol.y[1][-1]
    infect = sol.y[1][-1]
    return np.array([totalinfect, infect])


def plotodephasediagram(x, blist, xlist, T):
    """
    Generate ODE phase diagram of total percentage of the population infected (i+r)

    """
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
    """
    Generate ODE phase diagram of percentage of the population infected (i)

    """
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



# Generate plots
tspan = (0, 30)
xstart = np.array([19900, 100, 0])
teval1 = np.linspace(0, 30, 300)
# for b = 2
runodesimulation(tspan, xstart, 2, 0.2, teval1)
runodesimulation(tspan, xstart, 2, 0.5, teval1)
runodesimulation(tspan, xstart, 2, 0.8, teval1)
# for b = 5
runodesimulation(tspan, xstart, 5, 0.2, teval1)
runodesimulation(tspan, xstart, 5, 0.5, teval1)
runodesimulation(tspan, xstart, 5, 0.8, teval1)



# Generate phase diagrams
xstart = np.array([19900, 100, 0])
blist = np.arange(10, 0, -1)
klist = np.arange(0, 1, 0.1)
plotodephasediagram(xstart, blist,klist, 10)
plotodephasediagram(xstart, blist,klist, 20)
plotodephasediagram(xstart, blist,klist, 30)
plotodeinfectphasediagram(xstart, blist,klist, 10)
plotodeinfectphasediagram(xstart, blist,klist, 20)
plotodeinfectphasediagram(xstart, blist,klist, 30)


# Phase diagrams for b < 1
xstart = np.array([19900, 100, 0])
blist = np.arange(1, 0, -0.1)
klist = np.arange(0, 1, 0.1)
plotodephasediagram(xstart, blist, klist, 10)
plotodephasediagram(xstart, blist, klist, 20)
plotodephasediagram(xstart, blist, klist, 30)
plotodeinfectphasediagram(xstart, blist,klist, 10)
plotodeinfectphasediagram(xstart, blist,klist, 20)
plotodeinfectphasediagram(xstart, blist,klist, 30)
