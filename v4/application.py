from simulator import Simulator
from grass import Grass
from rules import Rule
from conseedset import StartBoardGenerator
import numpy as np
from collections import namedtuple


loadORInit = input('Load seed (y/n)?')
seed = StartBoardGenerator(20, 'startPoints.txt')
if loadORInit == 'y':
    seed.fileLoad()
    seed.printPoints()
else:
    seed.consInit()

sim = Simulator(Rule(), seed.square_face)
sim.setSeed(seed.board)

print(sim.getGrowMatrix())

for iter in range(20):
    sim.simulateStep()
    print('#' + str(iter))
    print(sim.getGrowMatrix())