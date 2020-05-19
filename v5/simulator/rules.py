from collections import namedtuple
from grass import *
import json


class Rule:

    def __init__(self, appear_range = range(3,4), survival_range = range(2,4), radius = 1, PMR = 0, PU = 0, MxG = 1):
        # Classic rule
        self.appear = appear_range
        self.surv = survival_range
        self.radius = radius        # Radius of search neighbours e.g. 1->8, 2->24, 5->120

        # Soil addon
        self.PMR = PMR              # Power migration rule.
        self.PU  = PU               # Power usage.
        self.MxG = MxG              # Max grow


    def consInit(self):
        self.radius = int(input("Input radius of searching neighbours: "))
        maxStopValue = (self.radius + 2) ** 2
        startA, stopA = input("Input appear range (start stop(" + str(maxStopValue) +")): ").split()
        startS, stopS = input("Input survival range (start stop(" + str(maxStopValue) +")): ").split()
        self.appear = range(int(startA), int(stopA))
        self.surv = range(int(startS), int(stopS))

        self.PMR = int(input("Power migration on step: "))
        self.PU  = int(input("Power usage for grow:    "))
        self.MxG = int(input("Max grow for grass:      "))
        print("Done!")


    def showSelf(self):
        print("Rule: ")
        print("Radius          = " + str(self.radius))
        print("appear range    = " + str(self.appear))
        print("survival range  = " + str(self.surv))
        print("power migration = " + str(self.PMR))
        print("power usage     = " + str(self.PU))
        print("max grow        = " + str(self.MxG))


    def executeRule(self, const_grass : Grass, countNeighbours : int):
        grass = const_grass.copy()
        if grass.isLife():
            if countNeighbours in self.surv:
                grass.toAlive()
            else:
                grass.toDie()
        else:
            if countNeighbours in self.appear:
                grass.toAlive()

        return grass


    def objToJson(self, fileName):
        f = open(fileName, 'w')

        jsonDict = {
            'Rule' : {
                'appear_range' : {
                    'start' : self.appear.start,
                    'stop'  : self.appear.stop
                },
                'survival_range' : {
                    'start' : self.surv.start,
                    'stop'  : self.surv.stop
                },
                'radius' : self.radius,
                'PMR'    : self.PMR,
                'PU'     : self.PU,
                'MxG'    : self.MxG
            }
        }        
        json.dump(jsonDict, f, indent=4)

        f.close


    def jsonToObj(self, fileName):
        try:
            f = open(fileName, 'r')
            jsonDict = json.load(f)

            if 'Rule' not in jsonDict:
                return False

            jr = jsonDict['Rule']
            self.appear = range(jr['appear_range']['start'], jr['appear_range']['stop'])
            self.surv   = range(jr['survival_range']['start'], jr['survival_range']['stop']) 
            self.radius = jr['radius']

            self.PMR = jr['PMR']
            self.PU  = jr['PU']
            self.MxG = jr['MxG']

            f.close()
        
        except:
            return False
        
        return True



if __name__ == '__main__':   

    r1 = Rule()
    r1.consInit()
    r1.objToJson('rule.json')
