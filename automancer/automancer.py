import numpy as np
import matplotlib.pyplot as plt
import os

# I'll be assuming that all things in a cellular automata simulation are just
# numbers.
class CellularAutomata:
    def __init__(self, grid, baseline = 0):
        if len(grid) != 2:
            raise ValueError("Grid must be iterable with length 2.")
        else:
            self.grid = grid # TODO: get error handling for grids with a size greater than two
        self.state = np.zeros(grid)
        self.rules = [] # initialize a set of rules
        self.neighborhoods = []
        self.baseline = baseline

    def __str__(self):
        return f"CellularAutomata ({self.grid[0]}x{self.grid[1]}) \n {self.state}"
    def __repr__(self):
        return f'CellularAutomata({self.grid})'
    # TODO: change this to get rid of redundant updates (e.g. an updating the same
    # cell twice), rather than just looking at the state of the grid, which should
    # be handled when defining a rule
    def __is_redundant(self, update):
        i, j  = update[0]
        value = update[1]
        if self.state[i, j] == value == 0:
            return True
        else:
            return False
    # from https://pymorton.wordpress.com/2015/02/16/wrap-integer-values-to-fixed-range/
    def __keep_periodic(self, number, maximum):
        return (number) % (maximum)
    
    def set_state(self, state):
        self.state = np.flip(state)

    # Is this really the best way to update the grid?
    # Anyways, this method is **fundamental**---don't get it spaghettified.
    # new_values is a list of tuples (e.g. `[((0, 0), 1)]`)
    def update(self, new_values): 
        for item in new_values:
            i, j = item[0]
            value = item[1]
            self.state[i, j] = value

    # This method needs some serious refinement
    def build_neighborhood(self, size, shape = 'v'):
        size += 1
        area = np.arange(-size, size + 1)
        neighborhood = []
        if shape == 'v' or 'Von Neumann': # Von Neumann neighborhood
            for i in area:
                for j in area:
                    if np.abs(i) + np.abs(j) <= size:
                        k = (i, j)
                        neighborhood.append(k)
                    else:
                        pass
        elif shape == 'm' or 'Moore':
            for i in area:
                for j in area:
                   if np.abs(i) <= size and np.abs(j) <= size:
                       k = (i, j)
                       neighborhood.append(k)
                   else:
                       pass
        else:
            raise ValueError("Neighborhood must be either Moore of Von Neumann")
        return neighborhood

    def custom_neighborhood(self, neighborhood):
        neighborhoods.append(neighborhood)

    def add_neighborhood(self, external = None, **kwargs):
        custom = kwargs.pop('custom' or 'c', False)
        shape  = kwargs.pop('shape' or 's', 'v')
        size   = kwargs.pop('size'  or 'a', 1)
        if custom == True and external != None:
            self.neighborhoods.append(external)
        else:
            a = self.build_neighborhood(size - 1, shape)
            self.neighborhoods.append(a)

    # woah, look at *this* complex method
    def print_state(self):
        print(self.state)

    def generate_picture(self, **kwargs):
        file = kwargs.pop('file', None)
        fig, ax = plt.subplots()
        
        # this feels bad to write :|
        x = np.arange(0, self.grid[0]) # REALLY mull over using `range` vs.
        y = np.arange(0, self.grid[1]) # `np.arange`
        z = self.state
        ax.pcolormesh(x, y, z)
        
        if file != None:
            plt.savefig(file)
        else:
            plt.show()

    def add_rule(self, rule):
        if type(rule) == str:
            raise TypeError("Input rule must be a function.")
        elif hasattr(rule, '__iter__'):
            self.rules.append(r if callable(r) else None for r in rule)
        elif callable(rule):
            self.rules.append(rule)
        else:
            pass

    def randomize_state(self, min_value = 0, max_value = 1):
        self.state = np.random.randint(low = min_value, high = max_value + 1,
                                       size = self.grid)

    def evaluate_rules(self):
        i_range = range(0, self.grid[0])
        j_range = range(0, self.grid[1])
        num_rules = len(self.rules)
        num_neighborhoods = len(self.neighborhoods)
        updates = []
        if num_rules != num_neighborhoods:
            raise ValueError("The number of neighborhoods must equal the number of rules.")
        else:
            rule_range = range(0, num_rules)
        for i in i_range: # oooooh I love me some nesting
            for j in j_range:
                for k in rule_range:
                    neighborhood = [(self.__keep_periodic(i + neighbor[0], self.grid[0]),
                                     self.__keep_periodic(j + neighbor[1], self.grid[1]))
                                    for neighbor in self.neighborhoods[k]]
                    point = (i, j)
                    new_value = self.rules[k](self.state, neighborhood, point)
                    for value in new_value: # only works for an iterable with iterables---make this more robust
                        updates.append(value)

        spaghetti_list = [val for val in updates]
        for update in spaghetti_list:
            if self.__is_redundant(update):
                updates.remove(update)
            else:
                pass
        #print(updates)
        self.update(updates)

    def time_evolution(self, steps = 10, **kwargs):
        file = kwargs.pop('file', None)
        evolution = []
        evolution.append(self.state)
        time = np.arange(0, steps)
        for t in time:
            self.evaluate_rules()
            evolution.append(self.state)
            #print(self.state)
        
        if file == None:
            return evolution
        else:
            np.save(file, evolution)

    def generate_picture(self, **kwargs):
        file = kwargs.pop('file', None)
        fig, ax = plt.subplots()
        
        # this feels bad to write :|
        x = np.arange(0, self.grid[0]) # REALLY mull over using `range` vs.
        y = np.arange(0, self.grid[1]) # `np.arange`
        z = self.state
        ax.pcolormesh(x, y, z)
        
        if file != None:
            plt.savefig(file)
        else:
            plt.show()

    def move_point(self, point, amount):
        temp_state = np.zeros(self.grid)
        temp_state[point] = self.state[point]
        temp_state = np.roll(temp_state, shift = amount, axis = (1, 0))
        new_point = tuple(np.argwhere(temp_state))
        return [[point, 0], [new_point, state[point]]]

    



# rules must have the state, neighborhood, and point evaluated in that order.
# rule must output a list of the form [[(i, j), value]]
def random_walk(state, neighborhood, point):
    x, y = point
    length = np.random.randint(0, len(neighborhood))
    new_spot = neighborhood[length]
    if state[x, y] == 1:
        new_state = [new_spot, 1]
        return [[point, 0], new_state]
    elif state[x, y] == 0:
        return [[point, 0]]
    else: 
        pass


# rules and neighborhoods are associated, meaning that if you add a
# neighborhood and then a rule, that rule will be evaluated with that
# neighborhood.
