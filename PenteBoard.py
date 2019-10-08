import enum


class PenteBoard:
    stone_color = enum.Enum('stone', 'black white')

    def __init__(self):
        self.black_stones = [[0 for x in range(19)] for x in range(19)]
        self.white_stones = [[0 for x in range(19)] for x in range(19)]

    def add_stone(self, color, location):
        selector = {self.stone_color.black : self.add_black_stone,
                    self.stone_color.white : self.add_white_stone}
        selector[color](location)

    def add_black_stone(self, location):
        if self.white_stones[location[0]][location[1]] == 1:
            raise SpaceOccupiedError('Space already occupied by white')
        self.black_stones[location[0]][location[1]] = 1

    def add_white_stone(self, location):
        if self.black_stones[location[0]][location[1]] == 1:
            raise SpaceOccupiedError('Space already occupied by black')
        self.white_stones[location[0]][location[1]] = 1


class SpaceOccupiedError(Exception):
    def __init__(self, message):
        self.message = message

