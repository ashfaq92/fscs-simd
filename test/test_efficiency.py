import time
import winsound
import random

from fscs.FSCS import FSCS
from vectorization.FSCS_VECTORIZED import FSCS_SIMD


class TestEfficiency:
    def __init__(self, sim):
        self.simulations = sim

    def testFscs(self, bd, n):
        fileName = str(len(bd)) + "d" + "FscsART" + str(n) + str(".txt")
        f = open(fileName, "w+")
        totalTime = 0
        for i in range(self.simulations):
            startTime = time.time()
            myFscs = FSCS(bd)
            myFscs.generate_points(n)
            timeTaken = time.time() - startTime
            totalTime = totalTime + timeTaken
            f.write(str(timeTaken) + "\n")
        f.write(str(totalTime / self.simulations) + "\n")
        f.close()
        return totalTime / self.simulations

    def testFscsSimd(self, bd, n):
        fileName = str(len(bd)) + "d" + "FscsSimd" + str(n) + str(".txt")
        f = open(fileName, "w+")
        totalTime = 0
        for i in range(self.simulations):
            startTime = time.time()
            myFscsSimd = FSCS_SIMD(bd)
            myFscsSimd.generate_points(n)
            timeTaken = time.time() - startTime
            totalTime = totalTime + timeTaken
            f.write(str(timeTaken) + "\n")
        f.write(str(totalTime / self.simulations) + "\n")
        f.close()
        return totalTime / self.simulations

    def main(self):
        testCases = []
        domains = []
        testCases.append(100)
        testCases.append(200)
        testCases.append(500)
        testCases.append(1000)
        testCases.append(2000)
        testCases.append(5000)
        testCases.append(10000)
        testCases.append(15000)
        testCases.append(20000)
        bd2 = [(-5000, 5000), (-5000, 5000)]
        bd3 = [(-5000, 5000), (-5000, 5000), (-5000, 5000)]
        bd4 = [(-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000)]
        bd5 = [(-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000)]
        bd10 = [(-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000),
                (-5000, 5000), (-5000, 5000), (-5000, 5000)]

        domains.append(bd2)
        domains.append(bd3)
        # domains.append(bd4)
        # domains.append(bd5)
        # domains.append(bd10)

        for bd in domains:
            for n in testCases:
                print('d: ', len(bd), 'tcNum', n)
                t1 = self.testFscs(bd, n)
                print(t1)
                # t2 = self.testFscsSimd(bd, n)
                # print(t2)
                print("-----")


if __name__ == '__main__':
    simulations = 1000
    xyz = TestEfficiency(simulations)
    xyz.main()
    winsound.MessageBeep()
