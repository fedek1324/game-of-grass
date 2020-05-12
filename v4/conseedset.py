from collections import namedtuple
import json

Point = namedtuple('Point', ['x', 'y'])

class StartBoardGenerator:
    def __init__(self, square_face, file_name):
        self.square_face = square_face
        self.file_name = file_name
        self.board = set()


    def consInit(self):
        count = input("Input count of points: ")
        for _ in range(int(count)):
            x = input("x: ")
            y = input("y: ")
            self.board.add(Point(x, y))


    def fileSave(self):
        f = open(self.file_name, 'w')
     
        json.dump(list(self.board),f)

        f.close()


    def fileLoad(self):
        f = open(self.file_name, 'r')
        
        listData = json.load(f)
        for el in listData:
            self.board.add(Point(el[0], el[1])) 

        f.close()


    def printPoints(self):
        for el in self.board:
            print(el)



if __name__ == '__main__':
    generator = StartBoardGenerator(30, "startPoints.txt")
    #generator.consInit()
    #generator.fileSave()
    generator.fileLoad()
    generator.printPoints()
