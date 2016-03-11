# coding: utf-8
from __future__ import division

import pygame
import random

rr = random.randrange
SIZE = 800, 600
cellsize = 20
SIDE = 200


def init():
    global SCREEN
    pygame.init()
    SCREEN = pygame.display.set_mode(SIZE)


class Board(object):
    linecolor = (255, 255, 255)
    linewidth = 10
    width = 3
    height = 3
    delay_to_play = 300

    def __init__(self, surface):
        self.surface = surface
        self.reset()
        self.ownturn = False
        self.played = 0

    def reset(self):
        self.data = [False] * self.width * self.height

    def __getitem__(self, pos):
        return self.data[pos[1] * self.width + pos[0]]

    def __setitem__(self, pos, value):
        self.data[pos[1] * self.width + pos[0]] = value

    def __iter__(self):
        for x in range(self.width):
            for y in range(self.height):
                yield (x, y), self[x, y]

    def _draw_piece_at(self, pos, color):
        piece_size = int(self.factor * 0.65)
        aux = int(self.factor / 2 - piece_size / 2)
        pygame.draw.rect(self.surface, color, (
                pos[0] * self.factor + aux,
                pos[1] * self.factor + aux,
                piece_size,
                piece_size
            )
        )

    @property
    def factor(self):
        w, h = self.surface.get_size()
        w, h = min(w, h), min(w, h)
        return w / self.width

    def draw(self):
        w, h = self.surface.get_size()
        w, h = min(w, h), min(w, h)
        for x in range(self.width + 1):
            pygame.draw.line(self.surface, (self.linecolor),
                             (x * self.factor, 0),
                             (x * self.factor, h),
                             self.linewidth)
        for y in range(self.width + 1):
            pygame.draw.line(self.surface, (self.linecolor),
                             (0, y * self.factor),
                             (w,  y * self.factor),
                             self.linewidth)
        for pos, value in self:
            if value:
                self._draw_piece_at(pos, value)
            else:
                self._draw_piece_at(pos, (0, 0, 0))

    def to_board_coordinates(self, pos):
        return int(pos[0] / self.factor), int(pos[1] / self.factor)

    def play(self, pos):
        if not self.valid_play(pos):
            return False
        self[pos] = (0, 0, 255)
        self.check_victory()
        self.ownturn = True
        self.played = pygame.time.get_ticks()
        return True

    def valid_play(self, pos):
        return not self[pos]

    def update(self):
        if not self.ownturn or (pygame.time.get_ticks() - self.played < self.delay_to_play):
            return
        played = False
        while not played:
            pos = rr(0, self.width), rr(0, self.height)
            if self.valid_play(pos):
                self[pos] = (255, 0, 0)
                played = True
        self.check_victory()
        self.ownturn = False

    def check_victory(self):

        def check_row(n):
            first = self[0, n]
            for i in range(1, self.width):
                if self[i, n] != first:
                    return False
            return first

        def check_column(n):
            first = self[n, 0]
            for i in range(1, self.height):
                if self[n, i] != first:
                    return False
            return first

        def check_diagonal(start, step):
            first = self[start]
            pos_x = start[0]
            pos_y = start[1]
            while pos_x >= 0 and pos_x < self.width:
                if self[pos_x, pos_x] != first:
                    return False
                pos_x += step[0]
                pos_y += step[1]
            return first
        won = False
        for n in range(0, self.width):
            won = won or check_row(n) or check_column(n)
            if won:
                break
        else:
            won = won or check_diagonal((0, 0), (1, 1))
            won = won or check_diagonal((self.width - 1, 0), (-1, 0))
        if won:
            print("Player {} won the game!".format(won))
            raise Exit
        if self.board_full():
            print("It is a tie")
            raise Exit

    def board_full(self):
        for pos, item in self:
            if not item:
                return False
        return True


def main():
    board = Board(SCREEN)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == 0x1b:
                raise Exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                cell = board.to_board_coordinates(event.pos)
                board.play(cell)
                # board[cell] = not board[cell]

        board.update()
        board.draw()
        pygame.display.flip()
        pygame.time.delay(30)


class Exit(BaseException):
    pass

if __name__ == "__main__":
    try:
        init()
        main()
    except Exit:
        print("Normal termination")

    finally:
        pygame.quit()
