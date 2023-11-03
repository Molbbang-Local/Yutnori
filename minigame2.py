import time
import sys
import pygame
import random

def RCP():

    # 초기화
    pygame.init()

    font = pygame.font.SysFont("malgungothic", 36) # 시스템 폰트 사용 시

    # 화면 설정
    WIDTH, HEIGHT = 1080, 720
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("플레이어 vs 플레이어 가위바위보 게임")
    # 색상 정의
    WHITE = (255, 255, 255)

    # 가위바위보 옵션
    choices = ["rock", "paper", "scissors"]
    player1_choice = None
    player2_choice = None
    player1_i = None
    player2_i = None

    # 키 매핑
    key_mapping = {
        pygame.K_a: "rock",
        pygame.K_s: "paper",
        pygame.K_d: "scissors"
    }

    # 승자 결정 함수
    def determine_winner(player1, player2):
        if player1 == player2:
            return "      무승부"
        if (player1 == "rock" and player2 == "scissors") or \
           (player1 == "paper" and player2 == "rock") or \
           (player1 == "scissors" and player2 == "paper"):
            return "플레이어 1 승리"
        return "플레이어 2 승리"

    # 초기화
    player1_wins = 0
    player2_wins = 0
    winner = None
    rounds_played = 0
    required_wins = 2  # 두 판 이기면 최종 승자


    # 게임 루프
    run = True
    player_turn = 1

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key in key_mapping:
                    choice = key_mapping[event.key]

                    if player_turn == 1:
                        win.fill(WHITE)

                        player1_choice = choice
                        player_turn = 2


                        #time.sleep(1000)

                    elif player_turn == 2:

                        player2_choice = choice
                        text_choices = font.render("플레이어 2 선택 완료", True, (0, 0, 0))
                        win.blit(text_choices, (320, 450))
                        #time.sleep(1000)
                        if player1_choice and player2_choice:
                            winner = determine_winner(player1_choice, player2_choice)
                            rounds_played += 1
                            if winner == "플레이어 1 승리":
                                player1_wins += 1
                            elif winner == "플레이어 2 승리":
                                player2_wins += 1
                            if player1_wins >= required_wins or player2_wins >= required_wins:
                                run = False
                            else:
                                player_turn = 1
        # 화면 지우기
        win.fill(WHITE)
        if player_turn==2:
            text_choices = font.render("플레이어 1 선택 완료", True, (0, 0, 0))
            win.blit(text_choices, (250, 50))
            pygame.time.delay(500)


        # 플레이어 선택 표시
        if player1_choice and player2_choice:
            player1_image = pygame.image.load(f"resource/{player1_choice}.png")
            player2_image = pygame.image.load(f"resource/{player2_choice}.png")
            win.blit(player1_image, (200, 200))
            text_choices = font.render("플레이어 1", True, (0, 0, 0))
            win.blit(text_choices, (200, 400))
            win.blit(player2_image, (400, 200))
            text_choices = font.render("플레이어 2", True, (0, 0, 0))
            win.blit(text_choices, (400, 400))


        # 승자 표시
        if winner:
            text_winner = font.render(winner, True, (0, 0, 0))
            win.blit(text_winner, (280, 450))

        # 현재 스코어 표시
        score_text = font.render(f"플레이어 1: {player1_wins} vs 플레이어 2: {player2_wins}", True, (0, 0, 0))
        win.blit(score_text, (250, 550))

        # 화면 업데이트
        pygame.display.update()
        pygame.time.delay(500)
        win.fill(WHITE)

    # 최종 승자 결정
    if player1_wins >= 2:
        final_winner = "플레이어 1 최종 승리"
        return 1
    else:
        final_winner = "플레이어 2 최종 승리"
        return 2
    pygame.time.delay(1500)
    if  player1_wins >= 2:
        win.fill(WHITE)
    if player2_wins >= 2:
        win.fill(WHITE)
    # 최종 승자와 선택 표시
    text_winner = font.render("최종 승자는! " + final_winner, True, (0, 0, 0))
    win.blit(text_winner, (120, 250))

    # 화면 업데이트
    pygame.display.update()

    # 게임 종료
    pygame.time.delay(3000)  # 결과 표시를 몇 초 동안 보여줌
    return 0

if __name__ == "__main__":
    winner = RCP()
    sys.exit(winner)