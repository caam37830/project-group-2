import scipy as scipy
from scipy import sparse
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
def forward_diff_matrix(n):
    data = []
    i = []
    j = []
    for k in range(n - 1):
        i.append(k)
        j.append(k)
        data.append(-1)

        i.append(k)
        j.append(k+1)
        data.append(1)

    # we'll just set the last entry to 0 to have a square matrix
    return sparse.coo_matrix((data, (i,j)), shape=(n, n)).tocsr()


def stencialxpartial(n):
    return -forward_diff_matrix(n).T@forward_diff_matrix(n)

def returnLaplacia(n):
    """
    return Laplacian operator
    """
    Dx = sparse.kron(stencialxpartial(n),sparse.eye(n)).tocsr()
    Dy = sparse.kron(sparse.eye(n),stencialxpartial(n)).tocsr()
    A = Dx+Dy
    return A

def f(t,total,p,b,k,Laplacianoperator):
    n = total.shape[0]
    #print(n)
    size = int(n/3)
    s = total[:size]
    i = total[size:2*size]
    r = total[2*size:n]
    #M = int(math.sqrt(size))
    #Laplacianoperator = returnLaplacia(M)
    """
    s1 = np.zeros(size)
    i1 = np.zeros(size)
    r1 = np.zeros(size)
    for j in range(size):
        s1[j] = -b*s[j]*i[j]
        r1[j] = k*i[j]
        i1[j] = b*s[j]*i[j]-k*i[j]
    """
    s1 = -b*np.multiply(s,i)
    r1 = k*i
    i1 = -s1-r1
    #print(np.hstack((s1,i1,r1)))

    s1 = s1 + p*Laplacianoperator@s
    i1 = i1 + p*Laplacianoperator@i
    r1 = r1 + p*Laplacianoperator@r

    #print(np.hstack((s1,i1,r1)))
    return np.hstack((s1,i1,r1))


def generatesum2corner(N):
    ssquare = np.ones((N,N))
    isquare = np.zeros((N,N))
    #Num = N**2*ratio
    #M = int(math.sqrt(Num))
    ssquare[0,0] = 0
    isquare[0,0] = 1
    s = ssquare.reshape(-1)
    i = isquare.reshape(-1)
    return np.hstack((s,i,np.zeros(N**2)))
def generatesum2center(N):
    ssquare = np.ones((N,N))
    isquare = np.zeros((N,N))
    #Num = N**2*ratio
    #M = int(math.sqrt(Num))
    ssquare[N//2,N//2] = 0
    isquare[N//2,N//2] = 1
    s = ssquare.reshape(-1)
    i = isquare.reshape(-1)
    return np.hstack((s,i,np.zeros(N**2)))


def generatesum2(N,rangenum):
    N = N**2

    vf = np.zeros(3*N)
    for j in range(N):
        k = np.random.uniform(0,rangenum)
        vf[j] = 1-k
        vf[j+N] = 1-vf[j]
    ratio = np.sum(vf[0:N])/np.sum(vf)

    return vf

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
plt.plot(sol.t,s/(200**2),label = "susceptible")
plt.plot(sol.t,i/(200**2),label = "infected")
plt.plot(sol.t,r/(200**2),label = "recovered")
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
plt.ylabel("total infected people")
plt.title("i change with p")
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
