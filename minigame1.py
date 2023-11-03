import pygame
import sys


def tabtab():
    # Pygame 초기화
    pygame.init()

    # 화면 크기 및 초기 위치 설정
    screen_width = 1080
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("게임")

    # 도형1과 도형2 초기 설정
    rect1 = pygame.Rect(300, 500, 100, 50)  # 도형1
    rect2 = pygame.Rect(700, 500, 100, 50)  # 도형2

    # 게임 오버 텍스트 설정
    font = pygame.font.Font("resource/Maplestory Light.ttf", 60)
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))

    background_image = pygame.image.load("resource/background.png")
    scaled_background_image = pygame.transform.scale(background_image, (1080, 720))
    # 배경 이미지의 알파 채널 활성화
    scaled_background_image = scaled_background_image.convert_alpha()
    # 배경 이미지의 투명도 설정 (0부터 255까지의 값, 0은 완전 투명, 255는 완전 불투명)
    alpha_value = 128  # 예: 128은 중간 투명도
    scaled_background_image.set_alpha(alpha_value)

    # 키 눌림 상태 추적 변수 초기화
    player1_key_pressed = [False, False, False]
    player2_key_pressed = [False, False, False]

    max_height = 400

    count1 = 0
    count2 = 0

    flag1 = 0
    flag2 = 0

    # 늘어나는 길이
    increase_height = 5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                return 0

        # 키 입력 처리
        keys = pygame.key.get_pressed()

        flag1 += 1
        flag2 += 1

        # 'a' 키 처리
        if keys[pygame.K_a] and not player1_key_pressed[0]:
            rect1.height += increase_height  # 높이를 increase_height씩 늘립니다
            rect1.y -= increase_height
            player1_key_pressed[0] = True
            count1 += 1
        elif not keys[pygame.K_a]:
            player1_key_pressed[0] = False

        # 's' 키 처리
        if keys[pygame.K_s] and not player1_key_pressed[1]:
            rect1.height += increase_height  # 높이를 increase_height씩 늘립니다
            rect1.y -= increase_height
            player1_key_pressed[1] = True
            count1 += 1
        elif not keys[pygame.K_s]:
            player1_key_pressed[1] = False

        # 'd' 키 처리
        if keys[pygame.K_d] and not player1_key_pressed[2]:
            rect1.height += increase_height  # 높이를 increase_height씩 늘립니다
            rect1.y -= increase_height
            player1_key_pressed[2] = True
            count1 += 1
        elif not keys[pygame.K_d]:
            player1_key_pressed[2] = False



        # 'j' 키 처리
        if keys[pygame.K_j] and not player2_key_pressed[0]:
            rect2.height += increase_height  # 높이를 increase_height씩 늘립니다
            rect2.y -= increase_height
            player2_key_pressed[0] = True
            count2 += 1
        elif not keys[pygame.K_j]:
            player2_key_pressed[0] = False

        # 'k' 키 처리
        if keys[pygame.K_k] and not player2_key_pressed[1]:
            rect2.height += increase_height  # 높이를 increase_height씩 늘립니다
            rect2.y -= increase_height
            player2_key_pressed[1] = True
            count2 += 1
        elif not keys[pygame.K_k]:
            player2_key_pressed[1] = False

        # 'l' 키 처리
        if keys[pygame.K_l] and not player2_key_pressed[2]:
            rect2.height += increase_height  # 높이를 increase_height씩 늘립니다
            rect2.y -= increase_height
            player2_key_pressed[2] = True
            count2 += 1
        elif not keys[pygame.K_l]:
            player2_key_pressed[2] = False

        # 게임 오버 조건 확인
        if rect1.height >= max_height or rect2.height < 50:
            game_over_text = font.render("플레이어1의 승리", True, (255, 0, 0))
            game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.fill((0, 0, 0))  # 화면을 검은색으로 지웁니다.
            screen.blit(game_over_text, game_over_rect)  # 게임 오버 텍스트를 표시합니다.
            pygame.display.flip()  # 화면 업데이트
            pygame.time.delay(2000)  # 2초 동안 게임 오버 화면을 보여줍니다.
            return 1

        if count1 > 10 and flag1 > 100:
            rect1.height -= 1  # 높이를 increase_height씩 늘립니다
            rect1.y += 1
            flag1 = 0

        if rect2.height >= max_height or rect1.height < 50:
            game_over_text = font.render("플레이어2의 승리", True, (0, 0, 255))
            game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.fill((0, 0, 0))  # 화면을 검은색으로 지웁니다.
            screen.blit(game_over_text, game_over_rect)  # 게임 오버 텍스트를 표시합니다.
            pygame.display.flip()  # 화면 업데이트
            pygame.time.delay(2000)  # 2초 동안 게임 오버 화면을 보여줍니다.
            return 2

        if count2 > 10 and flag2 > 100:
            rect2.height -= 1  # 높이를 increase_height씩 늘립니다
            rect2.y += 1
            flag2 = 0

        # 화면 업데이트
        screen.blit(scaled_background_image, (0, 0))
        font = pygame.font.Font("resource/Maplestory Light.ttf", 16)
        text1 = font.render("Player 1", True, (255, 0, 0))
        text2 = font.render("Player 2", True, (0, 0, 255))
        screen.blit(text1, (310, 570))
        screen.blit(text2, (710, 570))
        pygame.draw.rect(screen, (255, 0, 0), rect1)  # 도형1 그리기
        pygame.draw.rect(screen, (0, 0, 255), rect2)  # 도형2 그리기
        pygame.display.flip()

if __name__ == "__main__":
    winner = tabtab()
    sys.exit(winner)