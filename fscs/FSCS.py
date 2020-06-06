import sys
import random


class FSCS:
    def __init__(self, dom, candidates=10, seed=None):
        self.domain = dom
        self.dimensions = len(self.domain)
        self.candidate_num = candidates
        random.seed(seed)
        self.selected_set = []

    def gen_rand_tc(self):
        return tuple(random.uniform(coord[0], coord[1]) for coord in self.domain)

    def calc_distance(self, tc1, tc2):
        # A general distance formula for all dimensions can be following:
        # distance = (sum(pow(a - b, 2) for a, b in zip(tc1, tc2))) ** 0.5   # slower
        # from scipy.spatial import distance
        # dist = distance.euclidean(tc1, tc2)  #slowest
        # Hence, we have intentionally calculated Euclidean distance in static way to make it as faster as we can
        if self.dimensions == 1:
            return ((tc1[0] - tc2[0]) ** 2) ** 0.5
        elif self.dimensions == 2:
            return ((tc1[0] - tc2[0]) ** 2 + (tc1[1] - tc2[1]) ** 2) ** 0.5
        elif self.dimensions == 3:
            return ((tc1[0] - tc2[0]) ** 2 + (tc1[1] - tc2[1]) ** 2 + (tc1[2] - tc2[2]) ** 2) ** 0.5
        elif self.dimensions == 4:
            return ((tc1[0] - tc2[0]) ** 2 + (tc1[1] - tc2[1]) ** 2 + (tc1[2] - tc2[2]) ** 2 + (
                    tc1[3] - tc2[3]) ** 2) ** 0.5
        else:
            print("invalid args for calc_distance func")
            sys.exit()

    def select_best_test_case(self):
        best_distance = -1.0
        best_data = None
        # Generate unique random candidates
        for i in range(self.candidate_num):
            candidate = self.gen_rand_tc()
            min_candidate_distance = sys.maxsize
            for x in range(len(self.selected_set)):
                dist = self.calc_distance(self.selected_set[x], candidate)
                # find minimum distance MIN
                if dist < min_candidate_distance:
                    min_candidate_distance = dist
            # find maximum distance from all minimum distances MAX
            if best_distance < min_candidate_distance:
                best_data = candidate
                best_distance = min_candidate_distance
        return best_data

    def testEffectiveness(self, failure_region):
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
    myFscs = FSCS(bd, seed=12345)
    print(myFscs.generate_points(4))
