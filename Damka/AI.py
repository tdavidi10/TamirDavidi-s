import pygame
from const import *
from Board import *
import copy


def is_victory(board, win_color):
    table = board.table
    for row in range(8):
        for col in range(8):
            if table[row][col].inside != win_color and table[row][col].inside is not None:  # if there is rival left
                return False
    return True


def is_defeat(board, lose_color):
    table = board.table
    for row in range(8):
        for col in range(8):
            if table[row][col].inside == lose_color:  # if even one survive, no defeat
                return False
    return True


def max_option(option_lst):  # return the option with the max val
    max_val = -1
    best_option = None
    for option in option_lst:
        if option.val > max_val:
            max_val = option.val
            best_option = option
    return best_option


class Option:  # board after step, val, from step, to step

    def __init__(self, board_option=None, val=0, from_cell=None, to_cell=None, is_eating=False, eaten_cell=()):
        self.board_option = board_option
        self.val = val
        self.from_cell = from_cell  # tuple - (row, col)
        self.to_cell = to_cell  # tuple - (row, col)
        self.is_eating = is_eating
        self.eaten_cell = eaten_cell # tuple - (row, col)


class AI:

    def create_options_list(self, board):  # for every white left creates options of his steps
        options = list()
        copy_board_right = copy.deepcopy(board)  # creates copy of original board
        right_val = 0
        right_from_cell = None
        right_to_cell = None
        copy_board_left = copy.deepcopy(board)  # creates copy of original board
        left_val = 0
        left_from_cell = None
        left_to_cell = None
        for row in range(8):
            for col in range(8):
                if board.table[row][col].inside == "white":  # for each white left
                    # resets the fields of option for each cell
                    copy_board_right = copy.deepcopy(board)  # creates copy of original board
                    right_val = 0
                    right_from_cell = None
                    right_to_cell = None
                    copy_board_left = copy.deepcopy(board)  # creates copy of original board
                    left_val = 0
                    left_from_cell = None
                    left_to_cell = None
                    # non-eating step option - regular piece
                    if row + 1 <= 7:  # if white can go down
                        if col + 1 <= 7:  # if white can go right
                            if board.table[row + 1][col + 1].inside is None:  # if there is nothing in right-down
                                # updates option board
                                copy_board_right.table[row][col].inside = None  # updates inside of from_cell
                                copy_board_right.table[row + 1][col + 1].inside = "white"  # # updates inside of to_cell
                                right_val = self.eval(copy_board_right)
                                right_from_cell = (row, col)
                                right_to_cell = (row + 1, col + 1)
                                options.append(Option(copy_board_right, right_val, right_from_cell, right_to_cell))
                        if col - 1 >= 0:  # if white can go right
                            if board.table[row + 1][col - 1].inside is None:  # if there is nothing in left-down
                                # updates option board
                                copy_board_left.table[row][col].inside = None  # updates inside of from_cell
                                copy_board_left.table[row + 1][col - 1].inside = "white"  # # updates inside of to_cell
                                left_val = self.eval(copy_board_left)
                                left_from_cell = (row, col)
                                left_to_cell = (row + 1, col - 1)
                                options.append(Option(copy_board_left, left_val, left_from_cell, left_to_cell))
                    # eating step option - regular piece
                    # resets the fields of option for each cell
                    copy_board_right_right = copy.deepcopy(board)  # creates copy of original board
                    right_right_val = 0
                    right_right_from_cell = None
                    right_right_to_cell = None
                    copy_board_left_left = copy.deepcopy(board)  # creates copy of original board
                    left_left_val = 0
                    left_left_from_cell = None
                    left_left_to_cell = None
                    if row + 2 <= 7:  # if white can 2 rows down -- eat right down
                        if col + 2 <= 7:  # if white can go 2 cols right
                            if board.table[row + 2][col + 2].inside is None:  # if there is nothing in to_cell
                                if board.table[row + 1][col + 1].inside == "black":  # if there is black to eat
                                    # updates option board
                                    copy_board_right_right.table[row][col].inside = None  # updates inside of from_cell
                                    copy_board_right_right.table[row + 2][col + 2].inside = "white"  # # updates inside of to_cell
                                    copy_board_right_right.table[row + 1][col + 1].inside = None  # updates inside of eaten
                                    copy_board_right_right.num_of_blacks -= 1  # updates n_o blacks
                                    right_right_val = self.eval(copy_board_right_right)
                                    right_right_from_cell = (row, col)
                                    right_right_to_cell = (row + 2, col + 2)
                                    options.append(Option(copy_board_right_right, right_right_val, right_right_from_cell, right_right_to_cell, True, (row + 1, col + 1)))
                        if col - 2 >= 0:  # if white can go 2 cols left
                            if board.table[row + 2][col - 2].inside is None:  # if there is nothing in to_cell
                                if board.table[row + 1][col - 1].inside == "black":  # if there is black to eat
                                    # updates option board
                                    copy_board_left_left.table[row][col].inside = None  # updates inside of from_cell
                                    copy_board_left_left.table[row + 2][col - 2].inside = "white"  # # updates inside of to_cell
                                    copy_board_left_left.table[row + 1][col - 1].inside = None  # updates inside of eaten
                                    copy_board_left_left.num_of_blacks -= 1  # updates n_o blacks
                                    left_left_val = self.eval(copy_board_left_left)
                                    left_left_from_cell = (row, col)
                                    left_left_to_cell = (row + 2, col - 2)
                                    options.append(Option(copy_board_left_left, left_left_val, left_left_from_cell, left_left_to_cell, True, (row + 1, col - 1)))

        return options

    def eval(self, board):  # gets a board, returns his value 0-1000
        if is_victory(board, "white"):
            return 120

        elif board.num_of_blacks == 11:
            return 10

        elif board.num_of_blacks == 10:
            return 20

        elif board.num_of_blacks == 9:
            return 30

        elif board.num_of_blacks == 8:
            return 40

        elif board.num_of_blacks == 7:
            return 50

        elif board.num_of_blacks == 6:
            return 60

        elif board.num_of_blacks == 5:
            return 70

        elif board.num_of_blacks == 4:
            return 80

        elif board.num_of_blacks == 3:
            return 90

        elif board.num_of_blacks == 2:
            return 100

        elif board.num_of_blacks == 1:
            return 110

        elif is_defeat(board, "white"):
            return 0

        else:
            return 0

    def make_white_move(self, screen, board):
        option_lst = self.create_options_list(board)
        best_option = max_option(option_lst)
        from_cell_row = best_option.from_cell[0]
        from_cell_col = best_option.from_cell[1]
        to_cell_row = best_option.to_cell[0]
        to_cell_col = best_option.to_cell[1]
        eaten_cell_row = -1
        eaten_cell_col = -1

        if best_option.is_eating:
            eaten_cell_row = best_option.eaten_cell[0]
            eaten_cell_col = best_option.eaten_cell[1]
            board.num_of_blacks -= 1


        white_piece = pygame.image.load('images/WhitePiece.png')
        white_piece = pygame.transform.scale(white_piece, (CELL_WIDTH, CELL_HEIGHT))
        # make the move of best option

        board.table[from_cell_row][from_cell_col].draw(screen)  # removes from_cell
        board.table[from_cell_row][from_cell_col].inside = None  # updates the inside of from_cell
        screen.blit(white_piece, (board.table[to_cell_row][to_cell_col].x, board.table[to_cell_row][to_cell_col].y))  # places to_cell
        board.table[to_cell_row][to_cell_col].inside = "white"  # update the inside of to_cell
        if best_option.is_eating:
            board.table[eaten_cell_row][eaten_cell_col].draw(screen)
            board.table[eaten_cell_row][eaten_cell_col].inside = None  # updates the inside of eaten white cell
        return None  # moves one piece and out
