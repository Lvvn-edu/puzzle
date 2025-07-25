# test_puzzle.py
from puzzle import Puzzle

def test_valid_move():
    p = Puzzle(3, 3)
    assert p.is_valid_move(2, 1)
    assert p.is_valid_move(1, 2)
    assert not p.is_valid_move(0, 0)

def test_is_solved_and_swap():
    p = Puzzle(3, 3)
    assert p.is_solved()
    # move tile at (2,1)
    for i, tile in enumerate(p.tiles):
        if tile.col == 2 and tile.row == 1:
            p.swap_tiles(i)
            break
    assert not p.is_solved()
