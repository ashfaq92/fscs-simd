import sys
import random
import numpy as np
from scipy.spatial.distance import cdist


# Trying to speed up FSCS using SIMD instructions and Numpy array attributes and Euclidean distance normalization

class FSCS_SIMD:
    def __init__(self, dom, candidates=10, seed=None):
        self.domain = dom
        self.dimensions = len(self.domain)
        self.candidate_num = candidates
        random.seed(seed)
        self.selected_set = []  # todo: make it numpy array

    def gen_rand_tc(self):
        return tuple(random.uniform(coord[0], coord[1]) for coord in self.domain)

    def select_best_test_case(self):
        selectedSet = np.array(self.selected_set)
        candidates = np.array([self.gen_rand_tc() for _ in range(self.candidate_num)])
        ans = cdist(candidates, selectedSet)    #cdist is best for all pairwise distances
        nns = np.amin(ans, axis=1)
        best_distance = nns.max()
        candidateIndex = np.where(ans == best_distance)
        # print("selectedSet", selectedSet)
        # print("candidates", candidates)
        # print("ans", ans)
        # print('nns', nns)
        # print("best_distance", best_distance)
        # print("candidateIndex", candidateIndex[0][0])
        # print("best test case", tuple(candidates[candidateIndex[0][0]]))
        return tuple(candidates[candidateIndex[0][0]])

    def testEffectiveness(self, failure_region):
        # failure region is an object of faultZones classes
        self.selected_set.clear()
        initial_test_data = self.gen_rand_tc()
        self.selected_set.append(initial_test_data)
        while True:
            tc = self.select_best_test_case()
            self.selected_set.append(tc)
            if failure_region.findTarget(tc):
                return len(self.selected_set)

    def generate_points(self, n):
        initial_test_data = self.gen_rand_tc()
        self.selected_set.append(initial_test_data)
        while True:
            test_case = self.select_best_test_case()
            self.selected_set.append(test_case)
            if len(self.selected_set) >= n:
                return self.selected_set


if __name__ == '__main__':
    bd = [(0, 1), (0, 1)]
    candNum = 10
    randSeed = 12345
    my = FSCS_SIMD(bd, candNum, randSeed)
    print(my.generate_points(4))

