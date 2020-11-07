import unittest
from sir.agent import *
import numpy as np
class Testcountinfect(unittest.TestCase):
      """
      This test is used for testing the total people infected
      """
      def test_three(self):
            N = 2000
            susceptible  = []
            infect = []
            recover = []
            pop = [Person() for i in range(N)]
            """
            for all the people randomly assigned whether they are infected
            """
            for i in range(N):
                  k = np.random.randint(3,size = 1)
                  if k == 0:
                        susceptible.append(pop[i])

                  if k == 1:
                        infect.append(pop[i])
                        pop[i].get_infected()
                  if k == 2:
                        recover.append(pop[i])
                        pop[i].get_infected()
                        pop[i].get_recovered()

            self.assertTrue(count_suspectial(pop)==len(susceptible))
            self.assertTrue(count_infect(pop)==len(infect))
            self.assertTrue(count_recover(pop)==len(recover))
