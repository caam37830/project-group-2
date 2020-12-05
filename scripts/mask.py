
import sys
import os
sys.path.append("../")
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from sir.odemask import *


x = np.array([0.9,0,0.08,0.02,0,0,0])
beta = 0.5
eta = 0.5
sigma = 0.2
alpha = 0.5
phi = 0.025
gammaA = 1/8
gammaI = 1/8
gammah = 1/16
delta = 0.015
tspan = (0,50)
teval = np.linspace(0,50,200)
sol = solve_ivp(odemasksimulation,tspan,x,args=(eta,beta,sigma,phi,gammaI,alpha,gammaA,delta,gammah),t_eval=teval)
#We plot the curve for not wearing mask occasion
plt.plot(sol.t,sol.y[0],label = "suspect")
plt.plot(sol.t,sol.y[1],label = "expose")
plt.plot(sol.t,sol.y[5],label = "recover")
plt.plot(sol.t,sol.y[6],label = "death")
plt.plot(sol.t,sol.y[2]+sol.y[3]+sol.y[4],label = "infected")
plt.legend()
plt.show()

def plotrelativetotaldeath(x,clist,elist,params,T):
    """
    Here we plot the relative death rate after we wearing the mask
    """
    beta = params[0]
    eta = params[1]
    sigma = params[2]
    alpha = params[3]
    phi = params[4]
    gammaA = params[5]
    gammaI = params[6]
    gammah = params[7]
    delta = params[8]
    tspan = (0,T)
    teval = np.linspace(0,T,400)
    cts = np.zeros((len(clist),len(elist)))
    for j,e in enumerate(elist):
        for i,c in enumerate(clist):
            epsilon = e
            xmaskcoverage = np.hstack(((1-c)*x,c*x))
            solmask = solve_ivp(odemasksimulation,tspan,x,args=(eta,beta,sigma,phi,gammaI,alpha,gammaA,delta,gammah),t_eval=teval)
            solmaskmask = solve_ivp(odemasksimulationmask,tspan,xmaskcoverage,args=(eta,beta,sigma,phi,gammaI,alpha,gammaA,delta,gammah,epsilon),t_eval=teval)
            #print("epsilon is "+str(e))
            #print("coverage is "+str(c))
            #print("maskresult coverage is"+str(solmaskmask.y[13][-1])+"maskresult uncover is "+str(solmaskmask.y[6][-1]))
            cts[j,i] = (solmaskmask.y[13][-1]+solmaskmask.y[6][-1])/solmask.y[6][-1]
            #print(cts[j,i])
    plt.figure(figsize=(8,10))
    plt.imshow(cts,extent=[np.min(elist),np.max(elist),np.min(clist),np.max(clist)],interpolation="nearest",aspect='auto')
    plt.colorbar()
    plt.title("the ode total death rate at T = "+str(T)+" with beta = "+str(beta))
    plt.xlabel("change of e")
    plt.ylabel("change of c")
    plt.show()


beta = 0.5
eta = 0.5
sigma = 0.2
alpha = 0.5
phi = 0.025
gammaA = 1/8
gammaI = 1/8
gammah = 1/16
delta = 0.015
params = np.array([beta,eta,sigma,alpha,phi,gammaA,gammaI,gammah,delta])
T = 80
#elist is for epsilon, the efficacy for mask
elist = np.arange(1,-0.1,-0.1)
#clist is for coverage range
clist = np.arange(0,1.1,0.1)
x = np.array([0.9,0,0.08,0.02,0,0,0])
plotrelativetotaldeath(x,clist,elist,params,T)
beta = 1.5
params = np.array([beta,eta,sigma,alpha,phi,gammaA,gammaI,gammah,delta])
plotrelativetotaldeath(x,clist,elist,params,T)

def plotrelativetotalhospital(x,clist,elist,params,T):
    """
    We check the rate of peak hosptialzied after wearing the mask
    """
    beta = params[0]
    eta = params[1]
    sigma = params[2]
    alpha = params[3]
    phi = params[4]
    gammaA = params[5]
    gammaI = params[6]
    gammah = params[7]
    delta = params[8]
    tspan = (0,T)
    teval = np.linspace(0,T,400)
    cts = np.zeros((len(clist),len(elist)))
    for j,e in enumerate(elist):
        for i,c in enumerate(clist):
            epsilon = e
            xmaskcoverage = np.hstack(((1-c)*x,c*x))
            solmask = solve_ivp(odemasksimulation,tspan,x,args=(eta,beta,sigma,phi,gammaI,alpha,gammaA,delta,gammah),t_eval=teval)
            solmaskmask = solve_ivp(odemasksimulationmask,tspan,xmaskcoverage,args=(eta,beta,sigma,phi,gammaI,alpha,gammaA,delta,gammah,epsilon),t_eval=teval)
            #print("epsilon is "+str(e))
            #print("coverage is "+str(c))
            #print("maskresult coverage is"+str(solmaskmask.y[13][-1])+"maskresult uncover is "+str(solmaskmask.y[6][-1]))
            cts[j,i] = (np.max(solmaskmask.y[4]+solmaskmask.y[11]))/np.max(solmask.y[4])
            #print(cts[j,i])
    plt.figure(figsize=(8,10))
    plt.imshow(cts,extent=[np.min(elist),np.max(elist),np.min(clist),np.max(clist)],interpolation="nearest",aspect='auto')
    plt.colorbar()
    plt.title("the ode total hospital rate at T = "+str(T) +"beta = "+str(beta))
    plt.xlabel("change of e")
    plt.ylabel("change of c")
    plt.show()
#Now we change beta,

beta = 0.5
params = np.array([beta,eta,sigma,alpha,phi,gammaA,gammaI,gammah,delta])
plotrelativetotalhospital(x,clist,elist,params,T)

beta = 1.5
params = np.array([beta,eta,sigma,alpha,phi,gammaA,gammaI,gammah,delta])
plotrelativetotalhospital(x,clist,elist,params,T)
