import pygame


class Board:

    def __init__(self, screen, top_left=(115, 115), board_size=7, square_size=70, first_player="A"):
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
        self.selected = None
        self.throne = (board_size // 2, board_size // 2)
        self.attacker_color = 52, 63, 186
        self.defender_color = 60, 130, 53
        self.king_color = 68, 18, 74
        self.first_player = first_player
        self.turn_num = 0
        self.turn = self.first_player

    # switches to next player's turn
    def next_turn(self):
        if self.turn == "A":
            self.turn = "D"
        else:
            self.turn = "A"
    # TODO move display code to its own file
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

        # draw selected circle
        if self.selected is not None:
            pygame.draw.circle(self.screen, (0, 0, 0),
                               (self.top_left[0] + self.selected[1] * self.square_size + self.square_size * .5,
                                self.top_left[1] + self.selected[0] * self.square_size + self.square_size * .5),
                               self.square_size / 2 - 7)
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

    # pos comes through as x, y
    def click(self, pos):
        index = (pos[1] - self.top_left[0]) // self.square_size, (pos[0] - self.top_left[1]) // self.square_size
        # this is currently selected, deselect
        if self.selected == index:
            self.selected = None
        # is the right side to be able to select, select
        # FIXME, this won't allow king to be selected on defender turn currently
        elif self.state[index[1]][index[0]] == self.turn:
            self.selected = index


