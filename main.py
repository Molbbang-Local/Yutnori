import pygame
import sys
import random
from minigame1 import tabtab
from minigame2 import RCP
from minigame3 import CCC
import os

# Pygame 초기화
pygame.init()
# 화면 설정
screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

intro_image = pygame.image.load('resource/intro.png')
blue_win_image = pygame.image.load('resource/bluewin.png')
red_win_image = pygame.image.load('resource/redwin.png')
red_vic_image = pygame.image.load('resource/redvic.png')
blue_vic_image = pygame.image.load('resource/bluevic.png')

sub_game_flag = 0
redwin = 0
bluewin = 0

# 배경 이미지 로드
background = pygame.image.load('resource/field.jpg')

# 폰트 설정
pygame.font.init()  # 폰트 모듈 초기화
font = pygame.font.SysFont("arial", 36)  # 기본 폰트와 크기 설정

# node 변수 초기화
node = None

# 노드 값에 대한 좌표 범위를 저장하는 딕셔너리
node_ranges = {
    -1: (800, 515),
    0: (715, 515),
    1: (715, 445),
    2: (715, 385),
    3: (715, 325),
    4: (715, 265),
    5: (715, 195),
    6: (635, 195),
    7: (574, 195),
    8: (515, 195),
    9: (455, 195),
    10: (375, 195),
    11: (375, 265),
    12: (375, 325),
    13: (375, 385),
    14: (375, 445),
    15: (375, 515),
    16: (455, 515),
    17: (515, 515),
    18: (575, 515),
    19: (635, 515),
    20: (715, 515),
    21: (650, 255),
    22: (445, 255),
    23: (615, 295),
    24: (485, 295),
    25: (540, 355),
    26: (615, 415),
    27: (485, 415),
    28: (650, 460),
    29: (440, 460),
}

def draw_map():
    for node, (x_mid, y_mid) in node_ranges.items():
        pygame.draw.circle(screen, (0, 0, 0), (x_mid, y_mid), 25, 2)  # 2픽셀 두께의 테두리로 그리기

# 버튼 설정
button_color = (69, 193, 118)  # 버튼의 색상, 여기서는 빨간색
button_position = (380, 600)  # 버튼의 위치
button_size = (350, 50)  # 버튼의 크기
button_rect = pygame.Rect(button_position, button_size)  # 버튼의 Rect 객체

# 텍스트 위치 설정
text_position = (400, 50)

# 게임 상태 변수
current_player = 'player1'
turn_stage = 'btn_press'  # 'btn_press' 또는 'node_select'

# 윷 변수
yut = [0, 0, 0, 0, 0]
yut_front = pygame.image.load('resource/yut_front.png')
yut_back = pygame.image.load('resource/yut_back.png')

# 윷 던지기 메서드
def throw_yut():
    yut[0] = 0
    for i in range(1, 5):
        yut[i] = random.randint(0, 1)
        yut[0] += yut[i]
    if yut[0] == 0:
        yut[0] = 5

def draw_yut():
    for i in range(1, 5):
        if yut[i] == 1 :
            screen.blit(yut_back, (210 + 100 * i, 200))
        else :
            screen.blit(yut_front, (210 + 100 * i, 200))



# 노드 선택 함수
def check_node_value(mouse_pos, markable):
    for node, (x_mid, y_mid) in node_ranges.items():
        if x_mid - 15 <= mouse_pos[0] <= x_mid + 15 and y_mid - 15 <= mouse_pos[1] <= y_mid + 15:
            if node in markable:
                return node
    return None

# player 말
# marker = [node, mid, height]
marker1 = [0, (715, 515), 1]
marker2 = [0, (715, 515), 1]
markable = []
# 말 설정
marker1_color = (255, 0, 0)  # 버튼의 색상, 여기서는 빨간색
marker1_image = pygame.image.load('resource/marker1.png')
marker2_color = (0, 0, 255)  # 버튼의 색상, 여기서는 파란색
marker2_image = pygame.image.load('resource/marker2.png')
# 말의 위치를 업데이트하는 함수
def update_marker(marker, node):
    marker[0] = node
    marker[1] = node_ranges[node]  # 노드 범위 중앙값을 사용

