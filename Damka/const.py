import ctypes

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
SCREEN_WIDTH = screensize[0]
SCREEN_HEIGHT = screensize[1]

BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BROWN = (133, 88, 70)
LIGHT_BROWN = (255, 229, 186)

WIDTH = SCREEN_HEIGHT - 100
HEIGHT = SCREEN_HEIGHT - 100

CELL_WIDTH = WIDTH // 8
CELL_HEIGHT = HEIGHT // 8

COMP_SPEED = 0.8