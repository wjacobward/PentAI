import enum


class PenteBoard:
    stone_color = enum.Enum('stone', 'black white')

    def __init__(self):
        board_grid = [[[0 for x in range(19)] for x in range(19)] for x in range(2)]
        self.current_board = dict(zip(self.stone_color, board_grid))

    def place_stone(self, color, location):
        self.add_stone(color, location)
        self.check_for_capture(color, location)
        self.check_for_win(color)

    def add_stone(self, color, location):
        valid_spaces = self.get_valid_moves()
        if valid_spaces[location[0]][location[1]] == 0:
            raise SpaceOccupiedError("Space already occupied")
        self.current_board[color][location[0]][location[1]] = 1

    def get_valid_moves(self):
        occupied_spaces = [[sum(x) for x in zip(self.current_board[self.stone_color.black][row], self.current_board[self.stone_color.white][row])] for row in range(len(self.current_board[self.stone_color.black]))]
        valid_spaces = [[1-x for x in row] for row in occupied_spaces]
        return valid_spaces

    def check_for_capture(self, color, location):
        # look for two opposing stones sandwiched by two stones of <color>, one being the newly placed stone
        # look above
        if location[0] > 2:
            colors = [c for c in self.stone_color if c != color]
            locations = [[location[0] - 1, location[1]], [location[0] - 2, location[1]]]
            if self.check_for_stones(colors, locations):
                if self.check_for_stone(color, [location[0] - 3, location[1]]):
                    self.remove_stones(colors, locations)
        # look below
        if location[0] < 16:
            colors = [c for c in self.stone_color if c != color]
            locations = [[location[0] + 1, location[1]], [location[0] + 2, location[1]]]
            if self.check_for_stones(colors, locations):
                if self.check_for_stone(color, [location[0] + 3, location[1]]):
                    self.remove_stones(colors, locations)
        # look to the left
        if location[1] > 2:
            colors = [c for c in self.stone_color if c != color]
            locations = [[location[0], location[1] - 1], [location[0], location[1] - 2]]
            if self.check_for_stones(colors, locations):
                if self.check_for_stone(color, [location[0], location[1] - 3]):
                    self.remove_stones(colors, locations)
        # look to the right
        if location[1] < 16:
            colors = [c for c in self.stone_color if c != color]
            locations = [[location[0], location[1] + 1], [location[0], location[1] + 2]]
            if self.check_for_stones(colors, locations):
                if self.check_for_stone(color, [location[0], location[1] + 3]):
                    self.remove_stones(colors, locations)

    def check_for_win(self, color):
        # look for lines of 5 or more stones of the same color
        # check for horizontal win
        # check for vertical win
        # check for diagonal win (SW/NE)
        # check for diagonal win (NW/SE)
        pass

    def check_for_stones(self, colors, locations):
        for color, location in zip(colors, locations):
            if not self.check_for_stone(color, location):
                return False
        return True

    def check_for_stone(self, color, location):
        if self.current_board[color][location[0]][location[1]] == 1:
            return True
        else:
            return False

    def remove_stones(self, colors, locations):
        for color in colors:
            for location in locations:
                self.remove_stone(color, location)

    def remove_stone(self, color, location):
        if not self.current_board[color][location[0]][location[1]] == 1:
            raise SpaceEmptyError("Attempted to remove a stone that wasn't there")
        self.current_board[color][location[0]][location[1]] = 0


class SpaceOccupiedError(Exception):
    def __init__(self, message):
        self.message = message


class SpaceEmptyError(Exception):
    def __init__(self, message):
        self.message = message