mark_pointer = pygame.image.load('resource/pointer.png')
def draw_pointer(marker):
    markable.clear()
    if marker[0] == 20:
        markable.append(-1)
    if marker[0] + yut[0] <= 20:
        markable.append(marker[0] + yut[0])
    if marker[0] < 20 and marker[0] + yut[0] > 20:
        markable.append(-1)
    if marker[0] == 5:
        if yut[0] == 1:
            markable.append(21)
        if yut[0] == 2:
            markable.append(23)
        if yut[0] == 3:
            markable.append(25)
        if yut[0] == 4:
            markable.append(27)
        if yut[0] == 5:
            markable.append(29)
    elif marker[0] == 21:
        if yut[0] == 1:
            markable.append(23)
        if yut[0] == 2:
            markable.append(25)
        if yut[0] == 3:
            markable.append(27)
        if yut[0] == 4:
            markable.append(29)
        if yut[0] == 5:
            markable.append(15)
    elif marker[0] == 23:
        if yut[0] == 1:
            markable.append(25)
        if yut[0] == 2:
            markable.append(27)
        if yut[0] == 3:
            markable.append(29)
        if yut[0] == 4:
            markable.append(15)
        if yut[0] == 5:
            markable.append(16)
    elif marker[0] == 27:
        if yut[0] == 1:
            markable.append(29)
        if yut[0] == 2:
            markable.append(15)
        if yut[0] == 3:
            markable.append(16)
        if yut[0] == 4:
            markable.append(17)
        if yut[0] == 5:
            markable.append(18)
    elif marker[0] == 29:
        if yut[0] == 1:
            markable.append(15)
        if yut[0] == 2:
            markable.append(16)
        if yut[0] == 3:
            markable.append(17)
        if yut[0] == 4:
            markable.append(18)
        if yut[0] == 5:
            markable.append(19)
    elif marker[0] == 10:
        if yut[0] == 1:
            markable.append(22)
        if yut[0] == 2:
            markable.append(24)
        if yut[0] == 3:
            markable.append(25)
        if yut[0] == 4:
            markable.append(26)
        if yut[0] == 5:
            markable.append(28)
    elif marker[0] == 22:
        if yut[0] == 1:
            markable.append(24)
        if yut[0] == 2:
            markable.append(25)
        if yut[0] == 3:
            markable.append(26)
        if yut[0] == 4:
            markable.append(28)
        if yut[0] == 5:
            markable.append(20)
    elif marker[0] == 24:
        if yut[0] == 1:
            markable.append(25)
        if yut[0] == 2:
            markable.append(26)
        if yut[0] == 3:
            markable.append(28)
        if yut[0] == 4:
            markable.append(20)
        if yut[0] == 5:
            markable.append(-1)
    elif marker[0] == 26:
        if yut[0] == 1:
            markable.append(28)
        if yut[0] == 2:
            markable.append(20)
        if yut[0] == 3:
            markable.append(20)
        if yut[0] == 4:
            markable.append(-1)
        if yut[0] == 5:
            markable.append(-1)
    elif marker[0] == 28:
        if yut[0] == 1:
            markable.append(20)
        if yut[0] == 2:
            markable.append(-1)
        if yut[0] == 3:
            markable.append(-1)
        if yut[0] == 4:
            markable.append(-1)
        if yut[0] == 5:
            markable.append(-1)
    elif marker[0] == 25:
        if yut[0] == 1:
            markable.append(26)
            markable.append(27)
        if yut[0] == 2:
            markable.append(28)
            markable.append(29)
        if yut[0] == 3:
            markable.append(20)
            markable.append(15)
        if yut[0] == 4:
            markable.append(-1)
            markable.append(16)
        if yut[0] == 5:
            markable.append(-1)
            markable.append(17)

    print(f"markable {markable}")
    for able in markable:
        screen.blit(mark_pointer, (node_ranges[able][0] - 30, node_ranges[able][1] - 30))

