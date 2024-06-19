import pygame


class Board:

    def __init__(self, screen, top_left, board_size, square_size):
        self.screen = screen
        self.top_left = top_left
        self.board_size = board_size
        self.square_size = square_size
        # default board setup
        self.state = [[None, None, None, "A", None, None, None],
                      [None, None, None, "A", None, None, None],
                      [None, None, None, "D", None, None, None],
                      ["A", "A", "D", "K", "D", "A", "A"],
                      [None, None, None, "D", None, None, None],
                      [None, None, None, "A", None, None, None],
                      [None, None, None, "A", None, None, None]]
        self.throne = (board_size // 2, board_size // 2)
        self.attacker_color = 52, 63, 186
        self.defender_color = 60, 130, 53
        self.king_color = 68, 18, 74

    def draw(self):
        pygame.draw.rect(self.screen, (92, 57, 23), (*self.top_left, self.square_size * self.board_size,
                                                     self.square_size * self.board_size))
        # light squares
        for y in range(7):
            for x in range(7):
                # only select checkerboard of squares
                if (x + y) % 2 == 1:
                    pygame.draw.rect(self.screen, (247, 208, 171), (self.top_left[1] + x * self.square_size,
                                                                    self.top_left[0] + y * self.square_size,
                                                                    self.square_size, self.square_size))

        # Mark center
        center_rect = (self.top_left[1] + self.square_size * (self.board_size // 2),
                       self.top_left[0] + self.square_size * (self.board_size // 2),
                       self.square_size, self.square_size)
        pygame.draw.rect(self.screen, (255, 197, 38), center_rect)

        # draw pieces
        for y in range(len(self.state)):
            for x in range(len(self.state[x])):
                if self.state[y][x] is not None:
                    # TODO refactor to be less confusing
                    self.draw_piece((y, x), self.attacker_color if self.state[y][x] == "A"
                    else (self.defender_color if self.state[y][x] == "D" else self.king_color))

    def draw_piece(self, position, color):
        pygame.draw.circle(self.screen, color,
                           (self.top_left[0] + position[1] * self.square_size + self.square_size * .5,
                            self.top_left[1] + position[0] * self.square_size + self.square_size * .5),
                           self.square_size / 2 - 10)
