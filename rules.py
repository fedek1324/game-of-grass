from collections import namedtuple


class Rule:

    def __init__(self, burn_range = range(3,4), survival_range = range(2,4), radius = 1):
        self.burn = burn_range
        self.surv = survival_range
        self.radius = radius        # Raduis of search neighbours e.g. 1->8, 2->24, 5->120

