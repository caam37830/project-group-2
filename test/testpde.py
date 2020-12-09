import scipy as scipy
from scipy import sparse
import numpy as np
import math
from scipy.integrate import solve_ivp
import sys
import os
import numpy.linalg as la
sys.path.append("../")
import sir
import unittest

class Testtestpde(unittest.TestCase):
      """
      This test is used for testing the position of spatial agent people
      """
      def test_Laplacian(self):
            L = sir.pde.returnLaplacia(3)
            self.assertTrue(la.norm(L.todense()-np.array([[-2,1,0,1,0,0,0,0,0],[1,-3,1,0,1,0,0,0,0],[0,1,-2,0,0,1,0,0,0],[1,0,0,-3,1,0,1,0,0],[0,1,0,1,-4,1,0,1,0],[0,0,1,0,1,-3,0,0,1],[0,0,0,1,0,0,-2,1,0],[0,0,0,0,1,0,1,-3,1],[0,0,0,0,0,1,0,1,-2]]))<1e-8)

      def test_centergenerate(self):
            centervector = np.array([1,1,1,1,0,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
            self.assertTrue(la.norm(sir.pde.generatesum2center(3)-centervector)<1e-8)

      def test_cornergenerate(self):
            cornervector = np.array([0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            self.assertTrue(la.norm(sir.pde.generatesum2corner(3)-cornervector)<1e-8)
