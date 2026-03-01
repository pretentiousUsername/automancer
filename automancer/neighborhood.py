class Neighborhood:
    def __init__(self):
        ...

    def build_neighborhood(self, size, shape = 'v'):
        size += 1
        area = range(-size, size + 1)
        neighborhood = []
        if shape == 'v' or shape == 'Von Neumann':  # Von Neumann neighborhood
            for i in area:
                for j in area:
                    if np.abs(i) + np.abs(j) <= size:
                        k = (i, j)
                        neighborhood.append(k)
                    else:
                        pass
        elif shape == 'm' or shape == 'Moore':
            for i in area:
                for j in area:
                    if (np.abs(i) <= size) and (np.abs(j) <= size):
                        k = (i, j)
                        neighborhood.append(k)
                    else:
                        pass
        else:
            raise ValueError("Neighborhood must be either Moore of Von Neumann")
        return neighborhood

    def custom_neighborhood(self, neighborhood):
        self.neighborhoods.append(neighborhood)

    def add_neighborhood(self, external = None, **kwargs):
        custom = kwargs.pop('custom' or 'c', False)
        shape  = kwargs.pop('shape' or 's', 'v')
        size   = kwargs.pop('size' or 'a', 1)
        if custom is True and external is not None:
            self.neighborhoods.append(external)
        else:
            a = self.build_neighborhood(size - 1, shape)
            self.neighborhoods.append(a)
