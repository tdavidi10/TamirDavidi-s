# Import and initialize the pygame library
import const
import pygame

pygame.init()
from Board import *

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Damka')  # headline
programIcon = pygame.image.load('images/BlackKing.png')  # icon
pygame.display.set_icon(programIcon)  # icon

# Run until the user asks to quit
running = True
board = Board()
ai = AI()
board.draw(screen)
click = -1  # choose \ place black
from_cell = Cell()
is_placed = False


def activate_AI(screen, board):  # calls the make_move method of AI
    time.sleep(COMP_SPEED)
    ai.make_white_move(screen, board)
    pygame.display.flip()


while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # handle MOUSEBUTTONDOWN
        if event.type == pygame.MOUSEBUTTONDOWN:
            click += 1
            pos = pygame.mouse.get_pos()
            if click % 2 == 0:  # choose black click
                from_cell = board.mouse_click_choose_cell(screen, pos[0], pos[1])
                if from_cell == "not played":
                    click -= 1
            elif click % 2 == 1:  # place black click
                is_placed = board.mouse_click_place_cell(screen, pos[0], pos[1], from_cell)  # black moves
                if is_placed:
                    board.apply_black_kings(screen)  # applies black kings
                    activate_AI(screen, board)  # now white moves
                    board.apply_white_kings(screen)  # applies white kings
                else:
                    click -= 1

# Done! Time to quit.
pygame.quit()
