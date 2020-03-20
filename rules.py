from collections import namedtuple


class Rule:

    def __init__(self, burn_range = range(3,4), survival_range = range(2,4), radius = 1,
    BPR = 0, PUR = 0, PIC = 0, PMR = 0):
        self.burn = burn_range
        self.surv = survival_range
        self.radius = radius        # Raduis of search neighbours e.g. 1->8, 2->24, 5->120

        self.BPR = BPR # low limit of power to born
        self.PUR = PUR # power usage rule - generate energy when in surv range and spend else
        self.PIC = PIC # power inheric when die
        self.PMR = PMR # power migration rule

