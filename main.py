import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 설정
screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 배경 이미지 로드
background = pygame.image.load('resource/fieldN.jpg')

# node 변수 초기화
node = None

# 노드 값에 대한 좌표 범위를 저장하는 딕셔너리
node_ranges = {
    0: ((700, 725), (500, 530)),
    1: ((700, 725), (430, 460)),
    2: ((700, 725), (370, 400)),
    3: ((700, 725), (310, 340)),
    4: ((700, 725), (250, 280)),
    5: ((700, 725), (180, 210)),
    6: ((620, 650), (180, 210)),
    7: ((560, 590), (180, 210)),
    8: ((500, 530), (180, 210)),
    9: ((440, 470), (180, 210)),
    10: ((360, 390), (180, 210)),
    11: ((360, 390), (250, 280)),
    12: ((360, 390), (310, 340)),
    13: ((360, 390), (370, 400)),
    14: ((360, 390), (430, 460)),
    15: ((360, 390), (500, 530)),
    16: ((440, 470), (500, 530)),
    17: ((500, 530), (500, 530)),
    18: ((560, 590), (500, 530)),
    19: ((620, 650), (500, 530)),
    21: ((635, 665), (240, 270)),
    22: ((430, 460), (240, 270)),
    23: ((600, 630), (280, 310)),
    24: ((470, 500), (280, 310)),
    25: ((525, 555), (340, 370)),
    26: ((600, 630), (400, 430)),
    27: ((470, 500), (400, 430)),
    28: ((635, 655), (445, 475)),
    29: ((430, 455), (445, 475)),
}

def check_node_value(mouse_pos):
    """
    마우스 위치에 따라 node 값을 결정하는 함수
    """
    for node, ((x_start, x_end), (y_start, y_end)) in node_ranges.items():
        if x_start <= mouse_pos[0] <= x_end and y_start <= mouse_pos[1] <= y_end:
            return node
    return None

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 마우스 버튼이 눌렸는지 확인
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 함수를 사용하여 node 값 설정
            new_node = check_node_value(event.pos)
            if new_node is not None:
                node = new_node
                print(f"Node value changed to {node}")

    # 배경 이미지를 화면에 그리기
    screen.blit(background, (0, 0))

    # 화면 업데이트
    pygame.display.update()

# Pygame 종료
pygame.quit()
sys.exit()
