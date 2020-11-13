import numpy as np
import matplotlib.pyplot as plt
class Person():
    """
    An agent representing a person.
    Determine the state of the individual, and change the state of the individual.

    """

    def __init__(self):
        self.infected = False # if enlightened = True, the person has heard idea
        self.willinfect = True

    def is_infected(self):
        """
        returns true if the person has been infected
        """
        return self.infected

    def is_willinfected(self):
        """
        return true if the person is susceptible
        """
        return self.willinfect


    def get_infected(self):
        """
        once the person get infected
        """
        self.infected = True
        self.willinfect = False

    def get_recovered(self):
        """
        once the person get recovered
        """
        self.infected = False

    def is_recovered(self):
        """
        if the person is recovered
        """
        return self.infected==False and self.willinfect == False


def count_infect(pop):
    """
    the total infected people
    """
    total = 0
    for i in pop:
        if i.is_infected():
            total = total + 1
    return total

def count_recover(pop):
    """
    the total recovered people
    """
    total = 0
    for i in pop:
        if i.is_recovered():
            total = total + 1
    return total

def count_suspectial(pop):
    """
    the total suspectial people
    """
    total = 0
    for i in pop:
        if i.is_willinfected():
            total = total + 1
    return total
