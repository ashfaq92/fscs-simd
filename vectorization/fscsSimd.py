import sys
import random
import numpy as np
from scipy.spatial.distance import cdist

# Trying to speed up FSCS using SIMD instructions and Numpy array attributes and Euclidean distance normalization
from auxilliary.Point import Point


class FscsSimd:
    def __init__(self, domain, candidates=10, seed=None):
        self.domain = domain
        self.d = len(self.domain)
        self.candNum = candidates
        np.random.seed(seed)
        self.E = []  # todo: make it numpy array
        self.C = None

    def selectBestTc(self):
        selectedSet = np.array(self.E)
        self.C = np.random.uniform(*np.transpose(self.domain), (self.candNum, self.d)).astype(
            'float32')
        # print(self.C)
        # print(self.C[0])
        ans = cdist(self.C, selectedSet)  # cdist is best for all pairwise distances
        nns = np.amin(ans, axis=1)
        best_distance = nns.max()
        candidateIndex = np.where(ans == best_distance)
        # print("selectedSet", selectedSet)
        # print("C", C)
        # print("ans", ans)
        # print('nns', nns)
        # print("best_distance", best_distance)
        # print("candidateIndex", candidateIndex[0][0])
        # print("best test case", tuple(C[candidateIndex[0][0]]))
        # return tuple(self.C[candidateIndex[0][0]])
        return self.C[candidateIndex[0][0]]

    def testEffectiveness(self, failure_region):
        # failure region is an object of faultZones classes
        self.E.clear()
        initialTc = np.random.uniform(*np.transpose(self.domain)).astype('float32')
        self.E.append(initialTc)
        while True:
            tc = self.selectBestTc()
            self.E.append(tc)
            if failure_region.findTarget(tc):
                return len(self.E)

    def generatePoints(self, n, debug=False, returnBak=False):
        initialTc = np.random.uniform(*np.transpose(self.domain)).astype('float32')
        self.E.append(initialTc)
        while True:
            tc = self.selectBestTc()
            if debug:   print(tuple(tc), end=",")
            self.E.append(tc)
            if len(self.E) >= n:
                return self.E


if __name__ == '__main__':
    bd = [(-5000, 5000), (-5000, 5000)]
    tcNum = 500
    candNum = 10
    randSeed = 12345
    myFscsSimd = FscsSimd(bd, candNum, randSeed)
    asdf = myFscsSimd.generatePoints(tcNum, debug=False)
