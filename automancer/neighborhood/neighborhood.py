class Neighborhood():
    def __init__(self, size):
        self.size = self.__check_size(size)
        self.points = []

    def __check_size(self, size):
        if size >= 1:
            return size
        else:
            raise ValueError("The size must be greater than or equal to 1.")

    def build_neighborhood(self):
        ...

    def points(self):
        ...

        size += 1
        area = np.arange(-size, size + 1)
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


class MooreNeighborhood(Neighborhood):
    def __init__(self):
        super().__init__(self)
        self.area = np.arange(-size, size + 1)


class VonNeumannNeighborhood(Neighborhood):
    def __init__(self):
        super().__init__(self)
        self.area = np.arange(-size, size + 1)

    def build_neighborhood(self):
        for i in self.area:
            for j in self.area:
                if np.abs(i) + np.abs(j) <= size:
                    k = (i, j)
                    neighborhood.append(k)
