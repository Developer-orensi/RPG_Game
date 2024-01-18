import pygame
import random

# 게임 화면 크기
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# 셀 크기
CELL_SIZE = 40

# 게임 판 크기
BOARD_SIZE = 10

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("지뢰찾기")

clock = pygame.time.Clock()

game_over = False

board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]  # 게임 판 초기화
revealed = [[False] * BOARD_SIZE for _ in range(BOARD_SIZE)]  # 셀이 공개되었는지 여부를 저장하는 배열

# 지뢰 배치
num_mines = 10
mines = random.sample(range(BOARD_SIZE * BOARD_SIZE), num_mines)
for mine in mines:
    row = mine // BOARD_SIZE
    col = mine % BOARD_SIZE
    board[row][col] = -1

# 주변 지뢰 개수 계산
for row in range(BOARD_SIZE):
    for col in range(BOARD_SIZE):
        if board[row][col] != -1:
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= row + i < BOARD_SIZE and 0 <= col + j < BOARD_SIZE:
                        if board[row + i][col + j] == -1:
                            count += 1
            board[row][col] = count

def reveal_cell(row, col):
    if revealed[row][col]:
        return

    revealed[row][col] = True

    if board[row][col] == 0:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= row + i < BOARD_SIZE and 0 <= col + j < BOARD_SIZE:
                    reveal_cell(row + i, col + j)

def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            if revealed[row][col]:
                pygame.draw.rect(screen, WHITE, [x, y, CELL_SIZE, CELL_SIZE])
                if board[row][col] > 0:
                    font = pygame.font.Font(None, 30)
                    text = font.render(str(board[row][col]), True, BLACK)
                    text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                    screen.blit(text, text_rect)
            else:
                pygame.draw.rect(screen, GRAY, [x, y, CELL_SIZE, CELL_SIZE])

            pygame.draw.rect(screen, BLACK, [x, y, CELL_SIZE, CELL_SIZE], 1)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                col = pos[0] // CELL_SIZE
                row = pos[1] // CELL_SIZE
                reveal_cell(row, col)
                if board[row][col] == -1:
                    game_over = True

    screen.fill(BLACK)
    draw_board()
    pygame.display.flip()

    clock.tick(30)  # 게임의 속도 설정

pygame.quit()
