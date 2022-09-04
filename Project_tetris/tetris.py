import pygame
pygame.init()

screen_width = 300
screen_height = 600

#color
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0 , 0)

clock = pygame.time.Clock

screen = pygame.display.set_mode((screen_width, screen_height)) # 스크린 크기 및 변수선언

pygame.display.set_caption("TETRIS_MYUNGJUN") # 캡션

gaming = True
while gaming:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
        
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.type == pygame.K_LEFT: # 왼쪽 키를 눌렀을때
                pass
            elif event.type == pygame.K_RIGHT: # 오른쪽 키를 눌렀을때
                pass
            elif event.type == pygame.K_UP: # 위쪽 키를 눌렀을때
                pass
            elif event.type ==pygame.K_DOWN: # 아래쪽 키를 눌렀을때
                pass


    screen.fill(white)

tetris_1 = [[1,1,0],[0,1,0],[0,1,0]]
tetris_2 = [[1,1,0],[0,1,1],[0,0,0]]
tetris_3 = [[1,1,0],[1,1,0],[1,1,0]]

