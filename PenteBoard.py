import enum


class PenteBoard:
    stone_color = enum.Enum('stone', 'black white')

    def __init__(self):

        self.black_stones = [[0 for x in range(19)] for x in range(19)]
        self.white_stones = [[0 for x in range(19)] for x in range(19)]

    def place_stone(self, color, location):
        self.add_stone(color, location)
        self.check_for_capture(color, location)
        self.check_for_win(color)

    def add_stone(self, color, location):
        selector = {self.stone_color.black: self.add_black_stone,
                    self.stone_color.white: self.add_white_stone}
        selector[color](location)

    def remove_stone(self, color, location):
        selector = {self.stone_color.black: self.remove_black_stone,
                    self.stone_color.white: self.remove_white_stone}
        selector[color](location)

    def get_valid_moves(self):
        occupied_spaces = [[sum(x) for x in zip(self.black_stones[row], self.white_stones[row])] for row in range(len(self.black_stones))]
        valid_spaces = [[1-x for x in row] for row in occupied_spaces]
        return valid_spaces

    def add_black_stone(self, location):
        if self.white_stones[location[0]][location[1]] == 1:
            raise SpaceOccupiedError("Space already occupied by white")
        self.black_stones[location[0]][location[1]] = 1

    def add_white_stone(self, location):
        if self.black_stones[location[0]][location[1]] == 1:
            raise SpaceOccupiedError("Space already occupied by black")
        self.white_stones[location[0]][location[1]] = 1

    def remove_black_stone(self, location):
        if not self.black_stones[location[0]][location[1]] == 1:
            raise SpaceEmptyError("Attempted to remove a black stone that wasn't there")
        self.black_stones[location[0]][location[1]] = 0

    def remove_white_stone(self, location):
        if not self.white_stones[location[0]][location[1]] == 1:
            raise SpaceEmptyError("Attempted to remove a white stone that wasn't there")
        self.white_stones[location[0]][location[1]] = 0

    def check_for_capture(self, color, location):
        # look for two opposing stones sandwiched by two stones of <color>, one being the newly placed stone
        pass

    def check_for_win(self, color):
        # look for lines of 5 or more stones of the same color
        selector = {self.stone_color.black: self.black_stones,
                    self.stone_color.white: self.white_stones}
        stones_to_check = selector[color]
        # check for horizontal win
        # check for vertical win
        # check for diagonal win (SW/NE)
        # check for diagonal win (NW/SE)


class SpaceOccupiedError(Exception):
    def __init__(self, message):
        self.message = message


class SpaceEmptyError(Exception):
    def __init__(self, message):
        self.message = message
