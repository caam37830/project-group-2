import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
sys.path.append("../")
from sir.ode import *

df = pd.read_csv("files/time_series_covid19_confirmed_global.csv")
#Here we take the Hubei
dfc = df.iloc[69,:][4:80]
df2 = pd.read_csv("files/time_series_covid19_deaths_global.csv")
dfd = df2.iloc[69,:][4:80]
df3 = pd.read_csv("files/time_series_covid19_recovered_global.csv")
dfr = df3.iloc[56,:][4:80]
#Here we get
dfrt = dfr+dfd
dfi = dfc-dfrt




def runodesimulation4(tspan, xstart, b, k, teval):
    """
    Run ODE simulation with the value infected, recovered
    """
    sumresult = np.sum(xstart)
    xstart = convertvector(xstart)
    sol = solve_ivp(odesimulation, tspan, xstart, args = (b, k), t_eval = teval)
    return sol.y[1][-1]*sumresult,sol.y[2][-1]*sumresult

def runodesimulation3(tspan, xstart, b, k, teval):
    """
    Run ODE simulation with the vstack value so that we can calculate the mse
    """
    sumresult = np.sum(xstart)
    xstart = convertvector(xstart)
    sol = solve_ivp(odesimulation, tspan, xstart, args = (b, k), t_eval = teval)
    return np.vstack((sol.y[1]*sumresult,sol.y[2]*sumresult))

def calculatemse(vstacka,vstackb):
    msevalue = 0
    for i in range(2):
        for j in range(vstacka.shape[1]):
            msevalue = msevalue+(vstacka[i][j]-vstackb[i][j])**2
    return msevalue


def findsmallvalue(blist,klist,vstacka,tspan,xstart,teval):
    """
    find the most appropriate b,k
    """
    returnblist = []
    returnklist = []
    valuelist = []

    for i in blist:
        for j in klist:
            vstackb = runodesimulation3(tspan,xstart,i,j,teval)
            valuelist.append(calculatemse(vstacka,vstackb))
            returnblist.append(i)
            returnklist.append(j)
    valuereturn = min(valuelist)
    position = valuelist.index(min(valuelist))

    breturn = returnblist[position]
    kreturn = returnklist[position]

    return valuereturn,breturn,kreturn

blist = np.arange(0.2,0.4,0.005)
klist = np.arange(0.01,0.2,0.005)
vstacka = np.vstack((dfi[0:25],dfrt[0:25]))
"""
First we consider first 26 days
"""
xstart = [58.5e6-dfi[0]-dfrt[0],dfi[0],dfrt[0]]
tspan = (0,25)
teval = np.linspace(0,25,25)
a,b,c = findsmallvalue(blist,klist,vstacka,tspan,xstart,teval)
infect,remove = runodesimulation4(tspan,xstart,b,c,teval)
blist2 = 0.1*blist
klist2 = 2*klist
xstart2 = [58.5e6-infect-remove,infect,remove]
vstackas = np.vstack((dfi[25:76],dfrt[25:76]))
tspan2 = (0,51)
teval2 = np.linspace(0,51,51)
a2,b2,c2 = findsmallvalue(blist2,klist2,vstackas,tspan2,xstart2,teval2)
"""
we put the value b,c ,b2,c2 to the function
"""
vstackaf = runodesimulation3(tspan,xstart,b,c,teval)
vstackass = runodesimulation3(tspan2,xstart2,b2,c2,teval2)

vstackconnect = np.hstack((vstackaf,vstackass))
plt.plot(np.arange(0,76,1),dfc-dfd-dfr,label = "infected")
plt.plot(np.arange(0,76,1),dfd+dfr,label = "removed")
plt.plot(np.arange(0,76,1),vstackconnect[0],label = "simulated infected")
plt.plot(np.arange(0,76,1),vstackconnect[1],label = "simulated removed")
plt.ylabel("Infected or Removed ")
plt.xlabel("T")
plt.title("Infected, Removed Population")
plt.legend()
plt.show()
