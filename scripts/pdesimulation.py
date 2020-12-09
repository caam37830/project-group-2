import scipy as scipy
from scipy import sparse
import numpy as np
import math
import sys
import os
sys.path.append("../")
from sir.pde import *
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp




def calculatesol(sol,T,M):
    s = np.zeros(T)
    i = np.zeros(T)
    r = np.zeros(T)
    for k in range(M**2):
        s = s+sol.y[k]
        i = i+sol.y[k+M**2]
        r = r+sol.y[k+2*(M**2)]
    return (i[-1]+r[-1])/(s[-1]+i[-1]+r[-1])
xstart = generatesum2(200,2/(200**2))

tspan = (0,200)

Laplacianoperator = returnLaplacia(200)
teval = np.linspace(0,200,200)
sol = solve_ivp(f,tspan,xstart,args=(1,1,0.4,Laplacianoperator),t_eval=teval)

s = np.zeros(200)
i = np.zeros(200)
r = np.zeros(200)
for k in range(200**2):
    s = s+sol.y[k]
    i = i+sol.y[k+200**2]
    r = r+sol.y[k+2*(200**2)]
plt.plot(sol.t,s/(200**2),label = "s: percentage of susceptible")
plt.plot(sol.t,i/(200**2),label = "i: percentage of infected")
plt.plot(sol.t,r/(200**2),label = "r: percentage of removed ")
plt.title("Percentage of Population, Continuous")
plt.xlabel("T")
plt.ylabel("percentage")
plt.legend()
plt.show()
xstart2 = generatesum2center(200)
listappend = []
valuelist = [1,2,3,4,5,10,20,30,40,50]
for q in valuelist:
    if q <= 10:
        T = 200
    else:
        T = 50
    tspan = (0,T)
    t_eval = np.linspace(0,T,200)
    sol = solve_ivp(f,tspan,xstart2,args=(q,1,0.4,Laplacianoperator),t_eval=t_eval)
    """
    s = np.zeros(200)
    i = np.zeros(200)
    r = np.zeros(200)
    for k in range(200**2):
        s = s+sol.y[k]
        i = i+sol.y[k+200**2]
        r = r+sol.y[k+2*(200**2)]
    listappend.append((i[-1]+r[-1])/(s[-1]+i[-1]+r[-1]))
    """
    value = calculatesol(sol,200,200)
    print(value)
    listappend.append(value)
plt.plot(valuelist,listappend)
plt.xlabel("p")
plt.ylabel("percentage of individuals infected")
plt.title("Percentage of Individuals Infected vs p")
plt.show()



#Here we reset the parameter of p = 1

p  = 20
xstart = generatesum2(200, 2/(200**2))
xstart2 = generatesum2center(200)
xstart3 = generatesum2corner(200)
tspan = (0,50)
t_eval = np.linspace(0,50,200)
sol1 = solve_ivp(f,tspan,xstart,args=(p,1,0.4,Laplacianoperator),t_eval=t_eval)
print("infected people start randomly : "+str(calculatesol(sol1,200,200)))
sol2 = solve_ivp(f,tspan,xstart2,args=(p,1,0.4,Laplacianoperator),t_eval=t_eval)
print("infected people start from center : "+str(calculatesol(sol2,200,200)))
sol3 = solve_ivp(f,tspan,xstart3,args=(p,1,0.4,Laplacianoperator),t_eval=t_eval)
print("infected people start from corner : "+str(calculatesol(sol3,200,200)))
