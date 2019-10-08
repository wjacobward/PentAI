import enum


class PenteBoard:
    stoneColor = enum.Enum('stone', 'black white')

    def __init__(self):
        self.blackStones = [[0 for x in range(19)] for x in range(19)]
        self.whiteStones = [[0 for x in range(19)] for x in range(19)]

    def addStone(self, color, location):
        selector = {self.stoneColor.black : self.addBlackStone,
                    self.stoneColor.white : self.addWhiteStone}
        selector[color](location)

    def addBlackStone(self, location):
        if self.whiteStones[location[0]][location[1]] == 1:
            raise SpaceOccupiedError('Space already occupied by white')
        self.blackStones[location[0]][location[1]] = 1

    def addWhiteStone(self, location):
        if self.blackStones[location[0]][location[1]] == 1:
            raise SpaceOccupiedError('Space already occupied by black')
        self.whiteStones[location[0]][location[1]] = 1


class SpaceOccupiedError(Exception):
    def __init__(self, message):
        self.message = message

