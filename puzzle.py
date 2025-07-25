class Tile:
    def __init__(self, col, row, order):
        self.col = col
        self.row = row
        self.order = order

    def move(self, new_col, new_row):
        self.col = new_col
        self.row = new_row


class Puzzle:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.tiles = []
        self.empty_tile_index = 0

        tile_index = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if row == num_rows - 1 and col == num_cols - 1:
                    self.empty_tile_index = tile_index
                    break
                self.tiles.append(Tile(col, row, tile_index))
                tile_index += 1

    def is_valid_move(self, col, row):
        empty_col = self.empty_tile_index % self.num_cols
        empty_row = self.empty_tile_index // self.num_cols
        return abs(col - empty_col) + abs(row - empty_row) == 1

    def swap_tiles(self, tile_index_to_move):
        tile = self.tiles[tile_index_to_move]
        tile_col, tile_row = tile.col, tile.row
        empty_col = self.empty_tile_index % self.num_cols
        empty_row = self.empty_tile_index // self.num_cols

        tile.move(empty_col, empty_row)
        self.empty_tile_index = tile_row * self.num_cols + tile_col

    def is_solved(self):
        for tile in self.tiles:
            if tile.order != tile.row * self.num_cols + tile.col:
                return False
        return True
