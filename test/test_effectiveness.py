import winsound

from fscs.FSCS import FSCS
from vectorization.FSCS_VECTORIZED import FSCS_SIMD
from faultZones import FaultZone_Block
from faultZones import FaultZone_StripMao
from faultZones import FaultZone_StripXia


class TestEffectiveness:
    def __init__(self, sim):
        self.simulations = sim

    def main(self):
        failure_rates = [0.01, 0.005, 0.002, 0.001, 0.0005, 0.0002, 0.0001]
        domains = []
        bd2 = [(-5000, 5000), (-5000, 5000)]
        bd3 = [(-5000, 5000), (-5000, 5000), (-5000, 5000)]
        bd4 = [(-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000)]
        bd5 = [(-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000)]
        bd10 = [(-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000), (-5000, 5000),
                (-5000, 5000), (-5000, 5000), (-5000, 5000)]

        domains.append(bd2)
        # domains.append(bd3)
        # domains.append(bd4)
        # domains.append(bd5)
        # domains.append(bd10)
        for bd in domains:
            print("\n------DIMENSION:\t", len(bd), "D--------:")
            for theta in failure_rates:
                print(len(bd), "D", theta)
                # todo:  create file for recording output
                self.fixRateTest(theta, bd, "block")
                # self.fixRateTest(theta, bd, "stripMao")
                # self.fixRateTest(theta, bd, "stripXia")
        winsound.MessageBeep(winsound.MB_OK)

    def fixRateTest(self, area, domain, fp, file=None, fileName=None):
        failure_region = None
        total1, total2, total3 = 0, 0, 0
        for i in range(self.simulations):
            if fp == "block":
                failure_region = FaultZone_Block.FaultZone_Block(domain, area)
            elif fp == "stripMao":
                failure_region = FaultZone_StripMao.FaultZone_Strip(domain, area)
            elif fp == "stripXia":
                failure_region = FaultZone_StripXia.FaultZone_Strip2(domain, area)
                failure_region.genFailurePattern()
            for j in range(1):
                myFscs = FSCS(domain)
                f_measure = myFscs.testEffectiveness(failure_region)
                total1 = total1 + f_measure
                # print(f_measure)

                myFscsSimd = FSCS_SIMD(domain)
                f_measure = myFscsSimd.testEffectiveness(failure_region)
                total2 = total2 + f_measure
                # print(f_measure)

        n = self.simulations
        s = 1 / area / 100
        print((total1 / n / s), "\t", (total2 / n / s), "\t", (total3 / n / s))


if __name__ == '__main__':
    xyz = TestEffectiveness(3000)
    xyz.main()
    winsound.MessageBeep()
