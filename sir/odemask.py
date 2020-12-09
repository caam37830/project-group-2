import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def odemasksimulation(t,x,eta,beta,sigma,phi,gammaI,alpha,gammaA,delta,gammah):
    """
    we divide the group into suspect,asymptotic, infect,expose,hospitalized,recover,death
    more accurate ode
    """
    s = x[0]
    e = x[1]
    i = x[2]
    a = x[3]
    h = x[4]
    r = x[5]
    d = x[6]
    n = s+e+i+a+r
    ds = -beta*(i+eta*a)*(s/n)
    de = beta*(i+eta*a)*(s/n)-sigma*e
    di = alpha*sigma*e-phi*i-gammaI*i
    da = (1-alpha)*sigma*e - gammaA*a
    dh = phi*i - delta*h- gammah*h
    dr = gammaI*i+gammah*h+gammaA*a
    dd = delta*h
    return np.array([ds,de,di,da,dh,dr,dd])

def odemasksimulationmask(t,x,eta,beta,sigma,phi,gammaI,alpha,gammaA,delta,gammah,epsilon):
    """
    now we run the simulation with people wearing mask,this is the function for derivative
    """
    su = x[0]
    eu = x[1]
    iu = x[2]
    au = x[3]
    hu = x[4]
    ru = x[5]
    du = x[6]
    sm = x[7]
    em = x[8]
    im = x[9]
    am = x[10]
    hm = x[11]
    rm = x[12]
    dm = x[13]
    n = su+eu+iu+au+ru+sm+em+im+am+rm
    dsu = -beta*(iu+eta*au)*su/n-beta*((1-epsilon)*im+(1-epsilon)*eta*am)*su/n
    deu = beta*(iu+eta*au)*su/n-sigma*eu+beta*((1-epsilon)*im+(1-epsilon)*eta*am)*su/n
    diu = alpha*sigma*eu-phi*iu-gammaI*iu
    dau = (1-alpha)*sigma*eu - gammaA*au
    dhu = phi*iu - delta*hu- gammah*hu
    dru = gammaI*iu+gammah*hu+gammaA*au
    ddu = delta*hu
    #problem here
    dsm = -beta*(1-epsilon)*(iu+eta*au)*sm/n-beta*(1-epsilon)*((1-epsilon)*im+(1-epsilon)*eta*am)*sm/n
    dem = beta*(1-epsilon)*(iu+eta*au)*sm/n-sigma*em+beta*(1-epsilon)*((1-epsilon)*im+(1-epsilon)*eta*am)*sm/n
    dim = alpha*sigma*em-phi*im-gammaI*im
    dam = (1-alpha)*sigma*em - gammaA*am
    dhm = phi*im - delta*hm- gammah*hm
    drm = gammaI*im+gammah*hm+gammaA*am
    ddm = delta*hm
    return np.array([dsu,deu,diu,dau,dhu,dru,ddu,dsm,dem,dim,dam,dhm,drm,ddm])