score1 = 0
score2 = 0

winner = 0

def main_stream(score1, score2):
    # 배경 이미지를 화면에 그리기
    screen.blit(background, (0, 0))

    if turn_stage == 'visual_yut':
        draw_yut()

    if turn_stage == 'node_select':
        if current_player == 'player2':
            draw_pointer(marker2)
        elif current_player == 'player1':
            draw_pointer(marker1)

    # draw_map()
    # 버튼 그리기
    pygame.draw.rect(screen, button_color, button_rect)

    # 텍스트 렌더링
    status_text = font.render(f"{current_player} {turn_stage}", True, (0, 0, 0))
    screen.blit(status_text, text_position)
    if turn_stage == 'btn_press':
        status_text = font.render(f"Throw YUT", True, (255, 255, 255))
        screen.blit(status_text, (button_position[0] + 100, button_position[1]))
    if turn_stage == 'visual_yut':
        status_text = font.render(f"X", True, (255, 255, 255))
        screen.blit(status_text, (button_position[0] + 150, button_position[1]))

    # 말 그리기
    if marker1[0] != -1:
        screen.blit(marker1_image, (marker1[1][0] - 25, marker1[1][1] - 25))
    else:
        redwin = 1
    if marker2[0] != -1:
        screen.blit(marker2_image, (marker2[1][0] - 35, marker2[1][1] - 35))
    else:
        bluewin = 1
intro = 1
# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 마우스 버튼이 눌렸는지 확인
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 현재 플레이어의 btn_press 단계에서만 버튼 클릭을 처리
            if turn_stage == 'btn_press':
                if button_rect.collidepoint(event.pos):
                    print(f"{current_player} pressed the button!")
                    throw_yut()
                    print(f"{current_player} threw yut: {yut}")
                    turn_stage = 'visual_yut'  # 다음 단계로 이동

            elif turn_stage == 'visual_yut':
                if button_rect.collidepoint(event.pos):
                    turn_stage = 'node_select'

            # 현재 플레이어의 node_select 단계에서만 노드 선택을 처리
            elif turn_stage == 'node_select':
                new_node = check_node_value(event.pos, markable)
                if new_node is not None:
                    node = new_node
                    print(f"Node value changed to {node}")
                    current_player = 'player2' if current_player == 'player1' else 'player1'
                    turn_stage = 'btn_press'  # 다음 플레이어의 btn_press 단계로 이동
                    if current_player == 'player1':
                        update_marker(marker2, new_node)
                    elif current_player == 'player2':
                        update_marker(marker1, new_node)

    main_stream(score1, score2)

    if marker1[0] != 0 and marker1[0] == marker2[0]:

        ran = random.random()
        sub_game_flag = 0
        if ran >= 0.5:
            winner = tabtab()
        elif ran >= 0.25:
            winner = CCC()
        else:
            winner = RCP()
        print(f"The winner is: Player {winner}")
        if winner == 2:
            marker1[0] = 0
            marker1[1] = node_ranges[0]
            screen.blit(blue_win_image, (0, 0))
        elif winner == 1:
            marker2[0] = 0
            marker2[1] = node_ranges[0]
            screen.blit(red_win_image, (0, 0))
        sub_game_flag = 1

    if marker1[0] == -1:
        screen.blit(red_vic_image, (0,0))
    elif marker2[0] == -1:
        screen.blit(blue_vic_image, (0,0))


    if intro == 1:
        screen.blit(intro_image, (0,0))
    # 화면 업데이트
    pygame.display.update()

    if intro == 1:
        screen.blit(intro_image, (0,0))
        pygame.time.delay(2000)
        intro = 0

    if marker1[0] == -1:
        pygame.time.delay(3000)
        break
    elif marker2[0] == -1:
        pygame.time.delay(3000)
        break


    if sub_game_flag == 1:
        pygame.time.delay(3000)
        sub_game_flag = 0






# Pygame 종료
pygame.quit()
sys.exit()
