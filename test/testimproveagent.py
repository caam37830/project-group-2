import sys
import os
sys.path.append("../")
import unittest
import sir
import numpy as np
import numpy.linalg as la

class Testtestpos(unittest.TestCase):
      """
      This test is used for testing the position of spatial agent people
      """
      def test_resetcorner(self):
            N = 2000
            susceptible  = []
            infect = []
            recover = []
            pop = [sir.improveagent.Person() for i in range(N)]
            start = 10
            sir.improveagent.resetcorner(10, pop)
            for i in range(10):
                  self.assertTrue(la.norm(pop[i].pos-np.zeros(2))<1e-8)

      def test_resetcenter(self):
            """
            This test is used for testing the center position of people
            """
            N = 2000
            susceptible  = []
            infect = []
            recover = []
            pop = [sir.improveagent.Person() for i in range(N)]
            start = 10
            sir.improveagent.resetcenter(10, pop)
            for i in range(10):
                  self.assertTrue(la.norm(pop[i].pos-np.array([0.5,0.5]))<1e-8)
