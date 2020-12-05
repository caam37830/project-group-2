import sys
import os
sys.path.append("../")
import unittest
import sir
import numpy as np
class Testcountinfect(unittest.TestCase):
      """
      This test is used for testing the total people infected
      """
      def test_suspectial(self):
            N = 2000
            susceptible  = []
            infect = []
            recover = []
            pop = [sir.agent.Person() for i in range(N)]
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
            self.assertTrue(sir.agent.count_suspectial(pop)==len(susceptible))

      def test_infectremove(self):
            """
            We test the percentage of infected and removed people
            """
            N = 2000
            susceptible  = []
            infect = []
            recover = []
            pop = [sir.agent.Person() for i in range(N)]

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
            #We test the amount of infected people

            self.assertTrue(sir.agent.count_infect(pop)==len(infect))
            self.assertTrue(sir.agent.count_recover(pop)==len(recover))
