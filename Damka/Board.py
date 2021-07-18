from Cell import *
import pygame
import time
from AI import *


class Board:
    def __init__(self, x=0, y=0, width=WIDTH, height=HEIGHT, num_of_whites=12, num_of_blacks=12):
        self.table = [[Cell() for x in range(8)] for y in range(8)]  # define board
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.num_of_blacks = num_of_blacks
        self.num_of_whites = num_of_whites
        self.AI = AI()
        for row in range(8):  # inits the board
            for col in range(8):
                if (row + col) % 2 == 0:
                    self.table[row][col] = Cell(col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT,
                                                LIGHT_BROWN)
                else:
                    self.table[row][col] = Cell(col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT,
                                                DARK_BROWN)


    def draw(self, screen):
        black_piece = pygame.image.load('images/BlackPiece.png')
        black_piece = pygame.transform.scale(black_piece, (CELL_WIDTH, CELL_HEIGHT))  # defines size of image
        white_piece = pygame.image.load('images/WhitePiece.png')
        white_piece = pygame.transform.scale(white_piece, (CELL_WIDTH, CELL_HEIGHT))

        for row in range(8):
            for col in range(8):
                self.table[row][col].draw(screen)
                self.table[row][col].row = row
                self.table[row][col].col = col
                if row <= 2:  # white pieces
                    if row == 0 or row == 2:
                        if col % 2 == 1:
                            screen.blit(white_piece, (self.table[row][col].x, self.table[row][col].y))
                            self.table[row][col].inside = "white"
                    elif row == 1:
                        if col % 2 == 0:
                            screen.blit(white_piece, (self.table[row][col].x, self.table[row][col].y))
                            self.table[row][col].inside = "white"

                elif row >= 5:  # black pieces
                    if row == 5 or row == 7:
                        if col % 2 == 0:
                            screen.blit(black_piece, (self.table[row][col].x, self.table[row][col].y))
                            self.table[row][col].inside = "black"

                    elif row == 6:
                        if col % 2 == 1:
                            screen.blit(black_piece, (self.table[row][col].x, self.table[row][col].y))
                            self.table[row][col].inside = "black"
        pygame.display.flip()

    def choose_king_cell_movable(self, king_cell):  # returns true if king can be moved in his position, else false
        row = king_cell.row
        col = king_cell.col
        # row under
        if row + 1 <= 7:  # if there is under row
            if col + 1 <= 7:  # right-down empty
                if self.table[row + 1][col + 1].inside is None:
                    return True
            if col - 1 >= 0:  # left-down empty
                if self.table[row + 1][col - 1].inside is None:
                    return True
        # row above
        if row - 1 >= 0:  # if there is under row
            if col + 1 <= 7:  # right-up empty
                if self.table[row - 1][col + 1].inside is None:
                    return True
            if col - 1 >= 0:  # left-up empty
                if self.table[row - 1][col - 1].inside is None:
                    return True
        return False

    def mouse_click_choose_cell(self, screen, x, y):  # return the selected cell, if its good place, else not played
        for row in range(8):
            for col in range(8):
                if self.table[row][col].is_inside(x, y) and self.table[row][col].inside == "black":
                    if not self.table[row][col].is_king:
                        # regular move
                        if col + 1 == 8:  # right-up missing
                            if self.table[row - 1][col - 1].inside is None:
                                return self.table[row][col]
                        elif col - 1 < 0:  # left-up missing
                            if self.table[row - 1][col + 1].inside is None:
                                return self.table[row][col]
                        elif col + 1 <= 7 and col - 1 >= 0:
                            if self.table[row - 1][col - 1].inside is None or self.table[row - 1][col + 1].inside is None:
                                return self.table[row][col]
                        # eating move
                        if col + 2 <= 7:  # right-up exists
                            if self.table[row - 2][col + 2].inside is None:  # to_cell inside is None
                                if self.table[row - 1][col + 1].inside == "white":  # if there is someone to eat
                                    return self.table[row][col]
                        if col - 2 >= 0:
                            if self.table[row - 2][col - 2].inside is None:  # to_cell inside is None
                                if self.table[row - 1][col - 1].inside == "white":  # if there is someone to eat
                                    return self.table[row][col]
                    elif self.table[row][col].is_king:
                        if self.choose_king_cell_movable(self.table[row][col]):  # checks if the king can move
                            return self.table[row][col]
                elif self.table[row][col].is_inside(x, y) and self.table[row][col].inside != "black":  # clicked on white or none
                    return "not played"  # accidentally pressed on not black

    def apply_black_kings(self, screen):
        black_king = pygame.image.load('images/BlackKing.png')  # to_cell: table[row][col]
        black_king = pygame.transform.scale(black_king, (CELL_WIDTH, CELL_HEIGHT))  # defines size of image
        for col in range(1, 8, 2):  # top[0]-row: black kings
            if self.table[0][col].inside == "black":
                self.table[0][col].draw(screen)  # removes the non-king piece
                screen.blit(black_king, (self.table[0][col].x, self.table[0][col].y))  # draws the black king
                self.table[0][col].is_king = True
        pygame.display.flip()

    def apply_white_kings(self, screen):
        white_king = pygame.image.load('images/WhiteKing.png')  # to_cell: table[row][col]
        white_king = pygame.transform.scale(white_king, (CELL_WIDTH, CELL_HEIGHT))  # defines size of image
        for col in range(0, 7, 2):  # bottom[7]-row: black kings
            if self.table[7][col].inside == "white":
                self.table[7][col].draw(screen)  # removes the non-king piece
                screen.blit(white_king, (self.table[7][col].x, self.table[7][col].y))  # draws the white king
                self.table[7][col].is_king = True
        pygame.display.flip()

    def mouse_click_place_cell(self, screen, x, y, from_cell):  # removes from_cell,places to_cell. return True if placed
        black_piece = pygame.image.load('images/BlackPiece.png')  # to_cell: table[row][col]
        black_piece = pygame.transform.scale(black_piece, (CELL_WIDTH, CELL_HEIGHT))  # defines size of image
        black_king = pygame.image.load('images/BlackKing.png')  # to_cell: table[row][col]
        black_king = pygame.transform.scale(black_king, (CELL_WIDTH, CELL_HEIGHT))  # defines size of image
        for row in range(8):
            for col in range(8):
                if self.table[row][col].is_inside(x, y) and self.table[row][col].inside is None:
                    if not from_cell.is_king:
                        # not eating move
                        if col + 1 <= 7:
                            if self.table[row + 1][col + 1] == from_cell:
                                self.table[row + 1][col + 1].draw(screen)  # removes from_cell
                                self.table[row + 1][col + 1].inside = None  # updates the inside of from_cell

                                screen.blit(black_piece, (self.table[row][col].x, self.table[row][col].y))  # places to_cell
                                self.table[row][col].inside = "black"  # update the inside of to_cell
                                pygame.display.flip()
                                return True
                        if col - 1 >= 0:
                            if self.table[row + 1][col - 1] == from_cell:
                                self.table[row + 1][col - 1].draw(screen)  # removes from_cell
                                self.table[row + 1][col - 1].inside = None  # updates the inside of from_cell

                                screen.blit(black_piece, (self.table[row][col].x, self.table[row][col].y))  # places to_cell
                                self.table[row][col].inside = "black"  # update the inside of to_cell
                                pygame.display.flip()
                                return True
                        # eating move
                        if col + 2 <= 7:
                            if self.table[row + 2][col + 2] == from_cell:  # if legit position of to_cell
                                if self.table[row + 1][col + 1].inside == "white":  # if there is someone to eat
                                    self.table[row + 2][col + 2].draw(screen)  # removes from_cell
                                    self.table[row + 1][col + 1].draw(screen)  # removes the eaten white
                                    self.table[row + 2][col + 2].inside = None  # updates the inside of from_cell
                                    self.table[row + 1][col + 1].inside = None  # updates the inside of eaten white cell
                                    self.num_of_whites -= 1  # update num of whites

                                    screen.blit(black_piece, (self.table[row][col].x, self.table[row][col].y))  # places to_cell
                                    self.table[row][col].inside = "black"  # update the inside of to_cell
                                    pygame.display.flip()
                                    return True
                        if col - 2 >= 0:
                            if self.table[row + 2][col - 2] == from_cell:  # if legit position of to_cell
                                if self.table[row + 1][col - 1].inside == "white":  # if there is someone to eat
                                    self.table[row + 2][col - 2].draw(screen)  # removes from_cell
                                    self.table[row + 1][col - 1].draw(screen)  # removes the eaten white
                                    self.table[row + 2][col - 2].inside = None  # updates the inside of from_cell
                                    self.table[row + 1][col - 1].inside = None  # updates the inside of eaten white cell
                                    self.num_of_whites -= 1  # update num of whites

                                    screen.blit(black_piece, (self.table[row][col].x, self.table[row][col].y))  # places to_cell
                                    self.table[row][col].inside = "black"  # update the inside of to_cell
                                    pygame.display.flip()
                                    return True
                    elif from_cell.is_king:  # placing kings
                        from_cell.draw(screen)  # deleting from_cell
                        from_cell.inside = None  # updates the inside of from_cell
                        from_cell.is_king = False  # updates the kingness of from_cell
                        screen.blit(black_king, (self.table[row][col].x, self.table[row][col].y))  # places to_cell
                        self.table[row][col].inside = "black"  # update the inside of to_cell
                        self.table[row][col].is_king = True  # updates kingness
                        pygame.display.flip()
                        return True
        return False

    def __copy__(self):
        board_copy = Board(self.x, self.y, self.width, self.height)

    def in_board(self, x, y):
        if (self.x <= x <= self.x + self.width) and (self.y <= y <= self.y + self.height):
            return True
        return False
