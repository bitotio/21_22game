import pygame
pygame.init()
# Задаем размеры экрана
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.mouse.set_visible(False)
# Задаем заголовок окна
pygame.display.set_caption ("Полет самолета")
# Загружаем фоновое изображение
background_image = pygame.image.load ("sky.jpg"). convert()
# Загружаем изображение самолета
plane_image = pygame.image.load("plane.jpg"). convert ()
# Отразим горизонтально
plane_image = pygame.transform.flip(plane_image, True, False)
# Делаем фоновый цвет самолета прозрачным
plane_image. set_colorkey ((255, 255, 255))
plane_rect = plane_image.get_rect()
plane2_image = pygame. image. load("plane2.jpg"). convert_alpha()
plane2_rect = plane2_image.get_rect ()

clock = pygame. time.Clock()
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame. QUIT:
            running = False

    screen. blit (background_image, [0, 0])

    mouse_position = pygame.mouse.get_pos ()

    plane2_rect.x= mouse_position [0]
    plane2_rect. y = mouse_position [1]

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and plane_rect.left > 5:
        plane_rect.x -= 5
    if keys [pygame.K_RIGHT] and plane_rect.right < screen_width - 5:
        plane_rect.x += 5
    if keys[pygame.K_UP] and plane_rect. top > 5:
        plane_rect.y -= 5
    if keys[pygame.K_DOWN] and plane_rect.bottom < screen_height - 5:
        plane_rect.y += 5
    screen.blit(plane_image, plane_rect)
    screen.blit(plane2_image, plane2_rect)

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()