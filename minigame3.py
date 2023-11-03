import pygame
import logging
import sys
import time

def CCC():

    #logging.basicConfig(level=logging.DEBUG,  # 로그 레벨 (DEBUG, INFO, WARNING, ERROR, CRITICAL 중 선택)
    #                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger = logging.getLogger(__name__)

    # 초기화
    pygame.init()

    # 화면 크기
    screen_width = 1080
    screen_height = 720

    # 색상 정의
    black = (0, 0, 0)
    white = (255, 255, 255)

    # 게임 창 생성
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("참참참 게임")

    # 폰트 설정
    font = pygame.font.SysFont("malgungothic", 36)

    # 플레이어 초기 위치
    player1_x = screen_width // 4
    player2_x = 3 * screen_width // 4
    y = screen_height // 2

    left_image = pygame.image.load("resource/left.png")
    right_image = pygame.image.load("resource/right.png")

    scaled_left_image = pygame.transform.scale(left_image, (100, 100))
    scaled_right_image = pygame.transform.scale(right_image, (100, 100))

    player1_score = 0
    player2_score = 0

    final_win_player = None



    start_time = time.time()

    player1_choice = "입력하지 않음"
    player2_choice = "입력하지 않음"

    player1_image = None
    player2_image = None

    # 초기화면 표시
    def show_start_screen(countdown):
        screen.fill(white)
        screen.blit(scaled_left_image, (100, 500))
        screen.blit(scaled_right_image, (250, 500))
        screen.blit(scaled_left_image, (750, 500))
        screen.blit(scaled_right_image, (900, 500))
        text = font.render(str(countdown), True, black)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)
        font2 = pygame.font.SysFont("malgungothic", 16)
        text2 = font2.render("플레이어 1 : 공", True, black)
        text3 = font2.render("왼쪽 : A키, 오른쪽 : D키", True, black)
        text4 = font2.render("플레이어 2 : 수", True, black)
        text5 = font2.render("왼쪽 : J키, 오른쪽 : L키", True, black)
        screen.blit(text2, (130, 400))
        screen.blit(text3, (100, 420))
        screen.blit(text4, (730, 400))
        screen.blit(text5, (700, 420))

    # 결과 화면 표시
    def show_result(result):
        screen.fill(white)
        if player1_image:
            screen.blit(player1_image, (200, 500))
        if player2_image:
            screen.blit(player2_image, (800, 500))
        text = font.render(result, True, black)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)

    # 게임 루프
    running = True
    result = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            player1_choice = "왼쪽"
            player1_image = scaled_left_image
            logger.debug(player1_choice)
        elif keys[pygame.K_d]:
            player1_choice = "오른쪽"
            player1_image = scaled_right_image
            logger.debug(player1_choice)

        if keys[pygame.K_j]:
            player2_choice = "왼쪽"
            player2_image = scaled_left_image
            logger.debug(player2_choice)
        elif keys[pygame.K_l]:
            player2_choice = "오른쪽"
            player2_image = scaled_right_image
            logger.debug(player2_choice)

        show_start_screen(5 - int(time.time() - start_time))
        pygame.display.update()

        if time.time() - start_time > 5:
            if player1_choice == player2_choice:
                result = "똑같음! -> player1 승리"
                player1_score += 1
            else:
                win_player = "player 2"
                player2_score += 1
                if player1_choice != "입력하지 않음" and player2_choice == "입력하지 않음":
                    win_player = "player 1"
                    player1_score += 1
                result = f"플레이어 1: {player1_choice}, 플레이어 2: {player2_choice} -> {win_player} 승리!"

            show_result(result)
            pygame.display.update()
            pygame.time.delay(3000)  # 3초 대기

            start_time = time.time()
            player1_choice = "입력하지 않음"
            player2_choice = "입력하지 않음"
            player1_image = None
            player2_image = None

            if player1_score >= 2:
                final_win_player = "player 1"
                running = False
                return 1

            if player2_score >= 2:
                final_win_player = "player 2"
                running = False
                return 2

    screen.fill(white)
    text = font.render(f"최종 승리자 : {final_win_player}", True, black)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(3000)  # 3초 대기

if __name__ == "__main__":
    winner = CCC()
    sys.exit(winner)