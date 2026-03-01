import numpy as np

def Help():
    ...

class Neighborhood():
    def __init__(self):
        self.points = []

    def automata_points(self):
        ...


class DefinedNeighborhood(Neighborhood):
    def __init__(self):
        super().__init__()

    def __in_area(self):
        ...

class DefinedNeighborhood2d(Neighborhood):
    def __init__(self, size):
        super().__init__()
        self.size = self.__check_size(size)
        self.area = np.arange(-self.size, self.size + 1)
        self.points = self.generate_points()

    def __check_size(self, size):
        if size >= 1:
            return size
        else:
            raise ValueError("The size must be greater than or equal to 1.")

    def build_neighborhood(self):
        ...

    def generate_points(self):
        points = []
        for i in self.area:
            for j in self.area:
                points.append((i, j))
        return np.array(points)


class MooreNeighborhood(DefinedNeighborhood2d):
    def __init__(self):
        super().__init__(self)

    def __in_area(self, i, j):
        return (np.abs(i) <= self.size) and (np.abs(j) <= self.size)

    def build_neighborhood(self):
        for i in self.area:
            for j in self.area:
                if (np.abs(i) <= size) and (np.abs(j) <= size):
                    k = (i, j)
                    self.points.append(k)


class VonNeumannNeighborhood(DefinedNeighborhood2d):
    def __init__(self):
        super().__init__(self)

    def __in_area(self, point):
        return np.abs(point[0]) + np.abs(point[1]) <= self.size

    def build_neighborhood(self):
        for i in self.area:
            for j in self.area:
                if np.abs(i) + np.abs(j) <= size:
                    k = (i, j)
                    self.points.append(k)
