import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp



def odesimulation(t,x,b,k):
    s = x[0]
    i = x[1]
    r = x[2]
    ds = -b*s*i
    di = b*s*i-k*i
    dr = k*i
    return np.array([ds,di,dr])

def convertvector(x):
    s = x[0]
    i = x[1]
    r = x[2]
    return np.array([s/(s+i+r),i/(s+i+r),r/(s+i+r)])
def runodesimulation(tspan,xstart,b,k,teval):
    xstart = convertvector(xstart)
    sol = solve_ivp(odesimulation,tspan,xstart,args=(b,k),t_eval=teval)
    plt.plot(sol.t,sol.y[0],label="suspectial people")
    plt.plot(sol.t,sol.y[1],label="infected people")
    plt.plot(sol.t,sol.y[2],label="recovered people")
    plt.title("odesimulation with s = "+str(xstart[0])+"i = "+str(xstart[1]))
    plt.xlabel("days")
    plt.ylabel("percentage")
    plt.legend()
    plt.show()

def checktotalinfectpeople(x,b,k,T):
    x = convertvector(x)
    tspan = (0,T)
    xstart = x
    teval = np.linspace(0,T,200);
    sol = solve_ivp(odesimulation,tspan,xstart,args=(b,k),t_eval=teval)
    totalinfect = sol.y[2][-1]+ sol.y[1][-1]
    infect = sol.y[1][-1]
    return np.array([totalinfect,infect])

def plotodephasediagram(x,blist,xlist,T):
    cts = np.zeros((len(blist),len(xlist)))
    for j,b in enumerate(blist):
        for i,k in enumerate(klist):
            cts[j,i] = checktotalinfectpeople(x,b,k,T)[0]

    plt.figure(figsize=(8,10))
    plt.imshow(cts,extent=[np.min(klist),np.max(klist),np.min(blist),np.max(blist)],interpolation="nearest",aspect='auto')
    plt.colorbar()
    plt.title("the ode total infected people at T = "+str(T))
    plt.xlabel("change of k")
    plt.ylabel("change of b")
    plt.show()


def plotodeinfectphasediagram(x,blist,xlist,T):
    cts = np.zeros((len(blist),len(xlist)))
    for j,b in enumerate(blist):
        for i,k in enumerate(klist):
            cts[j,i] = checktotalinfectpeople(x,b,k,T)[1]
    print(cts)
    plt.figure(figsize=(8,10))
    plt.imshow(cts,extent=[np.min(klist),np.max(klist),np.min(blist),np.max(blist)],interpolation="nearest",aspect='auto')
    plt.colorbar()
    plt.title("the ode infected people at T = "+str(T))
    plt.xlabel("change of k")
    plt.ylabel("change of b")
    plt.show()

tspan = (0,20)
xstart = np.array([4500,500,0])
teval = np.linspace(0,20,200);
runodesimulation(tspan,xstart,8,0.4,teval)
tspan2 = (0,30)
xstart2 = np.array([9800,200,0])
teval2 = np.linspace(0,30,300);
runodesimulation(tspan2,xstart2,4,0.95,teval2);
blist = np.arange(10,0,-1)
klist = np.arange(0,1,0.1)
plotodephasediagram(np.array([399,1,0]),blist,klist,10)
plotodephasediagram(np.array([399,1,0]),blist,klist,20)
plotodephasediagram(np.array([399,1,0]),blist,klist,30)
plotodeinfectphasediagram(np.array([399,1,0]),blist,klist,10)
plotodeinfectphasediagram(np.array([399,1,0]),blist,klist,20)
plotodeinfectphasediagram(np.array([399,1,0]),blist,klist,30)
