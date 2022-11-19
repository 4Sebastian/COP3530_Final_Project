from typing import List, Tuple
from perlin_noise import PerlinNoise

class NoiseHandler:

    terrain = None

    def genTer(self, size: int, *octaves: Tuple[float, int]) -> None:
        print("Generating Terrain")

        noises = [PerlinNoise(octaves=octave[1]) for octave in octaves]

        xpix = ypix = size
        row = []
        for i in range(xpix):
            col = []
            for j in range(ypix):
                noise_val = sum(round(weight[0] * noise([i / xpix, j / ypix]), 3) for noise, weight in zip(noises, octaves))

                col.append(noise_val)
            row.append(col)

        self.terrain = row

    def getTer(self) -> List[List[float]]:
        if self.terrain:
            return self.terrain
        return [[]]

    def wipeTer(self) -> None:
        self.terrain = None

    def printTer(self) -> None:
        for s in self.terrain:
            print("".join(f"{str(i):10}" for i in s))

    def convert_matplotlib(self) -> Tuple[List[int], List[int], List[List[float]]]:
        d_arr = [ i for i in range(len(self.terrain)**2)]
        return d_arr, d_arr, self.terrain


