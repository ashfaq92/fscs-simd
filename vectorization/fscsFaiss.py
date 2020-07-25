import sys
import faiss
import random
import numpy as np
from scipy.spatial.distance import cdist


# Speed up FSCS using SIMD instructions and Numpy array attributes and Euclidean distance normalization

class FscsFaiss:
    def __init__(self, domain, candidates=10, seed=None):
        self.domain = domain
        self.d = len(self.domain)
        self.candNum = candidates
        self.faissIndex = faiss.IndexFlatL2(self.d)
        np.random.seed(seed)

    def selectBestTc(self):
        # C = np.array([self.gen_rand_tc() for _ in range(self.candidate_num)]).astype('float32')
        # C = np.random.uniform(*np.transpose(self.domain)).astype('float32')
        C = np.random.uniform(*np.transpose(self.domain), (self.candNum, self.d)).astype(
            'float32')
        D, I = self.faissIndex.search(C, 1)
        best_distance = np.max(D)
        cIndex = np.where(D == best_distance)
        # print(cIndex)
        return C[cIndex[0][0]]

    def testEffectiveness(self, failure_region):
        # failure region is an object of faultZones classes
        initialTc = np.random.uniform(*np.transpose(self.domain), (1, self.d)).astype('float32')
        self.faissIndex.add(initialTc)
        while True:
            tc = self.selectBestTc().reshape(1, self.d)
            self.faissIndex.add(tc)
            if failure_region.findTarget(tc[0]):
                return self.faissIndex.ntotal

    def generatePoints(self, n, debug=False):
        initialTc = np.random.uniform(*np.transpose(self.domain), (1, self.d)).astype('float32')
        self.faissIndex.add(initialTc)
        while True:
            tc = self.selectBestTc().reshape(1, self.d)
            if debug:   print(tuple(tc[0]), end=",")
            self.faissIndex.add(tc)
            if self.faissIndex.ntotal >= n:
                break


if __name__ == '__main__':
    bd = [(-5000, 5000), (-5000, 5000)]
    tcNum = 1000
    randSeed = 12345
    myFscsFaiss = FscsFaiss(bd, randSeed)
    myFscsFaiss.generatePoints(tcNum, debug=True)
    print()
    print(myFscsFaiss.faissIndex.ntotal)


