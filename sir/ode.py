import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
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
