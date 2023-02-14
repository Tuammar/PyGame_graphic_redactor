import pygame

pygame.init()
clock = pygame.time.Clock()
window_size = (1000, 700)
screen = pygame.display.set_mode(window_size)

pygame.init()
running = True
screen.fill("white")
f = 0
color = 'black'
cur_color = color
cur_thickness = 10


while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION and f == 1:
            pygame.draw.circle(screen, cur_color, [event.pos[0], event.pos[1]], cur_thickness)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                f = 1
                if cur_color != color:
                    cur_color = color
            elif event.button == 3:
                f = 1
                cur_color = 'white'
        elif event.type == pygame.MOUSEBUTTONUP:
            f = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                incol = input().split()
                if len(incol) == 3:
                    incol = (int(incol[0]), int(incol[1]), int(incol[2]))
                else:
                    incol = incol[0]
                try:
                    pygame.draw.line(screen, incol, (1001, 1), (1001, 1))
                    color = incol
                except ValueError:
                    print('Неверный формат цвета')
            elif event.key == pygame.K_c:
                screen.fill('white')
            elif event.key == pygame.K_t:
                try:
                    t = int(input())
                    cur_thickness = t
                except ValueError:
                    print('Неверный формат толщины')
        elif event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(300)
