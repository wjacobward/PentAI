import unittest
import PenteBoard


class TestCase(unittest.TestCase):
    def test_check_for_stone(self):
        p = PenteBoard.PenteBoard()

        black_stone_in_middle = p.check_for_stone(p.stone_color.black, [8,8])
        self.assertFalse(black_stone_in_middle)

        p.place_stone(p.stone_color.black, [8,8])
        black_stone_in_middle = p.check_for_stone(p.stone_color.black, [8,8])
        self.assertTrue(black_stone_in_middle)

    def test_capture(self):
        p = PenteBoard.PenteBoard()
        p.place_stone(p.stone_color.black, [8, 8])
        p.place_stone(p.stone_color.white, [8, 9])
        p.place_stone(p.stone_color.white, [8, 10])
        p.place_stone(p.stone_color.black, [8, 11])
        white_stones = p.current_board[p.stone_color.white]

        black_stones_correct = p.check_for_stones([p.stone_color.black, p.stone_color.black], [[8, 8], [8, 11]])
        white_stones_correct = sum([sum(row) for row in white_stones]) == 0
        self.assertTrue(white_stones_correct)
        self.assertTrue(black_stones_correct)


if __name__ == '__main__':
    unittest.main()
