import scipy as scipy
from scipy import sparse
import numpy as np
import math
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

def generatesum2corner(N):
    """
    generate a vector so that the initial infected people are located in a corner
    """
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
